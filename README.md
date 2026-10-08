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
