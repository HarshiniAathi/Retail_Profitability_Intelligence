from pathlib import Path
import pandas as pd

# LOAD THE CLEANED DATASET
project_folder = Path(__file__).resolve().parent.parent

file_path = (
project_folder
/ "data"
/ "processed"
/ "cleaned_superstore.csv"
)

df = pd.read_csv(file_path)

# CALCULATE OVERALL BUSINESS METRICS
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()

total_orders = df["Order ID"].nunique()
total_customers = df["Customer ID"].nunique()

average_order_value = total_sales / total_orders
profit_margin = (total_profit / total_sales) * 100

# DISPLAY THE RESULTS
print("=" * 50)
print("RETAIL PROFITABILITY INTELLIGENCE SYSTEM")
print("=" * 50)

print(f"Total Sales:          ${total_sales:,.2f}")
print(f"Total Profit:         ${total_profit:,.2f}")
print(f"Unique Orders:         {total_orders:,}")
print(f"Unique Customers:      {total_customers:,}")
print(f"Average Sales/Order:  ${average_order_value:,.2f}")
print(f"Overall Profit Margin: {profit_margin:.2f}%")

print("=" * 50)

# ANALYZE PROFITABILITY BY CATEGORY

category_analysis = (
df.groupby("Category")
.agg(
Total_Sales=("Sales", "sum"),
Total_Profit=("Profit", "sum"),
Average_Profit=("Profit", "mean"),
Total_Quantity=("Quantity", "sum")
)
.reset_index()
)

# Calculate profit margin for each category

category_analysis["Profit_Margin_Percent"] = (
category_analysis["Total_Profit"]
/ category_analysis["Total_Sales"]
* 100
)

# Sort categories by total profit, highest first
category_analysis = category_analysis.sort_values(
by="Total_Profit",
ascending=False
)

print("\n" + "=" * 70)
print("PROFITABILITY BY PRODUCT CATEGORY")
print("=" * 70)
print(category_analysis.round(2).to_string(index=False))

# ANALYZE PROFITABILITY BY SUB-CATEGORY
subcategory_analysis = (
df.groupby("Sub-Category")
.agg(
Total_Sales=("Sales", "sum"),
Total_Profit=("Profit", "sum"),
Average_Profit=("Profit", "mean"),
Total_Quantity=("Quantity", "sum")
)
.reset_index()
)

# Calculate profit margin
subcategory_analysis["Profit_Margin_Percent"] = (
subcategory_analysis["Total_Profit"]
/ subcategory_analysis["Total_Sales"]
* 100
)

# Sort by total profit, lowest first
subcategory_analysis = subcategory_analysis.sort_values(
by="Total_Profit",
ascending=True
)

print("\n" + "=" * 90)
print("PROFITABILITY BY SUB-CATEGORY (LOWEST PROFIT FIRST)")
print("=" * 90)
print(subcategory_analysis.round(2).to_string(index=False))

# ANALYZE PROFITABILITY BY REGION
region_analysis = (
df.groupby("Region")
.agg(
Total_Sales=("Sales", "sum"),
Total_Profit=("Profit", "sum"),
Unique_Orders=("Order ID", "nunique"),
Total_Quantity=("Quantity", "sum")
)
.reset_index()
)

# Calculate profit margin
region_analysis["Profit_Margin_Percent"] = (
region_analysis["Total_Profit"]
/ region_analysis["Total_Sales"]
* 100
)

# Sort regions by total profit, highest first
region_analysis = region_analysis.sort_values(
by="Total_Profit",
ascending=False
)

print("\n" + "=" * 85)
print("PROFITABILITY BY REGION")
print("=" * 85)
print(region_analysis.round(2).to_string(index=False))

# ANALYZE PROFITABILITY BY DISCOUNT
discount_analysis = (
df.groupby("Discount")
.agg(
Total_Sales=("Sales", "sum"),
Total_Profit=("Profit", "sum"),
Average_Profit=("Profit", "mean"),
Record_Count=("Profit", "count")
)
.reset_index()
)

# Calculate profit margin
discount_analysis["Profit_Margin_Percent"] = (
discount_analysis["Total_Profit"]
/ discount_analysis["Total_Sales"]
* 100
)

# Sort discounts from lowest to highest
discount_analysis = discount_analysis.sort_values(
by="Discount"
)

print("\n" + "=" * 100)
print("DISCOUNT VS PROFITABILITY ANALYSIS")
print("=" * 100)
print(discount_analysis.round(2).to_string(index=False))

# MONTHLY SALES AND PROFIT ANALYSIS

df["Order Date"] = pd.to_datetime(df["Order Date"])

df["Order Month"] = df["Order Date"].dt.to_period("M").astype(str)

monthly_analysis = (
    df.groupby("Order Month")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Total_Quantity=("Quantity", "sum")
    )
    .reset_index()
)

monthly_analysis = monthly_analysis.sort_values(by="Order Month")

print("\n" + "=" * 100)
print("MONTHLY SALES AND PROFIT ANALYSIS")
print("=" * 100)
print(monthly_analysis.round(2).to_string(index=False))

# VISUALIZE MONTHLY SALES TREND
import matplotlib.pyplot as plt
plt.figure(figsize=(14, 6))
plt.plot(
    monthly_analysis["Order Month"],
    monthly_analysis["Total_Sales"],
    marker="o"
)
plt.title("Monthly Sales Trend")
plt.xlabel("Order Month")
plt.ylabel("Total Sales ($)")
plt.xticks(rotation=90)
plt.grid(True)
plt.tight_layout()
plt.show()

# VISUALIZE MONTHLY PROFIT TREND
plt.figure(figsize=(14, 6))
plt.plot(
    monthly_analysis["Order Month"],
    monthly_analysis["Total_Profit"],
    marker="o"
)
plt.axhline(y=0, linestyle="--")
plt.title("Monthly Profit Trend")
plt.xlabel("Order Month")
plt.ylabel("Total Profit ($)")
plt.xticks(rotation=90)
plt.grid(True)
plt.tight_layout()
plt.show()

# CATEGORY-WISE PROFIT VISUALIZATION
plt.figure(figsize=(9, 5))
plt.bar(
    category_analysis["Category"],
    category_analysis["Total_Profit"]
)
plt.title("Total Profit by Product Category")
plt.xlabel("Category")
plt.ylabel("Total Profit ($)")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()

# SUB-CATEGORY PROFITABILITY VISUALIZATION
subcategory_chart = subcategory_analysis.sort_values(
    by="Total_Profit",
    ascending=True
)
plt.figure(figsize=(12, 8))
plt.barh(
    subcategory_chart["Sub-Category"],
    subcategory_chart["Total_Profit"]
)
plt.axvline(x=0, linestyle="--")
plt.title("Profitability by Product Sub-Category")
plt.xlabel("Total Profit ($)")
plt.ylabel("Sub-Category")
plt.grid(axis="x", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()

# EXPORT ANALYSIS TABLES
analysis_folder = project_folder / "analysis"
analysis_folder.mkdir(parents=True, exist_ok=True)
analysis_tables = {
    "category_analysis.csv": category_analysis,
    "subcategory_analysis.csv": subcategory_analysis,
    "region_analysis.csv": region_analysis,
    "discount_analysis.csv": discount_analysis,
    "monthly_analysis.csv": monthly_analysis
}
for filename, table in analysis_tables.items():
    output_path = analysis_folder / filename
    table.to_csv(output_path, index=False)
    print(f"Exported: {output_path.name}")
print("\nAll analysis tables exported successfully!")


