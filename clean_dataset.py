import pandas as pd

INPUT_FILE = "dataset.csv"
OUTPUT_FILE = "clean_dataset.csv"

df = pd.read_csv(INPUT_FILE)

print("Original rows:", len(df))

# Required columns check
required_columns = {"url", "label"}

if not required_columns.issubset(df.columns):
    print("Error: dataset must contain 'url' and 'label' columns")
    exit()

# Remove missing values
df = df.dropna(subset=["url", "label"])

# Convert URL to string
df["url"] = df["url"].astype(str).str.strip()

# Convert label to numeric
df["label"] = pd.to_numeric(df["label"], errors="coerce")

# Remove invalid labels
df = df[df["label"].isin([0, 1])]

# Remove empty URLs
df = df[df["url"] != ""]

# Remove duplicate URLs
df = df.drop_duplicates(subset=["url"])

# Keep only required columns
df = df[["url", "label"]]

# Convert label to integer
df["label"] = df["label"].astype(int)

# Save cleaned dataset
df.to_csv(OUTPUT_FILE, index=False)

print("Cleaned rows :", len(df))
print("\nClass distribution:")
print(df["label"].value_counts())

print("\nClean dataset saved as:", OUTPUT_FILE)
