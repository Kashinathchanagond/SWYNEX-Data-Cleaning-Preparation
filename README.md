# SWYNEX - Task 1: Data Cleaning & Preparation

## Overview
This repository contains the completed Task 1 for the internship at SWYNEX Technologies. The objective was to audit, clean, and standardize a public raw dataset using Python (Pandas & NumPy).

## Dataset Details
* **Source:** Titanic Passenger Dataset
* **Raw Size:** 891 rows × 12 columns

## Key Cleaning Steps
1. **Duplicate Removal:** Checked and dropped duplicate records.
2. **Missing Values Imputation:**
   - Imputed missing values in `age` using class median (`pclass`).
   - Filled missing `embarked` values using mode.
   - Dropped the `cabin` column due to high null sparsity (>75%).
3. **Data Type Correction:** Converted categorical attributes (`pclass`, `sex`, `embarked`) to category data type.
4. **Standardization:** Lowercased column headers and cleaned string columns.

## Repository Contents
- `data_cleaning.py`: Python script used for cleaning
- `titanic_raw.csv`: Original uncleaned dataset
- `titanic_cleaned.csv`: Processed dataset ready for analysis
-
---

# Task 2: Exploratory Data Analysis (EDA)

## Project Overview
Performed exploratory data analysis on the cleaned Titanic dataset to discover statistical distributions, key demographic factors influencing survival, and outlier patterns.

## Summary Statistics
- Total Passengers: 891
- Overall Survival Rate: ~38.38%
- Average Passenger Age: ~29.06 years
- Average Ticket Fare: $32.20

## 5 Key Useful Insights
1. **Gender Survival Disparity:** Female passengers had an overwhelmingly higher survival rate (~74%) compared to male passengers (~19%), adhering strictly to the maritime evacuation priority.
2. **Socio-Economic Class Impact:** Passenger class was a decisive factor—1st Class passengers experienced a >62% survival rate, while 3rd Class passengers saw only ~24% survival.
3. **Age Vulnerability:** Children under 10 years experienced higher survival likelihoods, whereas the highest absolute casualties were concentrated among working-age adults (20–35 years).
4. **Ticket Fare Outliers:** The fare distribution is heavily right-skewed; IQR analysis detected 116 statistical outliers with extreme luxury prices above $500.
5. **Correlation Drivers:** A positive correlation (+0.26) between ticket fare and survival confirms economic status as a primary survival determinant.
6.
