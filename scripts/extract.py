import requests

PRODUCT_API = "https://fakestoreapi.com/products"
USER_API = "https://fakestoreapi.com/users"


def get_data(url):
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    raise Exception(
        f"API request failed: {response.status_code}"
    )


products = get_data(PRODUCT_API)
users = get_data(USER_API)

print("Products received:", len(products))
print("Users received:", len(users))