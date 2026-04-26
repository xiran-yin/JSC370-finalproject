# JSC370 Final Project — Weather & TTC Subway Delays

**Author:** Xiran Yin
**Course:** JSC370 — Data Science II, University of Toronto
**Date:** April 26, 2026

🌐 **Project website:** <https://xiran-yin.github.io/JSC370-finalproject/>
📄 **Full report (PDF):** [available on the website](https://xiran-yin.github.io/JSC370-finalproject/final_report.pdf)
🎥 **5-minute presentation:** see Quercus / link on the website
📦 **GitHub repo:** <https://github.com/xiran-yin/JSC370-finalproject>

---

## Project Description

This project investigates whether daily weather conditions in Toronto can predict TTC subway delays. Twelve years of historical weather data (2014–2025) from the Open-Meteo API are merged with the City of Toronto's complete public record of subway delay incidents to build:

1. **Inferential models** (OLS, GAM) quantifying the weather → delay relationship,
2. **Predictive ML models** (Linear/Logistic Regression, Random Forest, XGBoost) for both regression (predicting total daily delay) and classification (predicting severe delay days), and
3. **NLP analysis** (VADER sentiment, LDA topic modelling) of rider posts on Reddit's `r/TTC` as an independent qualitative validation.

The website includes three fully interactive Plotly visualizations (Homework 5).

## Data Sources

| Source | Type | Access |
|--------|------|--------|
| [Open-Meteo Historical Weather API](https://open-meteo.com/en/docs/historical-weather-api) | Daily Toronto weather, 2014-01-01 to 2026-01-01 | Free public API, no key |
| [Toronto Open Data — TTC Subway Delays](https://open.toronto.ca/dataset/ttc-subway-delay-data/) | Every recorded subway delay 2014–2025 | CKAN API |
| [Reddit `r/TTC`](https://www.reddit.com/r/TTC/) | ~100 rider posts mentioning "delay" | Reddit JSON API; cached in [`data/reddit_ttc_posts.csv`](data/reddit_ttc_posts.csv) |

## Repository Structure

```
JSC370-finalproject/
├── README.md                # this file
├── _quarto.yml              # Quarto website config
├── styles.css               # site styling
├── index.qmd                # website home page
├── final_report.qmd         # full written report (HTML + PDF source)
├── viz.qmd                  # 3 interactive Plotly figures (HW5)
├── fetch_reddit.py          # script to refresh Reddit cache
├── presentation_outline.md  # talking points for the 5-min video
├── data/
│   ├── README.md            # data documentation
│   └── reddit_ttc_posts.csv # cached Reddit posts
└── docs/                    # rendered website (auto-generated, GitHub Pages root)
```

## How to Reproduce

### Prerequisites

- Python 3.10+
- [Quarto](https://quarto.org/) 1.4+

### Install Python dependencies

```bash
pip install -r requirements.txt
```

(or install the packages listed at the top of `final_report.qmd` individually.)

### Render the website

From the project root:

```bash
# Optionally refresh the Reddit cache first (live fetch)
python fetch_reddit.py

# Render the full website (re-fetches weather and TTC data live from public APIs)
quarto render
```

The rendered website is written to `docs/` and is served by GitHub Pages.

### Render only the PDF version of the report

```bash
quarto render final_report.qmd --to pdf
```

## Reproducibility Notes

- **Weather data and TTC delay data** are fetched live from public APIs on every render. Both sources are historically stable, so re-running the project produces identical (or, for the TTC, monotonically growing) datasets.
- **Reddit data** is cached in `data/reddit_ttc_posts.csv` because the Reddit `?sort=new` endpoint is non-deterministic. Run `python fetch_reddit.py` to refresh.
- **Random seeds** are set in all stochastic steps (XGBoost, Random Forest, train/test splits, LDA) via `np.random.seed(42)` and `random_state=42`.
- **Train/test split is chronological** (train: 2014–2023, test: 2024–2025) to prevent temporal leakage.

## License

Code is released under the MIT License. Data are owned by their respective providers (Open-Meteo, City of Toronto, Reddit users); please consult their terms of service before redistribution.
