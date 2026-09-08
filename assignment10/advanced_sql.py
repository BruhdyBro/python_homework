import sqlite3
import pandas as pd


try:
    with sqlite3.connect("../db/lesson.db") as conn:
        print("Database connected successfully.")

        cursor = conn.cursor()

        conn.execute("PRAGMA foreign_keys = 1")

# Task 1
        # Get total price of first five orders
        cursor.execute("""
        SELECT o.order_id, SUM(p.price * l.quantity) AS total_price
        FROM orders o
        JOIN line_items l
            ON o.order_id = l.order_id
        JOIN products p
            ON l.product_id = p.product_id
        GROUP BY o.order_id
        ORDER BY o.order_id
        LIMIT 5;
        """)

        # fetch and print the orders
        five_orders = cursor.fetchall()

        for order in five_orders:
            print(order)
        print()



# Task 2
        # Get average price of customer
        cursor.execute("""
        SELECT c.customer_name, AVG(order_totals.total_price) AS average_total_price
        FROM customers c
        LEFT JOIN (
            SELECT o.customer_id AS customer_id_b, o.order_id, SUM(p.price * l.quantity) AS total_price
            FROM orders o
            JOIN line_items l
                ON l.order_id = o.order_id
            JOIN products p
                ON p.product_id = l.product_id
            GROUP BY o.order_id
        ) AS order_totals
            ON c.customer_id = order_totals.customer_id_b
        GROUP BY c.customer_id;
        """)

        # fetch and print the average price of order per customer
        average_price = cursor.fetchall()

        for item in average_price:
            print(item)
        print()



# Task 3

        # Set the names for the transaction
        customer_name = "Perez and Sons"
        employee_name = ["Miranda", "Harris"]

        # Get the IDs and keys necessary for the INSERT

        cursor.execute("""
        SELECT customer_id FROM customers
            WHERE customer_name = ?
        """, (customer_name, ))

        customer_id = cursor.fetchall()[0][0]

        cursor.execute("""
        SELECT employee_id FROM employees
            WHERE first_name = ? AND last_name = ?
        """, (employee_name[0], employee_name[1]))

        employee_id = cursor.fetchall()[0][0]

        # Get the 5 least expensive products
        cursor.execute("""
        SELECT product_id FROM products
        ORDER BY price
        LIMIT 5
        """)

        products = cursor.fetchall()

        # Insert the order for the customer by the employee on current date
        cursor.execute("""
        INSERT INTO orders (customer_id, employee_id, date)
            VALUES (?,?, (SELECT date('now')))
            RETURNING order_id""", 
            (customer_id, employee_id))

        order_id = cursor.fetchall()[0][0]

        # For each of the 5 products, insert using their ID
        for product in products:
            cursor.execute("""
            INSERT INTO line_items (order_id, product_id, quantity)
                VALUES (?, ?, 10)
            """, (order_id, product[0]))

        # Commit transaction
        conn.commit()



# Task 4

        # Get first, last, and order count for employees with more than 5 orders

        cursor.execute("""
        SELECT e.first_name, e.last_name, COUNT(o.order_id) AS num_orders
        FROM employees e
        JOIN orders o
            ON e.employee_id = o.employee_id
        GROUP BY e.employee_id
        HAVING COUNT(o.order_id) > 5
        """)

        employees = cursor.fetchall()

        # print each returned employee
        for person in employees:
            print(person)
        print()
        
except Exception as e:
    print(f"Couldnt do it: {e}")

