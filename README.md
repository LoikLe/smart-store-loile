# smart-sales-starter-files

Starter files to initialize the smart sales project.

-----

## Project Setup Guide (1-Mac/Linux)

Run all commands from a terminal in the root project folder. 

### Step 1A - Create a Local Project Virtual Environment

```shell
python3 -m venv .venv
```

### Step 1B - Activate the Virtual Environment

```shell
source .venv/bin/activate
```

### Step 1C - Install Packages

```shell
python3 -m pip install --upgrade -r requirements.txt
```

### Step 1D - Optional: Verify .venv Setup

```shell
python3 -m datafun_venv_checker.venv_checker
```

### Step 1E - Run the initial project script

```shell
python3 scripts/data_prep.py
```

-----

## Project Setup Guide (2-Windows)

Run all commands from a PowerShell terminal in the root project folder.

### Step 2 - Git Pull Before Changes

```shell
git pull origin main
```

### Step 2A - Create a Local Project Virtual Environment

```shell
py -m venv .venv
```

### Step 2B - Activate the Virtual Environment

```shell
.venv\Scripts\activate
```

### Step 2C - Install Packages

```shell
py -m pip install --upgrade -r requirements.txt
```

### Step 2D - Optional: Verify .venv Setup

```shell
py -m datafun_venv_checker.venv_checker
```

### Step 2E - Run the initial project script

```shell
py scripts/data_prep.py
```
## Git Commands Used for Module 2
Below are the Git commands I used to initialize my project, track changes, and push updates to GitHub.

```sh
# Initialize a new Git repository (only needed once)  
git init  

# Add all files to Git tracking  
git add .  

# Commit the changes with a meaningful message  
git commit -m "add starter files"  

# Push changes to GitHub on the main branch  
git push -u origin main  

# After making additional changes on README, use these commands:  
git add .  
git commit -m "Update README with commands"  
git push  
```
-----

## Data Cleaning & Prepare for ETL (P3)

In this module, we focus on cleaning and preparing the data for analysis.

### Step 3a - Create Folders
1. data
   - raw
   - prepared
2. scripts
3. utils

### Step 3b - Download Data Files
Find raw data .csv files in course repo and download to data/raw folder
- customers_data.csv
- products_data.csv
- sales_data.csv

### Step 3c - Create logger.py and data_prep.py

1. Create `logger.py` file under utils folder
2. Find `logger.py` file in course repo and copy/paste contents into local `logger.py`
3. Create `data_prep.py` file under scripts folder
4. Find `data_prep.py` file under `smart-sales-starter-files` repo and copy/paste nto local `data_prep.py`
5. Execute Python script:
```
py scripts\data_prep.py
```
### Step 3d - Run Data Scrubber Tests
Before running the main data preparation script, execute the following test script to ensure the data_scrubber.py is working properly:

```shell
py tests\test_data_scrubber.py
```
### Step 3e - Final Data Preparation
After confirming that the data_scrubber.py is working as expected, run the main data preparation script:

```shell
py scripts/data_prep.py
```
-----

## Data Warehouse (P4)

This module stores cleaned sales, product, and customer data in a SQLite database (smart_sales.db). Data is extracted, transformed, and loaded (ETL) from pre-processed CSV files into three main tables: customer, product, and sale, for direct querying or integration with business intelligence tools.

### Running the ETL Script

To create the database, tables, and insert data from the cleaned CSV files, run the following command:

```shell
py scripts\etl_to_dw.py
```

## Database Schema

### `sale` Table

| Column Name     | Data Type | Description                                |
|-----------------|-----------|--------------------------------------------|
| transaction_id | INTEGER   | Primary key                                |
| sale_date      | DATE      | Sale date                                 |
| customer_id    | INTEGER   | Foreign key referencing `customer` table   |
| product_id     | INTEGER   | Foreign key referencing `product` table    |
| store_id       | INTEGER   | Foreign key referencing `store` table      |
| campaign_id    | INTEGER   | Foreign key referencing `campaign` table   |
| sale_amount    | REAL      | Total amount of sale                       |
| bonus_points   | INTEGER   | Bonus points earned                        |
| payment_type   | TEXT      | Type of payment                            |

---

### `customer` Table

| Column Name         | Data Type | Description                                   |
|--------------------|-----------|-----------------------------------------------|
| customer_id        | INTEGER   | Primary key                                   |
| name               | TEXT      | Customer's name                               |
| region             | TEXT      | Region where customer resides                  |
| join_date          | DATE      | Customer's join date                           |
| loyalty_points     | INTEGER   | Loyalty points customer earned                 |
| preferred_contact  | TEXT      | Preferred contact method for customer          |

---

### `product` Table

| Column Name      | Data Type | Description                                 |
|------------------|-----------|---------------------------------------------|
| product_id      | INTEGER   | Primary key                                 |
| product_name    | TEXT      | Name of the product                          |
| category        | TEXT      | Category of the product                      |
| unit_price      | REAL      | Price per unit of the product                |
| year_added      | INTEGER   | Year the product was added                   |
| supplier        | TEXT      | Name of the supplier                          |

---

## Table Previews

### Customer Table
![customer_table_screenshot](https://github.com/user-attachments/assets/821f2f10-1954-49d9-b80b-586ff821f441)
eenshot.png)

### Product Table
![product_table_screenshot](https://github.com/user-attachments/assets/c8f747f0-60ba-4fb3-8e5b-3d99b5624401)


### Sale Table
![sale_table_screenshot](https://github.com/user-attachments/assets/8878059b-9c4f-47a4-a033-772cb25b9e34)


## Loading Data into the Data Warehouse
1. Prepared data files are loaded into the SQLite database using `etl_to_dw.py`:
   ```sh
   python scripts/etl_to_dw.py
   
## Initial Package List

- pip
- loguru
- ipykernel
- jupyterlab
- numpy
- pandas
- matplotlib
- seaborn
- plotly
- pyspark==4.0.0.dev1
- pyspark[sql]
- git+https://github.com/denisecase/datafun-venv-checker.git#egg=datafun_venv_checker

