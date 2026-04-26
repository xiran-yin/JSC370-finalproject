# Data Directory

This directory contains cached copies of data that need stable snapshots for reproducibility.

## Files

### `reddit_ttc_posts.csv`

Cached snapshot of recent posts from the Reddit subreddit [r/TTC](https://www.reddit.com/r/TTC/) matching the search query `delay`. Used as input for the NLP / sentiment / topic-modelling section of the [main report](../final_report.qmd).

| Column | Description |
|--------|-------------|
| `created_utc` | ISO 8601 timestamp of when the post was created |
| `text` | Concatenation of post title and body (selftext) |
| `upvotes` | Net upvote score at time of fetch |

**Why is this cached?** Reddit's `?sort=new` endpoint returns a moving window of the latest 100 posts, so re-fetching on every report render would yield non-reproducible results. The cached CSV pins the analysis to a fixed sample.

**How to refresh.** From the project root, run:

```bash
python fetch_reddit.py
```

This will overwrite `reddit_ttc_posts.csv` with a fresh snapshot.

## Other Data Sources

The other two data sources used by this project are **not cached** in this directory because they are deterministic and version-controlled at their respective public APIs:

- **Weather data** — fetched live on each Quarto render from the [Open-Meteo Historical Weather API](https://open-meteo.com/en/docs/historical-weather-api). The historical archive is stable, so re-running the project produces identical weather records.
- **TTC subway delay data** — fetched live from the [City of Toronto Open Data CKAN API](https://open.toronto.ca/dataset/ttc-subway-delay-data/). The City updates this dataset monthly with new records but does not modify historical entries.
