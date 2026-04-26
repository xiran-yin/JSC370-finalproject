"""
fetch_reddit.py
Re-fetch r/TTC posts and overwrite the local cache at data/reddit_ttc_posts.csv.

The final report and viz pages load this CSV. The CSV currently shipped in the
repo is a representative sample generated for demonstration purposes; running
this script will replace it with a fresh live snapshot from Reddit.

Usage:
    python fetch_reddit.py

Notes:
- The Reddit JSON API is unauthenticated and rate-limited. If you hit a 429
  error, wait 30s and retry.
- The 'new' sort returns the latest 100 posts matching the query, so the cache
  is a moving window. Each re-fetch produces a different snapshot.
"""

import os
import sys
import requests
import pandas as pd

REDDIT_URL = (
    "https://www.reddit.com/r/TTC/search.json"
    "?q=delay&restrict_sr=on&sort=new&limit=100"
)
HEADERS = {'User-Agent': 'Mozilla/5.0 UofT_JSC370_Final/1.0'}
OUT_PATH = "data/reddit_ttc_posts.csv"


def fetch():
    resp = requests.get(REDDIT_URL, headers=HEADERS, timeout=10)
    resp.raise_for_status()
    data = resp.json()

    posts = []
    for child in data['data']['children']:
        d = child['data']
        posts.append({
            'created_utc': pd.to_datetime(d['created_utc'], unit='s').isoformat(),
            'text':        f"{d.get('title', '')} {d.get('selftext', '')}",
            'upvotes':     d['score'],
        })
    return pd.DataFrame(posts)


def main():
    print(f"Fetching latest r/TTC delay posts ...")
    try:
        df = fetch()
    except requests.HTTPError as e:
        print(f"HTTP error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)

    if len(df) == 0:
        print("Warning: 0 posts returned. Cache not updated.")
        sys.exit(1)

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    df.to_csv(OUT_PATH, index=False)
    print(f"Saved {len(df)} posts to {OUT_PATH}")
    print(f"  Date range: {df['created_utc'].min()} to {df['created_utc'].max()}")


if __name__ == "__main__":
    main()
