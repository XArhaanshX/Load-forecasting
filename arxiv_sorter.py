import arxiv
import pandas as pd

search = arxiv.Search(
    query='("load forecasting" OR "electricity demand forecasting") AND ("LSTM" OR "machine learning" OR "deep learning")',
    max_results=50,
    sort_by=arxiv.SortCriterion.SubmittedDate
)

papers = []

for result in search.results():
    papers.append({
        "title": result.title,
        "authors": ", ".join([a.name for a in result.authors]),
        "year": result.published.year,
        "journal": result.journal_ref,
        "summary": result.summary,
        "pdf": result.pdf_url
    })

df = pd.DataFrame(papers)

# sorting in descenorder by years
df = df.sort_values(by="year", ascending=False)

# adding serial nummber columns
df.insert(0, "sr_no", range(1, len(df) + 1))

# saving the file for easy viewing experience
df.to_excel("literature_review.xlsx", index=False)
df.to_csv("literature_review.csv", index=False)

print("Files saved: literature_review.xlsx and literature_review.csv")