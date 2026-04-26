# 5-Minute Presentation Outline

## Recording instructions

Record a screencast of the website with voice-over. Walk through each section
roughly in the order below. Aim for ~5 minutes total — practice once with a
timer to stay on schedule. Upload the resulting video to Quercus and link it
from the README / website.

Suggested tools: Loom, OBS Studio, or QuickTime (macOS).

---

## Slot-by-slot script

### 0:00 – 0:30 — Hook + Question (30 sec)
**On screen:** the home page (`index.qmd`).

> "TTC carries over a million riders a day. Some days the system runs smoothly;
> other days it grinds to a halt. The question this project asks is simple:
> can we predict, from weather alone, which days the subway will be a mess?"

Briefly point at the four "Key Findings" cards, but don't read them all.

### 0:30 – 1:15 — Data and methods (45 sec)
**On screen:** scroll to the "Data Sources" table on the home page, then click
into the **Methods** section of `final_report.qmd`.

> "I merged three independent data sources: 12 years of Toronto weather from
> Open-Meteo, every recorded TTC subway delay from the City's open-data portal,
> and a sample of rider posts from r/TTC for qualitative validation. The merged
> dataset has just over 4,300 daily observations from 2014 to 2025."
>
> "I used four classes of methods, in increasing complexity: OLS regression as
> a baseline, GAM for non-linearity, three machine-learning models — logistic
> regression, random forest, and XGBoost — and NLP for sentiment and topic
> modelling on the Reddit posts."

### 1:15 – 2:30 — Inferential findings (75 sec)
**On screen:** scroll to **Figure 5b** (the GAM temperature smooth).

> "The headline inferential result is the U-shape in temperature. OLS finds
> temperature non-significant — but that's because OLS forces a single linear
> slope. The GAM smooth shows clearly that delays are lowest in the 5 to 20
> degree range and rise at both extremes. That matches two known operational
> mechanisms: frozen track switches in winter, rail steel buckling in summer."

**On screen:** scroll up to **Table 3** (OLS).

> "On the linear side, snowfall has roughly 10 times the per-unit impact of
> rain — about 14 minutes of delay per centimetre of snow versus 1.2 minutes
> per millimetre of rain. Weekends lose about 32 fewer minutes to delay than
> weekdays, holding weather constant."

### 2:30 – 3:30 — Predictive ML (60 sec)
**On screen:** scroll to **Tables 4 and 5** (regression and classification
performance), then to **Figure 8** (feature importance) and **Figure 6** (ROC
curves).

> "For prediction, I split the data chronologically — train on 2014 through
> 2023, test on 2024 to 2025 — and compared three models. XGBoost wins on both
> tasks: regression R-squared around 0.18, and classification ROC-AUC around
> 0.74 for predicting top-quartile severe-delay days. The R-squared looks
> modest, but remember that most of the day-to-day delay variance comes from
> non-weather causes the model can't see — random equipment failures, security
> incidents, that kind of thing."
>
> "The feature-importance plot is the satisfying part. The top three features
> XGBoost picks — snowfall, mean temperature, day-of-week — are exactly the
> three predictors that the OLS and GAM analyses flagged as most consequential.
> Two completely different model classes, same answer."

### 3:30 – 4:15 — Interactive viz + NLP (45 sec)
**On screen:** click to the **Interactive Visualizations** page.

> "The site has three interactive Plotly figures. This first one is a
> 4,400-point time series with weather coloring and a 30-day rolling mean —
> hover over any point to see that day's exact weather. The third one combines
> XGBoost's feature importance with a partial-dependence dropdown so you can
> see exactly how the model's prediction depends on, say, snowfall."

**On screen:** scroll to the NLP section of the main report (**Figure 9**).

> "Finally, as an independent check, I did sentiment analysis and topic
> modelling on Reddit r/TTC posts. The most negative sentiment clusters on
> infrastructure-related posts — Topic 3 — which lines up with the
> quantitative finding that infrastructure-stressing weather drives the worst
> delays. Riders agree with the model."

### 4:15 – 4:50 — Limitations + closing (35 sec)
**On screen:** the **Conclusions** section of `final_report.qmd`.

> "Three honest limitations. First, weather only explains about 18% of delay
> variance — most variance is from things the data doesn't capture. Second,
> aggregating to a single daily total hides line-level differences; Line 1
> being underground, for instance, is much less weather-sensitive. Third,
> VADER misclassifies sarcasm, which is everywhere on r/TTC."
>
> "But the practical story stands up. Weather has a real, measurable, and
> directionally-clear effect on TTC reliability, and a flexible ML model
> trained on it generalizes to a held-out future window. If you wanted to
> deploy this against next-day weather forecasts to pre-position maintenance
> crews, you could."
>
> "Thanks — code, data, and the full report are linked from the home page."

### 4:50 – 5:00 — Buffer
A few seconds of silence is fine. Don't rush.

---

## Things to point at on screen

| Time   | What to point at                                    |
|--------|------------------------------------------------------|
| 0:30   | The Data Sources table on `index.qmd`               |
| 1:30   | The temperature U-shape in Figure 5b                 |
| 2:00   | The snowfall coefficient in Table 3                  |
| 3:00   | The ROC curves in Figure 6                           |
| 3:15   | The feature importance bars in Figure 8              |
| 3:45   | The interactive timeseries (Figure 1 of viz page)   |
| 4:00   | The NLP topic-sentiment violin (Figure 9)            |

## Things to NOT do

- Don't read code on screen.
- Don't read tables row-by-row.
- Don't apologize for low R².
- Don't introduce new content the audience hasn't already seen on the site.

## Total target: 5:00 ± 0:15
