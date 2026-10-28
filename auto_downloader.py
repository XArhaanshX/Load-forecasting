import pandas as pd
import requests
import os

# read the csv
df = pd.read_csv("literature_review.csv")

# main papers folder
base_folder = "papers"
os.makedirs(base_folder, exist_ok=True)

for i, row in df.iterrows():

    url = row["pdf"]
    title = row["title"]
    year = str(row["year"])

    # create year folder
    year_folder = os.path.join(base_folder, year)
    os.makedirs(year_folder, exist_ok=True)

    # safe filename
    safe_title = "".join(c for c in title if c.isalnum() or c in " _-").rstrip()
    filename = f"{year}_{safe_title}.pdf"

    filepath = os.path.join(year_folder, filename)

    try:
        response = requests.get(url)
        response.raise_for_status()

        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"Downloaded: {year}/{filename}")

    except Exception as e:
        print(f"Failed: {title}")