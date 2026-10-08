from scripts.extract import get_data, PRODUCT_API, USER_API
from scripts.transform import transform_products, transform_customers
from scripts.load import load_products, load_customers


def main():

    print("Starting ETL pipeline...")

    # Extract
    products = get_data(PRODUCT_API)
    users = get_data(USER_API)

    print(f"Extracted {len(products)} products")
    print(f"Extracted {len(users)} customers")

    # Transform
    transformed_products = transform_products(products)
    transformed_customers = transform_customers(users)

    print("Data transformation completed")

    # Load
    load_products(transformed_products)
    load_customers(transformed_customers)

    print("ETL pipeline completed successfully")


if __name__ == "__main__":
    main()