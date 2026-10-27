from pathlib import Path
import pandas as pd

project_folder = Path(__file__).resolve().parent.parent

file_path = project_folder / "data" / "raw" / "sample_-_superstore.xls"

df = pd.read_excel(file_path)

print("FIRST FIVE ROWS")
print(df.head())

print("\nDATASET SHAPE")
print(df.shape)

print("\nCOLUMN NAMES")
print(df.columns.tolist())

print("\nDATA TYPES")
print(df.dtypes)

print("\nMISSING VALUES")
print(df.isnull().sum())

print("\nFULLY DUPLICATED ROWS")
print(df.duplicated().sum())

print("\nNUMERICAL SUMMARY")
print(df.describe())

print("\nDUPLICATE ROW IDs")
print(df["Row ID"].duplicated().sum())

#CHECK REPEATED ORDER IDs
print("\nREPEATED ORDER IDs")
print(df["Order ID"].duplicated().sum())

#CHECK REPEATED ORDER ID + PRODUCT ID COMBINATIONS
print("\nDUPLICATE ORDER-PRODUCT COMBINATIONS")
print(df.duplicated(subset=["Order ID", "Product ID"]).sum())

#CHECK TEXT FORMATTING
print("\nTEXT VALUES WITH LEADING OR TRAILING SPACES")

text_columns = df.select_dtypes(include=["object", "str"]).columns

for column in text_columns:
    count = (
        df[column]
        .dropna()
        .astype(str)
        .ne(df[column].dropna().astype(str).str.strip())
        .sum()
    )

    if count > 0:
        print(f"{column}: {count}")

print("\nORDERS SHIPPED BEFORE THEY WERE PLACED")
print((df["Ship Date"] < df["Order Date"]).sum())

print("\nZERO OR NEGATIVE SALES")
print((df["Sales"] <= 0).sum())
print("\nZERO OR NEGATIVE QUANTITY")
print((df["Quantity"] <= 0).sum())

print("\nDISCOUNT RANGE")
print(df["Discount"].min(), "to", df["Discount"].max())

#INVESTIGATE REPEATED ORDER-PRODUCT COMBINATIONS
duplicate_mask = df.duplicated(
    subset=["Order ID", "Product ID"],
    keep=False
)

duplicate_records = df[duplicate_mask].sort_values(
    by=["Order ID", "Product ID"]
)

print("\nREPEATED ORDER-PRODUCT RECORDS")
print(duplicate_records.to_string(index=False))

print("\nNUMBER OF AFFECTED RECORDS")
print(len(duplicate_records))

# INSPECT SUSPICIOUS RECORDS
rows_to_check = [1699, 1700, 391, 392]

print("\nINSPECTING SUSPICIOUS ROWS")
print(df[df["Row ID"].isin(rows_to_check)].to_string(index=False))

print("\nEXACT DUPLICATE CHECK FOR THESE ROWS")
selected_rows = df[df["Row ID"].isin(rows_to_check)]

print(
    selected_rows.duplicated(
        subset=df.columns.tolist(),
        keep=False
    )
)

# CHECK DUPLICATES EXCLUDING ROW ID
columns_to_compare = df.columns.drop("Row ID")

print("\nDUPLICATE RECORDS EXCLUDING ROW ID")
print(
    df.duplicated(
        subset=columns_to_compare,
        keep=False
    ).sum()
)

print("\nROWS THAT MATCH EXCLUDING ROW ID")
print(
    df[
        df.duplicated(
            subset=columns_to_compare,
            keep=False
        )
    ].sort_values("Order ID").to_string(index=False)
)

#CHECK DISTINCT VALUES IN IMPORTANT CATEGORICAL COLUMNS
columns_to_check = [
    "Ship Mode",
    "Segment",
    "Country/Region",
    "Region",
    "Category",
    "Sub-Category"
]

for column in columns_to_check:
    print(f"\n--- {column} ---")
    print("Unique values:", df[column].nunique())
    print(sorted(df[column].dropna().unique().tolist()))

#CHECK THE DATE RANGE
print("\nORDER DATE RANGE")
print("Earliest order date:", df["Order Date"].min())
print("Latest order date:", df["Order Date"].max())

print("\nSHIP DATE RANGE")
print("Earliest ship date:", df["Ship Date"].min())
print("Latest ship date:", df["Ship Date"].max())

print("\nRECORDS BY ORDER YEAR")
print(df["Order Date"].dt.year.value_counts().sort_index())

