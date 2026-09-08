import sqlite3

# Task 3 Functions

# Adds a publisher by using the connection cursor and publisher's name
def add_publisher(cursor, name):
    try:
        cursor.execute("INSERT INTO publishers (publisher_name) VALUES (?)", (name,))
    except sqlite3.IntegrityError:
        print(f"{name} is already a publisher in the database.")

# Adds a magazine using the connection cursor. magazine's name, and publisher's name
def add_magazine(cursor, name, publisher_name):
    try:
        cursor.execute("SELECT publisher_id FROM publishers WHERE publisher_name = ?", (publisher_name,))
        results = cursor.fetchall()
        if len(results) > 0:
            publisher_id = results[0][0]
        else:
            print(f"No publisher found with the name \"{publisher_name}\"")
            return
        cursor.execute("INSERT INTO magazines (magazine_name, publisher_id) VALUES (?, ?)", (name, publisher_id))
    except sqlite3.IntegrityError:
        print(f"{name} is already a magazine in the database.")

# Adds a subscriber using the connection cursor, subscriber's name, subscriber's address
def add_subscriber(cursor, name, address):
    try:
        cursor.execute("SELECT * FROM subscribers WHERE subscriber_name = ? AND subscriber_address = ?", (name, address))
        results = cursor.fetchall()
        if len(results) > 0:
            print(f"{name} with that address is already a subscriber in the database.")
            return
        cursor.execute("INSERT INTO subscribers (subscriber_name, subscriber_address) VALUES (?, ?)", (name, address))
    except sqlite3.IntegrityError:
        print(f"{name} with that address is already a subscriber in the database.")

# Adds a subscription using the connection cursor, subscriber's name, and magazine's name
def add_subscription(cursor, subscriber_name, magazine_name):
    try:
        # Get subscriber id from subscriber name
        cursor.execute("SELECT subscriber_id FROM subscribers WHERE subscriber_name = ?", (subscriber_name,))
        results = cursor.fetchall()
        if len(results) > 0:
            subscriber_id = results[0][0]
        else:
            print(f"No subscriber found with the name \"{subscriber_name}\"")
            return

        # Get magazine id from magazine name
        cursor.execute("SELECT magazine_id FROM magazines WHERE magazine_name = ?", (magazine_name,))
        results = cursor.fetchall()
        if len(results) > 0:
            magazine_id = results[0][0]
        else:
            print(f"No magazine found with the name \"{magazine_name}\"")
            return

        # Insert it all together
        cursor.execute("""
        INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) 
            VALUES (?, ?, ?)""", 
            (subscriber_id, magazine_id, "January 1st, 2027")
        )
    except sqlite3.IntegrityError:
        print(f"{subscriber_name} is already subscribed to {magazine_name} in the database.")




# Task 1
try:
    with sqlite3.connect("../db/magazines.db") as conn:
        print("Database created and connected successfully.")
        conn.execute("PRAGMA foreign_keys = 1")

        #
        # Task 2: Define Database Structure
        #
        cursor = conn.cursor()

        # Create tables
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS publishers (
            publisher_id INTEGER PRIMARY KEY,
            publisher_name TEXT NOT NULL UNIQUE
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS magazines (
            magazine_id INTEGER PRIMARY KEY,
            magazine_name TEXT NOT NULL UNIQUE,
            publisher_id INTEGER NOT NULL,
            FOREIGN KEY (publisher_id) REFERENCES publishers (publisher_id)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscribers (
            subscriber_id INTEGER PRIMARY KEY,
            subscriber_name TEXT NOT NULL,
            subscriber_address TEXT NOT NULL,
            UNIQUE(subscriber_name, subscriber_address)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions (
            subscription_id INTEGER PRIMARY KEY,
            subscriber_id INTEGER NOT NULL,
            magazine_id INTEGER NOT NULL,
            expiration_date TEXT NOT NULL,
            FOREIGN KEY (subscriber_id) REFERENCES subscribers (subscriber_id),
            FOREIGN KEY (magazine_id) REFERENCES magazines (magazine_id),
            UNIQUE(subscriber_id, magazine_id)
        )
        """)

        #
        # Task 3: Populate Tables with Data
        #
        add_publisher(cursor, "sports")
        add_publisher(cursor, "home")
        add_publisher(cursor, "food")
        
        add_magazine(cursor, "soccer", "sports")
        add_magazine(cursor, "football", "sports")
        add_magazine(cursor, "kitchen", "home")
        add_magazine(cursor, "garage", "home")
        add_magazine(cursor, "food", "meats and veggies")

        add_subscriber(cursor, "Bruhdy", "123 Playground Street")
        add_subscriber(cursor, "Betty", "456 Over There Lane")
        add_subscriber(cursor, "Jason", "789 Myhouse Boulevard")
        add_subscriber(cursor, "Jonesy", "123 Playground Street")

        add_subscription(cursor, "Bruhdy", "soccer")
        add_subscription(cursor, "Bruhdy", "kitchen")
        add_subscription(cursor, "Betty", "kitchen")
        add_subscription(cursor, "Betty", "garage")
        add_subscription(cursor, "Jason", "soccer")
        add_subscription(cursor, "Jason", "football")
        add_subscription(cursor, "Jonesy", "football")
        add_subscription(cursor, "Jonesy", "kitchen")
        
        conn.commit()

        #
        # Task 4: Write SQL Queries
        #

        # Get all subscribers
        cursor.execute("SELECT * FROM subscribers")
        all_subscribers = cursor.fetchall()

        # Get all magazines sorted by name
        cursor.execute("SELECT * FROM magazines ORDER BY magazine_name")
        all_magazines = cursor.fetchall()

        # Get all magazines by specific publisher. Can be "home" or "sports"
        publisher = "home" 
        cursor.execute("""
        SELECT p.publisher_name, m.magazine_name FROM publishers p
        JOIN magazines m 
            ON p.publisher_id = m.publisher_id
        WHERE p.publisher_name = ?;
        """,
        (publisher,))
        all_results = cursor.fetchall()

        print()

        print("-=-=-=- All Subscribers in Database -=-=-=-")
        for row in all_subscribers:
            print(row)
        print()

        print("-=-=-=- All magazines in Database Ordered by Name -=-=-=-")
        for row in all_magazines:
            print(row)
        print()

        print("-=-=-=- All Magazines in Database from Specific Publisher -=-=-=-")
        for row in all_results:
            print(row)
        print()

except:
    print("Couldnt do it")



