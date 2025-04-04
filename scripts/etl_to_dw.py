import pandas as pd
import sqlite3
import pathlib

# Ensure the path is always correct based on the current script location
SCRIPT_DIR = pathlib.Path(__file__).parent  # Gets the directory where the script is located
DW_DIR = SCRIPT_DIR.parent.joinpath("data").joinpath("dw")  # Points to the existing 'dw' folder in 'data'
DB_PATH = DW_DIR.joinpath("smart_sales.db")
PREPARED_DATA_DIR = SCRIPT_DIR.parent.joinpath("data").joinpath("prepared")  # Points to the 'prepared' folder

def create_schema(cursor: sqlite3.Cursor) -> None:
    """Create tables in the data warehouse if they don't exist."""
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY,
            name TEXT,
            region TEXT,
            join_date DATE,
            loyalty_points INTEGER,
            preferred_contact_method TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY,
            product_name TEXT,
            category TEXT,
            unit_price REAL,
            year_added INTEGER,
            supplier TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            transaction_id INTEGER PRIMARY KEY,
            sale_date DATE,
            customer_id INTEGER,
            product_id INTEGER,
            store_id INTEGER,
            campaign_id INTEGER,
            sale_amount REAL,
            bonus_points INTEGER,
            payment_type TEXT,
            FOREIGN KEY (customer_id) REFERENCES customers (customer_id),
            FOREIGN KEY (product_id) REFERENCES products (product_id)
        )
    """)

def delete_existing_records(cursor: sqlite3.Cursor) -> None:
    """Clear existing records before inserting new ones."""
    cursor.execute("DELETE FROM customers")
    cursor.execute("DELETE FROM products")
    cursor.execute("DELETE FROM sales")

def insert_customers(customers_df: pd.DataFrame, cursor: sqlite3.Cursor) -> None:
    """Insert data into the customers table."""
    customers_df = customers_df[[
        "CustomerID", "Name", "Region", "JoinDate",
        "LoyaltyPoints", "PreferredContactMethod"
    ]]
    customers_df.columns = [
        "customer_id", "name", "region", "join_date",
        "loyalty_points", "preferred_contact_method"
    ]
    customers_df.to_sql("customers", cursor.connection, if_exists="append", index=False)

def insert_products(products_df: pd.DataFrame, cursor: sqlite3.Cursor) -> None:
    """Insert data into the products table."""
    products_df = products_df[[
        "ProductID", "ProductName", "Category", "UnitPrice", 
        "YearAdded", "Supplier"
    ]]
    products_df.columns = [
        "product_id", "product_name", "category", 
        "unit_price", "year_added", "supplier"
    ]
    products_df.to_sql("products", cursor.connection, if_exists="append", index=False)

def insert_sales(sales_df: pd.DataFrame, cursor: sqlite3.Cursor) -> None:
    """Insert data into the sales table."""
    sales_df = sales_df[[
        "TransactionID", "SaleDate", "CustomerID", "ProductID",
        "StoreID", "CampaignID", "SaleAmount", "BonusPoints", "PaymentType"
    ]]
    sales_df.columns = [
        "transaction_id", "sale_date", "customer_id", "product_id",
        "store_id", "campaign_id", "sale_amount", "bonus_points", "payment_type"
    ]
    sales_df.to_sql("sales", cursor.connection, if_exists="append", index=False)

def load_data_to_db() -> None:
    """Main ETL function to load prepared CSVs into the database."""
    try:
        DW_DIR.mkdir(parents=True, exist_ok=True)

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Create schema and clear existing records
        create_schema(cursor)
        delete_existing_records(cursor)

        # Load and insert prepared data
        customers_df = pd.read_csv(PREPARED_DATA_DIR.joinpath("customers_data_prepared.csv"))
        products_df = pd.read_csv(PREPARED_DATA_DIR.joinpath("products_data_prepared.csv"))
        sales_df = pd.read_csv(PREPARED_DATA_DIR.joinpath("sales_data_prepared.csv"))

        insert_customers(customers_df, cursor)
        insert_products(products_df, cursor)
        insert_sales(sales_df, cursor)

        conn.commit()
        print("Data successfully loaded into the smart_sales database.")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    load_data_to_db()
