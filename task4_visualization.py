import pandas as pd
import matplotlib.pyplot as plt
import os

file_path = "data/trends_analysed.csv"
df = pd.read_csv(file_path)

if not os.path.exists("outputs"):
    os.makedirs("outputs")

def short_title(title):
    if len(title) > 50:
        return title[:50] + "..."
    return title

# Chart 1: Top 10 stories by score
top_10 = df.sort_values("score", ascending=False).head(10)
titles = [short_title(title) for title in top_10["title"]]
scores = top_10["score"]
plt.figure(figsize=(10, 6))
plt.barh(titles, scores)
plt.xlabel("Score")
plt.ylabel("Story Title")
plt.title("Top 10 Stories by Score")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("outputs/chart1_top_stories.png")
plt.show()

# Chart 2: Stories per category
category_counts = df["category"].value_counts()
plt.figure(figsize=(8, 5))
plt.bar(category_counts.index, category_counts.values,
        color=["blue", "green", "orange", "red", "purple"])
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Stories per Category")
plt.tight_layout()
plt.savefig("outputs/chart2_categories.png")
plt.show()

# Chart 3: Score vs Comments
popular = df[df["is_popular"] == True]
not_popular = df[df["is_popular"] == False]
plt.figure(figsize=(8, 5))
plt.scatter(popular["score"], popular["num_comments"], label="Popular")
plt.scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")
plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs Comments")
plt.legend()
plt.tight_layout()
plt.savefig("outputs/chart3_scatter.png")
plt.show()

# Bonus Dashboard
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
fig.suptitle("TrendPulse Dashboard")

# dashboard chart 1
axes[0].barh(titles, scores)
axes[0].set_title("Top 10 Stories")
axes[0].set_xlabel("Score")
axes[0].set_ylabel("Title")
axes[0].invert_yaxis()

# dashboard chart 2
axes[1].bar(category_counts.index, category_counts.values,
            color=["blue", "green", "orange", "red", "purple"])
axes[1].set_title("Stories per Category")
axes[1].set_xlabel("Category")
axes[1].set_ylabel("Count")
axes[1].tick_params(axis="x", rotation=45)

# dashboard chart 3
axes[2].scatter(popular["score"], popular["num_comments"], label="Popular")
axes[2].scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")
axes[2].set_title("Score vs Comments")
axes[2].set_xlabel("Score")
axes[2].set_ylabel("Comments")
axes[2].legend()
plt.tight_layout()
plt.savefig("outputs/dashboard.png")
plt.show()
print("Charts saved in outputs folder")
