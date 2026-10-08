def transform_products(products):
    transformed_products = []

    for product in products:
        transformed_products.append({
            "product_id": product["id"],
            "product_name": product["title"],
            "category": product["category"],
            "price": product["price"]
        })

    return transformed_products


def transform_customers(users):
    transformed_customers = []

    for user in users:
        transformed_customers.append({
            "customer_id": user["id"],
            "customer_name": (
                user["name"]["firstname"]
                + " "
                + user["name"]["lastname"]
            ),
            "email": user["email"],
            "city": user["address"]["city"]
        })

    return transformed_customers