import pandas as pd
import numpy as np

# 1. Load CSV file
file_path = "data/trends_clean.csv"
df = pd.read_csv(file_path)
print("Loaded data:", df.shape)
print("\nFirst 5 rows:")
print(df.head())
avg_score = df["score"].mean()
avg_comments = df["num_comments"].mean()
print("\nAverage score :", int(avg_score))
print("Average comments:", int(avg_comments))

# 2. NumPy Analysis
scores = df["score"].values
print("\n--- NumPy Stats ---")
print("Mean score :", int(np.mean(scores)))
print("Median score:", int(np.median(scores)))
print("Std deviation:", int(np.std(scores)))
print("Max score :", int(np.max(scores)))
print("Min score :", int(np.min(scores)))
most_cat = df["category"].value_counts().idxmax()
count = df["category"].value_counts().max()
print("\nMost stories in:", most_cat, f"({count} stories)")
top_story = df.loc[df["num_comments"].idxmax()]
print("\nMost commented story:", f"\"{top_story['title']}\" - {top_story['num_comments']} comments")

# 3. Add new columns
df["engagement"] = df["num_comments"] / (df["score"] + 1)
df["is_popular"] = df["score"] > avg_score

# 4. Save result
output_file = "data/trends_analysed.csv"
df.to_csv(output_file, index=False)
print("\nSaved to", output_file)
