# Retail Profitability Intelligence System

## Project Overview

The Retail Profitability Intelligence System is a data analysis project that examines retail sales, profit, discounts, product categories, regional performance, and monthly trends.

The goal is to identify business patterns and areas that may require further investigation using Python and data analysis techniques.

## Objectives

* Analyze overall sales and profitability.
* Compare performance across product categories and sub-categories.
* Examine regional sales and profit.
* Investigate the relationship between discounts and profitability.
* Analyze monthly sales and profit trends.
* Prepare structured datasets for visualization in Power BI.

## Tools and Technologies

* Python
* Pandas
* Matplotlib
* Excel
* CSV data processing
* Power BI (planned)

## Dataset

The project uses the Sample Superstore dataset.

The dataset contains approximately 10,000 retail transaction records with information about orders, customers, products, sales, discounts, profit, and shipping.

## Key Findings

* Total sales: $2,326,534.35
* Total profit: $292,296.81
* Overall profit margin: 12.56%
* Technology generated the highest total profit among the three product categories.
* Tables, Bookcases, and Supplies recorded negative total profit.
* The West region recorded the highest total profit.
* Discount levels of 30% and above were associated with negative total profit in this dataset.
* Monthly analysis revealed variations in sales and profit, including some loss-making months.

## Data Preparation

* Inspected missing values and duplicate identifiers.
* Checked date and numerical consistency.
* Standardized postal-code formatting for four-digit US ZIP codes.
* Preserved the original raw dataset.
* Exported cleaned data and analysis tables as CSV files.

## Project Structure

Retail_Profitability_Intelligence/
├── data/
│   ├── raw/
│   └── processed/
├── python/
├── reports/
├── analysis/
└── README.md


## Business Value

The analysis highlights products, regions, discount levels, and time periods that deserve further investigation.

These findings can help guide more detailed analysis of product profitability, discount policies, and regional performance. The observed relationships are descriptive and do not independently establish causation.

## Future Improvements

* Build an interactive Power BI dashboard.
* Analyze product-level profitability.
* Investigate loss-making transactions.
* Add year-over-year performance comparisons.
* Develop recommendations supported by deeper transaction-level analysis.

