from pathlib import Path
import pandas as pd

# LOAD THE RAW DATASET
project_folder = Path(__file__).resolve().parent.parent
file_path = project_folder / "data" / "raw" / "sample_-_superstore.xls"

df = pd.read_excel(file_path)

# CLEAN POSTAL CODES
# Store postal codes as text to preserve leading zeros

df["Postal Code"] = df["Postal Code"].astype(str)

# Restore missing leading zeros in four-digit US ZIP codes
us_mask = df["Country/Region"] == "United States"

four_digit_zip_mask = (
us_mask
& df["Postal Code"].str.fullmatch(r"\d{4}")
)

df.loc[four_digit_zip_mask, "Postal Code"] = (
df.loc[four_digit_zip_mask, "Postal Code"].str.zfill(5)
)

# Display the results
print("POSTAL CODE CLEANING RESULTS")
print("Total rows:", len(df))
print("Total columns:", len(df.columns))
print("Postal Code data type:", df["Postal Code"].dtype)
print("Four-digit US ZIP codes corrected:", four_digit_zip_mask.sum())

print("\nExamples of cleaned US ZIP codes:")
print(
df.loc[four_digit_zip_mask, ["City", "State/Province", "Postal Code"]]
.head(10)
.to_string(index=False)
)

print("\nSample Canadian postal-code prefixes:")
print(
df.loc[
df["Country/Region"] == "Canada",
["City", "Postal Code"]
].head(5).to_string(index=False)
)

# SAVE THE CLEANED DATASET
output_folder = project_folder / "data" / "processed"
output_folder.mkdir(parents=True, exist_ok=True)

output_file = output_folder / "cleaned_superstore.csv"

df.to_csv(output_file, index=False)

print("\nCLEANED DATASET SAVED")
print("Saved location:", output_file)
print("Rows saved:", len(df))
print("Columns saved:", len(df.columns))

# VALIDATE THE SAVED DATASET

cleaned_df = pd.read_csv(output_file)

print("\nFINAL DATA VALIDATION")
print("File exists:", output_file.exists())
print("Rows in saved file:", len(cleaned_df))
print("Columns in saved file:", len(cleaned_df.columns))
print("Missing values:", cleaned_df.isnull().sum().sum())
print("Duplicate Row IDs:", cleaned_df["Row ID"].duplicated().sum())

print("\nFirst five cleaned postal codes:")
print(
cleaned_df[
["City", "State/Province", "Postal Code"]
].head().to_string(index=False)
)
