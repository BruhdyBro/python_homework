import sqlite3
import pandas as pd

# Task 5
try:
    with sqlite3.connect("../db/lesson.db") as conn:
        print("Database connected successfully.")

        # Break select statement into multiple lines for easier reading
        sql_statement = """
        SELECT l.line_item_id, l.quantity, p.product_id, p.product_name, p.price 
        FROM line_items l 
        JOIN products p 
            ON l.product_id = p.product_id;
        """

        # Turn results into pd dataframe
        df = pd.read_sql_query(sql_statement, conn)
        print(df.head(5))
        print()

        # set total as price time the quantity for each row
        df['total'] = df['quantity'] * df['price']
        print(df.head(5))
        print()

        # create new df instead of altering previous one
        new_df = df.groupby('product_id').agg({
            'line_item_id': 'count',
            'total': 'sum',
            'product_name': 'first'
        })
        print(new_df.head(5))
        print()

        # Sort values and export as CSV
        new_df = new_df.sort_values('product_name')
        new_df = new_df.reset_index()
        new_df.to_csv("order_summary.csv")
except:
    print("Couldnt do it")

