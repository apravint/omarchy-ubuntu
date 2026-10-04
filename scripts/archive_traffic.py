#!/usr/bin/env python3
"""
GitHub Traffic & Clone Archiver for @apravint
Archives clone and view traffic beyond GitHub's 14-day limit.
https://github.com/apravint/omarchy-ubuntu
"""

import os
import sys
import json
import csv
import urllib.request
import urllib.error
from datetime import datetime, timezone

OWNER = os.environ.get("GITHUB_OWNER", "apravint")
TOKEN = os.environ.get("TRAFFIC_ACTION_TOKEN") or os.environ.get("GITHUB_TOKEN")
OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "traffic_data")

if not TOKEN:
    print("Error: TRAFFIC_ACTION_TOKEN or GITHUB_TOKEN environment variable is required.")
    sys.exit(1)

HEADERS = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {TOKEN}",
    "X-GitHub-Api-Version": "2022-11-28",
    "User-Agent": "GitHub-Traffic-Archiver"
}

def gh_api_get(endpoint):
    url = f"https://api.github.com/{endpoint.lstrip('/')}"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code} for {url}")
        return None
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def merge_traffic_data(file_path, new_items, key_field="clones"):
    """
    Merges new traffic entries with existing CSV history.
    CSV header: date,count,uniques
    """
    history = {}
    if os.path.exists(file_path):
        with open(file_path, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            header = next(reader, None)
            for row in reader:
                if len(row) >= 3:
                    history[row[0]] = (int(row[1]), int(row[2]))

    for item in new_items:
        ts = item.get("timestamp", "")[:10] # YYYY-MM-DD
        if ts:
            count = item.get("count", 0)
            uniques = item.get("uniques", 0)
            history[ts] = (count, uniques)

    sorted_dates = sorted(history.keys())
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "count", "uniques"])
        for d in sorted_dates:
            cnt, unq = history[d]
            writer.writerow([d, cnt, unq])

    total_count = sum(cnt for cnt, _ in history.values())
    return len(sorted_dates), total_count

def get_repos_to_track():
    """Fetches non-fork public repositories owned by the user, prioritized."""
    repos_data = gh_api_get(f"users/{OWNER}/repos?per_page=100&type=owner&sort=pushed")
    if not repos_data or not isinstance(repos_data, list):
        # Fallback to key known projects
        return [
            {"name": "omarchy-ubuntu", "fork": False, "stargazers_count": 0, "forks_count": 0},
            {"name": "clawdbot", "fork": False, "stargazers_count": 0, "forks_count": 0},
            {"name": "waybar-theme-sync", "fork": False, "stargazers_count": 0, "forks_count": 0},
            {"name": "dual-desktop-ubuntu", "fork": False, "stargazers_count": 0, "forks_count": 0},
            {"name": "win11-kde-plasma", "fork": False, "stargazers_count": 0, "forks_count": 0},
            {"name": "nanoclaw", "fork": False, "stargazers_count": 0, "forks_count": 0},
            {"name": "Video-Editor", "fork": False, "stargazers_count": 0, "forks_count": 0}
        ]
    
    # Filter to non-fork repos or repos created by user
    tracked = [r for r in repos_data if not r.get("fork", False)]
    return tracked

