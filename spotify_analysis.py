import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Load Dataset ---
df = pd.read_excel("Spotify Global Chart 2024.xlsx")

# --- Clean Column Names ---
df.columns = df.columns.str.strip().str.lower()

# --- Convert 'streams' to Numeric ---
df["streams"] = pd.to_numeric(df["streams"], errors="coerce")

# --- Basic Info ---
print("Shape of dataset:", df.shape)
print("\nColumns:\n", df.columns.tolist())
print("\nMissing values:\n", df.isnull().sum())

# --- Task 1: Top 10 Most Streamed Songs ---
top10_songs = df.sort_values("streams", ascending=False).head(10)

plt.figure(figsize=(10,6))
sns.barplot(x="streams", y="track_name", data=top10_songs, hue="track_name", palette="viridis", legend=False)
plt.title("Top 10 Most Streamed Songs (2024)")
plt.xlabel("Streams")
plt.ylabel("Song")
plt.tight_layout()
plt.show()

# --- Task 2: Top 10 Artists by Total Streams ---
if "artist_names" in df.columns:
    top_artists = df.groupby("artist_names")["streams"].sum().sort_values(ascending=False).head(10)

    plt.figure(figsize=(10,6))
    sns.barplot(x=top_artists.values, y=top_artists.index, palette="magma")
    plt.title("Top 10 Artists by Total Streams (2024)")
    plt.xlabel("Total Streams")
    plt.ylabel("Artist")
    plt.tight_layout()
    plt.show()

# --- Task 3: Top Countries by Streams ---
if "country" in df.columns:
    top_countries = df.groupby("country")["streams"].sum().sort_values(ascending=False).head(10)

    plt.figure(figsize=(10,6))
    top_countries.plot(kind='bar', color='green')
    plt.title("Top 10 Countries by Streams")
    plt.xlabel("Country")
    plt.ylabel("Total Streams")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
# --- Task 4: Streams vs Rank ---
if "rank" in df.columns:
    plt.figure(figsize=(8,6))
    sns.scatterplot(data=df, x='rank', y='streams', alpha=0.6, color='purple')
    plt.title("Streams vs Rank")
    plt.xlabel("Rank")
    plt.ylabel("Streams")
    plt.tight_layout()
    plt.show()

# --- Task 5: Streams vs Danceability ---
if "danceability" in df.columns:
    plt.figure(figsize=(8,6))
    sns.scatterplot(data=df, x='danceability', y='streams', alpha=0.6, color='orange')
    plt.title("Streams vs Danceability")
    plt.xlabel("Danceability")
    plt.ylabel("Streams")
    plt.tight_layout()
    plt.show()

# --- Task 6: Correlation Heatmap ---
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Feature Correlation Heatmap")
plt.tight_layout()
plt.show()

