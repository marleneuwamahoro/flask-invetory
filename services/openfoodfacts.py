import requests


BASE_URL = "https://world.openfoodfacts.org"


def search_product_by_barcode(barcode):
    """
    Search product information using barcode
    """

    url = f"{BASE_URL}/api/v0/product/{barcode}.json"

    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()

    if data.get("status") != 1:
        return None

    product = data.get("product", {})

    return {
        "barcode": barcode,
        "product_name": product.get("product_name"),
        "brand": product.get("brands"),
        "category": product.get("categories"),
        "ingredients": product.get("ingredients_text")
    }



def search_product_by_name(name):
    """
    Search product information using product name
    """

    url = f"{BASE_URL}/cgi/search.pl"

    params = {
        "search_terms": name,
        "search_simple": 1,
        "action": "process",
        "json": 1
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return None

    data = response.json()

    products = data.get("products")

    if not products:
        return None

    product = products[0]

    return {
        "barcode": product.get("code"),
        "product_name": product.get("product_name"),
        "brand": product.get("brands"),
        "category": product.get("categories"),
        "ingredients": product.get("ingredients_text")
    }