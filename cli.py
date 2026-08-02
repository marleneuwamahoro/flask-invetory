import requests


BASE_URL = "http://127.0.0.1:5000"


def view_inventory():

    response = requests.get(
        f"{BASE_URL}/inventory"
    )

    products = response.json()

    if not products:
        print("Inventory is empty")
        return

    for product in products:
        print("---------------------")
        print(f"ID: {product['id']}")
        print(f"Name: {product['product_name']}")
        print(f"Brand: {product['brand']}")
        print(f"Price: {product['price']}")
        print(f"Stock: {product['stock']}")



def add_product():

    print("\nAdd New Product")

    data = {
        "barcode": input("Barcode: "),
        "product_name": input("Product name: "),
        "brand": input("Brand: "),
        "category": input("Category: "),
        "price": float(input("Price: ")),
        "stock": int(input("Stock quantity: ")),
        "ingredients": input("Ingredients: ")
    }


    response = requests.post(
        f"{BASE_URL}/inventory",
        json=data
    )


    if response.status_code == 201:
        print("Product added successfully")
        print(response.json())

    else:
        print("Failed to add product")



def update_product():

    product_id = input("Product ID: ")

    price = input(
        "New price (leave empty to skip): "
    )

    stock = input(
        "New stock (leave empty to skip): "
    )


    data = {}


    if price:
        data["price"] = float(price)

    if stock:
        data["stock"] = int(stock)


    response = requests.patch(
        f"{BASE_URL}/inventory/{product_id}",
        json=data
    )


    print(response.json())



def delete_product():

    product_id = input(
        "Product ID to delete: "
    )


    response = requests.delete(
        f"{BASE_URL}/inventory/{product_id}"
    )


    print(response.json())



def search_product():

    choice = input(
        "Search by barcode or name? "
    )


    if choice == "barcode":

        barcode = input("Barcode: ")

        response = requests.get(
            f"{BASE_URL}/search",
            params={
                "barcode": barcode
            }
        )

    else:

        name = input("Product name: ")

        response = requests.get(
            f"{BASE_URL}/search",
            params={
                "name": name
            }
        )


    print(response.json())



def menu():

    while True:

        print("""
======== Inventory CLI ========

1. View inventory
2. Add product
3. Update product
4. Delete product
5. Search OpenFoodFacts
6. Exit

===============================
        """)


        choice = input(
            "Choose option: "
        )


        if choice == "1":
            view_inventory()

        elif choice == "2":
            add_product()

        elif choice == "3":
            update_product()

        elif choice == "4":
            delete_product()

        elif choice == "5":
            search_product()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option")



if __name__ == "__main__":
    menu()