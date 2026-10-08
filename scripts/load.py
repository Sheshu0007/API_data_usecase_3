import psycopg2


def get_connection():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        database="api_sales",
        user="postgres",
        password="1611"
    )


def load_products(products):
    conn = get_connection()
    cursor = conn.cursor()

    for product in products:
        cursor.execute("""
            INSERT INTO products
            (product_id, product_name, category, price)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (product_id) DO NOTHING;
        """, (
            product["product_id"],
            product["product_name"],
            product["category"],
            product["price"]
        ))

    conn.commit()

    cursor.close()
    conn.close()

    print("Products loaded successfully")


def load_customers(customers):
    conn = get_connection()
    cursor = conn.cursor()

    for customer in customers:
        cursor.execute("""
            INSERT INTO customers
            (customer_id, customer_name, email, city)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (customer_id) DO NOTHING;
        """, (
            customer["customer_id"],
            customer["customer_name"],
            customer["email"],
            customer["city"]
        ))

    conn.commit()

    cursor.close()
    conn.close()

    print("Customers loaded successfully")