def main():
    print(f"📊 Starting GitHub Traffic Archiver for @{OWNER}...")
    repos = get_repos_to_track()
    print(f"Found {len(repos)} source repositories to monitor.")

    summary_rows = []
    overall_clones_14d = 0
    overall_clones_lifetime = 0
    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    for repo in repos:
        name = repo["name"]
        stars = repo.get("stargazers_count", 0)
        forks = repo.get("forks_count", 0)

        # 1. Clones
        clones_data = gh_api_get(f"repos/{OWNER}/{name}/traffic/clones")
        c_14d_count = clones_data.get("count", 0) if clones_data else 0
        c_14d_uniques = clones_data.get("uniques", 0) if clones_data else 0
        c_list = clones_data.get("clones", []) if clones_data else []

        c_file = os.path.join(OUTPUT_DIR, "data", name, "clones.csv")
        c_days, c_lifetime = merge_traffic_data(c_file, c_list, "clones")

        # 2. Views
        views_data = gh_api_get(f"repos/{OWNER}/{name}/traffic/views")
        v_14d_count = views_data.get("count", 0) if views_data else 0
        v_14d_uniques = views_data.get("uniques", 0) if views_data else 0
        v_list = views_data.get("views", []) if views_data else []

        v_file = os.path.join(OUTPUT_DIR, "data", name, "views.csv")
        v_days, v_lifetime = merge_traffic_data(v_file, v_list, "views")

        # 3. Referrers
        ref_data = gh_api_get(f"repos/{OWNER}/{name}/traffic/popular/referrers")
        if ref_data and isinstance(ref_data, list):
            ref_file = os.path.join(OUTPUT_DIR, "data", name, "referrers.csv")
            os.makedirs(os.path.dirname(ref_file), exist_ok=True)
            with open(ref_file, mode="w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["referrer", "count", "uniques"])
                for r in ref_data:
                    writer.writerow([r.get("referrer"), r.get("count"), r.get("uniques")])

        overall_clones_14d += c_14d_count
        overall_clones_lifetime += c_lifetime

        # Add to summary if it has activity or stars
        if c_14d_count > 0 or v_14d_count > 0 or stars > 0 or c_lifetime > 0:
            summary_rows.append({
                "name": name,
                "clones_14d": f"{c_14d_count} ({c_14d_uniques} unique)",
                "clones_lifetime": c_lifetime,
                "views_14d": f"{v_14d_count} ({v_14d_uniques} unique)",
                "views_lifetime": v_lifetime,
                "stars": stars,
                "forks": forks,
                "c_count": c_14d_count
            })

    # Sort summary by 14d clones descending
    summary_rows.sort(key=lambda x: (x["clones_lifetime"], x["c_count"]), reverse=True)

    # Generate README.md in output dir
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    readme_path = os.path.join(OUTPUT_DIR, "README.md")

    md_lines = [
        f"# 📈 GitHub Traffic & Clone Archive (`@{OWNER}`)",
        f"Automated permanent traffic analytics preserving clone and visitor records beyond GitHub's 14-day window.",
        f"\n**Last Updated:** `{now_utc}`  ",
        f"**Active Monitored Repositories:** `{len(repos)}`  ",
        f"**Total Clones (14-day rolling):** `{overall_clones_14d:,}`  ",
        f"**Total Cumulative Clones Tracked:** `{overall_clones_lifetime:,}`\n",
        "## 🏆 Traffic & Clone Leaderboard",
        "| Repository | Clones (Last 14d) | Lifetime Clones | Views (Last 14d) | Stars | History |",
        "| :--- | :--- | :--- | :--- | :---: | :---: |"
    ]

    for row in summary_rows:
        repo_link = f"[{row['name']}](https://github.com/{OWNER}/{row['name']})"
        csv_link = f"[clones.csv](data/{row['name']}/clones.csv)"
        md_lines.append(
            f"| **{repo_link}** | `{row['clones_14d']}` | **`{row['clones_lifetime']:,}`** | `{row['views_14d']}` | ⭐ {row['stars']} | {csv_link} |"
        )

    md_lines.extend([
        "\n---",
        "### 📂 Directory Structure",
        "```",
        "data/",
        "└── <repo-name>/",
        "    ├── clones.csv     # Cumulative daily clone counts & unique cloners",
        "    ├── views.csv      # Cumulative daily page views & unique visitors",
        "    └── referrers.csv  # Top referring sites and search engines",
        "```",
        "\n*Archived automatically every day via GitHub Actions.*"
    ])

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines) + "\n")

    print(f"✓ Summary generated at {readme_path}")
    print(f"✓ Total 14-day clones: {overall_clones_14d:,} | Cumulative: {overall_clones_lifetime:,}")

    # Write GitHub Actions Step Summary if in CI
    step_summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if step_summary:
        try:
            with open(step_summary, "a", encoding="utf-8") as f:
                f.write(f"### 📈 Traffic & Clone Summary (`@{OWNER}`)\n\n")
                f.write(f"- **14-Day Rolling Clones:** `{overall_clones_14d:,}`\n")
                f.write(f"- **Cumulative Clones Archived:** `{overall_clones_lifetime:,}`\n\n")
                f.write("| Repository | Clones (14d) | Lifetime Clones | Views (14d) |\n")
                f.write("| :--- | :--- | :--- | :--- |\n")
                for r in summary_rows[:15]:
                    f.write(f"| **{r['name']}** | {r['clones_14d']} | {r['clones_lifetime']} | {r['views_14d']} |\n")
        except Exception as e:
            print(f"Could not write step summary: {e}")

if __name__ == "__main__":
    main()
