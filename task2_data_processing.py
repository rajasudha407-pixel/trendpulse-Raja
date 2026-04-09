import pandas as pd
import os

file_path = "data/trends_20240115.json"

# 1. Load JSON file
try:
    df = pd.read_json(file_path)
    print("Loaded", len(df), "stories from", file_path)
except:
    print("Error loading file")
    df = pd.DataFrame()

# 2. Clean the data
df = df.drop_duplicates(subset=["post_id"])
print("After removing duplicates:", len(df))
df = df.dropna(subset=["post_id", "title", "score"])
print("After removing nulls:", len(df))
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)
df = df[df["score"] >= 5]
print("After removing low scores:", len(df))
df["title"] = df["title"].str.strip()

# 3. Save as CSV
if not os.path.exists("data"):
    os.makedirs("data")
output_file = "data/trends_clean.csv"
df.to_csv(output_file, index=False)
print("\nSaved", len(df), "rows to", output_file)

# print category summary
print("\nStories per category:")
print(df["category"].value_counts())
