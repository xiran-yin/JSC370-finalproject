# JSC370 Final Project — Weather & TTC Subway Delays

**Author:** Xiran Yin
**Course:** JSC370 — Data Science II, University of Toronto
**Date:** April 26, 2026

**Project website:** <https://xiran-yin.github.io/JSC370-finalproject/>
**Full report (PDF):** [download](https://xiran-yin.github.io/JSC370-finalproject/final_report.pdf)
**GitHub repo:** <https://github.com/xiran-yin/JSC370-finalproject>

---

## Project Description

This project investigates whether daily weather conditions in Toronto can predict TTC subway delays. Twelve years of historical weather data (2014–2025) from the Open-Meteo API are merged with the City of Toronto's complete public record of subway delay incidents to build:

1. **Inferential models** (OLS multiple regression, Generalized Additive Model) quantifying the weather → delay relationship, including non-linear effects.
2. **Predictive ML models** (Linear/Logistic Regression, Random Forest, XGBoost) for both regression (predicting total daily delay duration) and classification (predicting severe delay days, defined as the top quartile of total delay).

The website also includes three fully interactive Plotly visualizations (Homework 5).

## Data Sources

| Source | Type | Access |
|--------|------|--------|
| [Open-Meteo Historical Weather API](https://open-meteo.com/en/docs/historical-weather-api) | Daily Toronto weather, 2014-01-01 to 2026-01-01 | Free public API, no key required |
| [Toronto Open Data — TTC Subway Delays](https://open.toronto.ca/dataset/ttc-subway-delay-data/) | Every recorded subway delay 2014–2025 | CKAN API |

Both data sources are fetched **live** from their public APIs every time the project is rendered. There are no API keys, authentication tokens, or local credentials required.

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

### Render the website

From the project root:

```bash
quarto render
```

This re-fetches weather and TTC data live from their public APIs, fits all models, and rebuilds the entire website to `docs/`. The rendered website is served by GitHub Pages.

### Render only the PDF version of the report

```bash
quarto render final_report.qmd --to pdf
```

## Reproducibility Notes

- **All data sources are live public APIs** — no local data files are required to reproduce the analysis.
- **Random seeds are set** in all stochastic steps (XGBoost, Random Forest, train/test splits) via `np.random.seed(42)` and `random_state=42`.
- **Train/test split is chronological** (train: 2014-01-01 to 2023-12-31, test: 2024-01-01 onward) to prevent temporal leakage.

## License

Code is released under the MIT License. Data are owned by their respective providers (Open-Meteo, City of Toronto); please consult their terms of service before redistribution.