#CALCULATE SHIPPING DURATION
df["Shipping Days"] = (
    df["Ship Date"] - df["Order Date"]
).dt.days

print("\nSHIPPING DURATION SUMMARY")
print(df["Shipping Days"].describe())

print("\nAVERAGE SHIPPING DAYS BY SHIP MODE")
print(
    df.groupby("Ship Mode")["Shipping Days"]
    .mean()
    .sort_values()
    .round(2)
)

print("\nAVERAGE SHIPPING DAYS BY REGION")
print(
    df.groupby("Region")["Shipping Days"]
    .mean()
    .sort_values()
    .round(2)
)

#CALCULATE SHIPPING DURATION
text_columns = df.select_dtypes(include=["object","str"]).columns

print("\nBLANK TEXT VALUES BY COLUMN")

for column in text_columns:
    blank_count = df[column].astype(str).str.strip().eq("").sum()

    if blank_count > 0:
        print(f"{column}: {blank_count}")
        
print("Blank text check completed.")

# INSPECT POSTAL CODES
print("\nPOSTAL CODE DATA TYPE")
print(df["Postal Code"].dtype)

print("\nPOSTAL CODE SAMPLE")
print(df["Postal Code"].head(15).to_list())

print("\nUNIQUE POSTAL CODE COUNT")
print(df["Postal Code"].nunique())

print("\nPOSTAL CODE VALUE COUNTS — TOP 10")
print(df["Postal Code"].value_counts().head(10))

# CHECK POSTAL CODE CONSISTENCY

print("\nPOSTAL CODE VALUE TYPES")
print(df["Postal Code"].map(lambda value: type(value).__name__).value_counts())

print("\nPOSTAL CODE MISSING VALUES")
print(df["Postal Code"].isna().sum())

print("\nPOSTAL CODES WITH UNEXPECTED FORMATS")
postal_text = df["Postal Code"].astype(str).str.strip()

print(
    df.loc[
        ~postal_text.str.fullmatch(r"\d{5}"),
        ["Country/Region", "State/Province", "City", "Postal Code"]
    ].head(15)
)

# ANALYSE POSTAL CODE FORMATS

postal_text = df["Postal Code"].astype(str).str.strip()

print("\nCOUNTRY RECORD COUNTS")
print(df["Country/Region"].value_counts())

print("\nPOSTAL CODE LENGTHS BY COUNTRY")
postal_length = postal_text.str.len()

print(
    df.assign(Postal_Length=postal_length)
    .groupby(["Country/Region", "Postal_Length"])
    .size()
    .sort_index()
)

print("\nSHORT NUMERIC POSTAL CODES IN THE UNITED STATES")
us_mask = df["Country/Region"].eq("United States")
short_numeric_mask = postal_text.str.fullmatch(r"\d{1,4}")

print(
    df.loc[
        us_mask & short_numeric_mask,
        ["City", "State/Province", "Postal Code"]
    ].drop_duplicates().head(20)
)

# INVESTIGATE FOUR-DIGIT US ZIP CODES

postal_text = df["Postal Code"].astype(str).str.strip()

four_digit_mask = (
    df["Country/Region"].eq("United States")
    & postal_text.str.fullmatch(r"\d{4}")
)

four_digit_zip_rows = df.loc[four_digit_mask].copy()

print("\nFOUR-DIGIT ZIP CODE RECORD COUNT")
print(len(four_digit_zip_rows))

print("\nFOUR-DIGIT ZIP CODES BY STATE")
print(
    four_digit_zip_rows.groupby("State/Province")
    .size()
    .sort_values(ascending=False)
)

print("\nUNIQUE FOUR-DIGIT ZIP CODES BY STATE")
print(
    four_digit_zip_rows.groupby("State/Province")["Postal Code"]
    .nunique()
    .sort_values(ascending=False)
)

print("\nSAMPLE FOUR-DIGIT ZIP CODES")
print(
    four_digit_zip_rows[
        ["City", "State/Province", "Postal Code"]
    ].drop_duplicates().head(25).to_string(index=False)
)


# PREVIEW POSTAL CODE CORRECTIONS

postal_text = df["Postal Code"].astype(str).str.strip()

four_digit_us_mask = (
    df["Country/Region"].eq("United States")
    & postal_text.str.fullmatch(r"\d{4}")
)

preview = df.loc[
    four_digit_us_mask,
    ["City", "State/Province", "Postal Code"]
].head(10).copy()

