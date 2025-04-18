import pandas as pd
import sqlite3
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger(__name__)

# Constants
DB_FILE = "data/dw/smart_sales.db"  # Path to your SQLite database
RESULTS_OUTPUT_DIR = "data/results"  # Folder to save results

# Create output directory if it doesn't exist
os.makedirs(RESULTS_OUTPUT_DIR, exist_ok=True)

def list_tables(db_file):
    """
    List all the tables in the SQLite database.
    
    Parameters:
        db_file (str): Path to the SQLite database.
    """
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # Query to get all table names
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        # Log the table names
        logger.info("Tables in the database:")
        for table in tables:
            logger.info(f"Table: {table[0]}")

        conn.close()

    except sqlite3.Error as e:
        logger.error(f"Error listing tables: {e}")

def load_data_from_db(db_file):
    """
    Load data from the SQLite database for customers, products, and sales.
    
    Parameters:
        db_file (str): Path to the SQLite database.
    
    Returns:
        tuple: DataFrames for customers, products, and sales.
    """
    try:
        conn = sqlite3.connect(db_file)

        # Use correct table names based on your database
        customers_df = pd.read_sql_query("SELECT * FROM customers", conn)
        products_df = pd.read_sql_query("SELECT * FROM products", conn)
        sales_df = pd.read_sql_query("SELECT * FROM sales", conn)

        conn.close()

        return customers_df, products_df, sales_df

    except sqlite3.Error as e:
        logger.error(f"Error loading data from database: {e}")
        raise

def analyze_category_sales_by_region(sales_df, products_df, customers_df):
    """
    Analyze product category sales by region (including all categories).
    
    Returns:
        pd.DataFrame: DataFrame grouped by region and category.
    """
    try:
        # Merge data
        merged_df = sales_df.merge(products_df, on="product_id", how="left")
        merged_df = merged_df.merge(customers_df[['customer_id', 'region']], on="customer_id", how="left")
        merged_df['category'] = merged_df['category'].fillna('Unknown')

        # Group by region and category
        grouped = merged_df.groupby(["region", "category"]).agg(
            total_sales=("sale_amount", "sum")
        ).reset_index()

        logger.info(f"Grouped category sales by region:\n{grouped}")
        return grouped

    except Exception as e:
        logger.error(f"Error analyzing category sales: {e}")
        raise


def visualize_all_categories_by_region(grouped_data):
    """
    Visualize all category sales by region using a clustered bar plot.
    
    Parameters:
        grouped_data (pd.DataFrame): DataFrame with category sales by region.
    """
    try:
        import matplotlib.pyplot as plt
        import seaborn as sns

        sns.set_theme(style="whitegrid")
        plt.figure(figsize=(14, 8))

        # Create barplot with 'region' on x-axis, colored by category
        sns.barplot(
            data=grouped_data,
            x="region",
            y="total_sales",
            hue="category",
            palette="tab10",
            dodge=True
        )

        # Add this line to switch y-axis to logarithmic scale
        plt.yscale("log")

        plt.title("Product Category Sales by Region (Log Scale)")
        plt.xlabel("Region")
        plt.ylabel("Total Sales (Log Scale)")
        plt.legend(title="Product Category", bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()

        chart_path = os.path.join(RESULTS_OUTPUT_DIR, "category_sales_by_region.png")
        plt.savefig(chart_path)
        logger.info(f"Chart saved to {chart_path}")
        plt.show()

    except Exception as e:
        logger.error(f"Error visualizing category sales by region: {e}")
        raise



def main():
    logger.info("Starting top category by region analysis...")

    # Step 1: List all tables in the SQLite database (for debugging purposes)
    list_tables(DB_FILE)

    # Step 2: Load data from the database
    customers_df, products_df, sales_df = load_data_from_db(DB_FILE)

    # Step 3: Analyze and visualize all category sales by region
    grouped_data = analyze_category_sales_by_region(sales_df, products_df, customers_df)
    visualize_all_categories_by_region(grouped_data)


    logger.info("Analysis and visualization completed successfully.")

if __name__ == "__main__":
    main()
