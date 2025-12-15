import pandas as pd
from pathlib import Path

# Path to data folder
data_path = Path("data")

# Read all CSV files
dfs = []
for file in data_path.glob("*.csv"):
    df = pd.read_csv(file)
    dfs.append(df)

# Combine all data into one DataFrame
combined_df = pd.concat(dfs, ignore_index=True)

# Keep only Pink Morsels
pink_df = combined_df[combined_df["product"] == "Pink Morsel"]

# Create Sales column
pink_df["Sales"] = pink_df["quantity"] * pink_df["price"]

# Select required columns
final_df = pink_df[["Sales", "date", "region"]]

# Rename columns
final_df = final_df.rename(columns={
    "date": "Date",
    "region": "Region"
})

# Save output file
final_df.to_csv("processed_sales.csv", index=False)

print("processed_sales.csv created successfully")
