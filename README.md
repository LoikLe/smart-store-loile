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

