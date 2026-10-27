# Retail Profitability Intelligence System

## Project Overview

The **Retail Profitability Intelligence System** is an end-to-end data analytics project that analyzes retail sales, profitability, discounts, product categories, regional performance, and monthly trends.

The project uses Python for data preparation and exploratory analysis, along with Power BI to create interactive dashboards that help identify business patterns and areas requiring further investigation.

## Project Objectives

* Analyze overall sales, profit, and profitability margins.
* Compare performance across product categories and subcategories.
* Evaluate sales and profitability across regions.
* Investigate the relationship between discounts and profitability.
* Analyze monthly sales and profit trends.
* Prepare structured analysis datasets for visualization.
* Present business insights through interactive Power BI dashboards.

## Tools and Technologies

* **Python** — data analysis and preparation
* **Pandas** — data manipulation and cleaning
* **Matplotlib** — data visualization
* **CSV** — structured data storage and analysis outputs
* **Microsoft Power BI** — interactive dashboard development
* **GitHub** — project documentation and version control

## Dataset

The project uses the Sample Superstore retail dataset, which contains approximately 10,000 transaction records covering orders, customers, products, sales, discounts, profits, and shipping information.

The dataset supports analysis of product performance, regional differences, discount patterns, and changes in business performance over time.

**Note:** The dataset is not included in this repository. Users must obtain an appropriate copy of the dataset separately before rerunning the Python scripts.

## Key Performance Indicators

| Metric                  |         Value |
| ----------------------- | ------------: |
| Total Sales             | $2,326,534.35 |
| Total Profit            |   $292,296.81 |
| Total Orders            |         5,111 |
| Unique Customers        |           804 |
| Average Sales per Order |       $455.20 |
| Overall Profit Margin   |        12.56% |

## Key Findings

* Technology recorded the highest profit margin among the three product categories.
* Furniture had a comparatively low profit margin of 2.61%.
* Tables, Bookcases, and Supplies recorded negative total profits.
* The West region recorded the highest profit margin at 14.98%.
* The Central region had the lowest profit margin at 7.92%.
* Several higher discount levels were associated with negative aggregate profitability.
* Monthly analysis revealed variations in sales and profit over time.

These findings are descriptive. The observed relationships do not independently establish causation.

## Data Preparation and Analysis

The Python workflow covers:

1. **Data Inspection:** Examining dataset structure, column types, and data quality.
2. **Data Cleaning:** Preparing the dataset for analysis and checking data consistency.
3. **Sales and Profit Analysis:** Calculating business metrics and generating category, subcategory, regional, discount, and monthly analysis tables.

The resulting CSV files support further exploration and Power BI visualization.

## Power BI Dashboard

The project includes three dashboard pages:

### 1. Executive Overview

Presents key performance indicators and a high-level summary of retail performance.

### 2. Profitability Analysis

Examines profitability across product categories, subcategories, regions, and discount levels.

### 3. Sales Trends

Explores changes in sales and profit over time.

The Power BI report is available as a `.pbix` file in this repository.

## Repository Structure

```text
Retail_Profitability_Intelligence/
├── analysis/
│   ├── category_analysis.csv
│   ├── subcategory_analysis.csv
│   ├── region_analysis.csv
│   ├── discount_analysis.csv
│   └── monthly_analysis.csv
├── python/
│   ├── 01_data_inspection.py
│   ├── 02_data_cleaning.py
│   └── 03_sales_profit_analysis.py
├── reports/
│   └── data_quality_notes.txt
├── screenshots/
│   ├── executive_overview.png
│   ├── profitability_analysis.png
│   └── sales_trends.png
├── Retail_Profitability_Intelligence.pbix
└── README.md
```

## Business Value

This project demonstrates how data analytics can help businesses identify profitable product categories, investigate loss-making subcategories, compare regional performance, and examine discount-related profitability patterns.

The insights can support further investigation into pricing, discount strategies, product performance, and regional business opportunities.

## Future Improvements

* Perform deeper transaction-level profitability analysis.
* Investigate loss-making orders and products.
* Add year-over-year comparisons.
* Develop additional business recommendations based on detailed analysis.
* Extend the project with predictive analytics and forecasting.

## Project Status

**Completed:** Python data analysis, analysis dataset generation, and the three-page Power BI dashboard.

**Potential extensions:** Deeper profitability analysis, forecasting, and additional business insights.

