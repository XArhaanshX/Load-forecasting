# Load Forecasting: Literature Review

A research survey of machine-learning methods for electrical load forecasting: the 50 most recent arXiv papers on the topic, collected and summarised by script, plus a write-up that compares a shortlist of them.

The implementation work that grew out of it lives in [Time-Series-Load-Forecasting](https://github.com/XArhaanshX/Time-Series-Load-Forecasting), [HFLF-Temporal-Resolution-Study](https://github.com/XArhaanshX/HFLF-Temporal-Resolution-Study) and [Stochastic-Signal-Integration-in-HF-Load-Data](https://github.com/XArhaanshX/Stochastic-Signal-Integration-in-HF-Load-Data).

## Contents

| Path | What it is |
| --- | --- |
| `arxiv_sorter.py` | Queries arXiv for the 50 most recently submitted papers matching `("load forecasting" OR "electricity demand forecasting") AND ("LSTM" OR "machine learning" OR "deep learning")`, sorts them by year and writes the table below. |
| `literature_review.csv`, `literature_review.xlsx` | One row per paper: title, authors, year, journal, abstract and PDF link. |
| `auto_downloader.py` | Downloads every PDF in the table into `papers/<year>/<year>_<title>.pdf`. |
| `papers/` | The downloaded papers (2025 and 2026). |
| `2023/`, `2026/` | Papers added by hand from outside the arXiv query. |
| `Literature_Review_for_A_Machine_Learning_Approach_to_Electrical_Load_Forecasting (5).pdf` | The write-up: a comparison table of selected papers by model, data source, results, forecasting horizon (short, medium, long term), citations and patents. |

## Rebuild it

```bash
pip install arxiv pandas openpyxl requests
python arxiv_sorter.py      # refresh literature_review.csv / .xlsx
python auto_downloader.py   # download the PDFs into papers/
```

The query returns the newest submissions, so a rerun picks up a different set of papers.