preview["Corrected Postal Code"] = (
    preview["Postal Code"].astype(str).str.zfill(5)
)

print("\nPOSTAL CODE CORRECTION PREVIEW")
print(preview.to_string(index=False))

# CHECK CATEGORICAL CONSISTENCY

category_columns = [
    "Ship Mode",
    "Segment",
    "Country/Region",
    "Region",
    "Category",
    "Sub-Category"
]

print("\nCATEGORICAL CONSISTENCY CHECK")

for column in category_columns:
    values = df[column].dropna().astype(str)

    print(f"\n{column}")
    print("Unique values:", sorted(values.unique()))
    print("Leading/trailing spaces:", values.ne(values.str.strip()).sum())
    print("Blank strings:", values.str.strip().eq("").sum())

# INVESTIGATE SUSPECTED DUPLICATES

suspected_ids = [391, 392, 1699, 1700]

print("\nSUSPECTED DUPLICATE RECORDS")
print(
    df.loc[
        df["Row ID"].isin(suspected_ids)
    ].sort_values("Row ID").to_string(index=False)
)

print("\nDUPLICATE PAIRS — COMPARISON WITHOUT ROW ID")

comparison_columns = [
    column for column in df.columns
    if column != "Row ID"
    and column != "Shipping Days"
]

suspected_rows = df.loc[
    df["Row ID"].isin(suspected_ids)
].sort_values("Row ID")

print(
    suspected_rows[
        ["Row ID", "Order ID", "Product ID", "Sales", "Quantity", "Discount", "Profit"]
    ].to_string(index=False)
)

print(
    "\nNumber of records matching another record across all columns except Row ID:",
    df.drop(columns=["Row ID", "Shipping Days"], errors="ignore")
    .duplicated(keep=False).sum()
)

# INSPECT PROFIT EXTREMES

profit_columns = [
    "Row ID",
    "Order ID",
    "Category",
    "Sub-Category",
    "Product Name",
    "Sales",
    "Quantity",
    "Discount",
    "Profit"
]

print("\n10 LEAST PROFITABLE RECORDS")
print(
    df.nsmallest(10, "Profit")[profit_columns]
    .to_string(index=False)
)

print("\n10 MOST PROFITABLE RECORDS")
print(
    df.nlargest(10, "Profit")[profit_columns]
    .to_string(index=False)
)

# ANALYSE DISCOUNT AND PROFIT

print("\nPROFITABILITY BY DISCOUNT LEVEL")

discount_analysis = (
    df.groupby("Discount")
    .agg(
        Records=("Profit", "size"),
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Average_Profit=("Profit", "mean")
    )
    .round(2)
    .sort_index()
)

print(discount_analysis.to_string())

print("\nOVERALL PROFITABILITY")

print("Total sales:", round(df["Sales"].sum(), 2))
print("Total profit:", round(df["Profit"].sum(), 2))
print("Average profit per record:", round(df["Profit"].mean(), 2))

# PROFITABILITY BY CATEGORY

print("\nPROFITABILITY BY CATEGORY")

category_analysis = (
    df.groupby("Category")
    .agg(
        Records=("Profit", "size"),
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Average_Profit=("Profit", "mean")
    )
    .round(2)
    .sort_values("Total_Profit")
)

print(category_analysis.to_string())

# PROFITABILITY BY SUB-CATEGORY

print("\nPROFITABILITY BY SUB-CATEGORY")

subcategory_analysis = (
    df.groupby("Sub-Category")
    .agg(
        Records=("Profit", "size"),
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Average_Profit=("Profit", "mean")
    )
    .round(2)
    .sort_values("Total_Profit")
)

print(subcategory_analysis.to_string())

# TABLES PROFITABILITY BY DISCOUNT

print("\nTABLES PROFITABILITY BY DISCOUNT")

tables_df = df[df["Sub-Category"] == "Tables"]

tables_discount_analysis = (
    tables_df.groupby("Discount")
    .agg(
        Records=("Profit", "size"),
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Average_Profit=("Profit", "mean")
    )
    .round(2)
    .sort_index()
)

print(tables_discount_analysis.to_string())

# FINAL INITIAL-INSPECTION CHECK

print("\nFINAL INITIAL-INSPECTION CHECK")

print("Total records:", len(df))
print("Total columns:", len(df.columns))
print("Duplicate Row IDs:", df["Row ID"].duplicated().sum())
print("Missing values:", df.isnull().sum().sum())
print("Raw dataset path:", file_path)

print("\nInspection completed successfully.")






