def test_get_inventory(client):

    response = client.get("/inventory")

    assert response.status_code == 200

    assert response.json == []



def test_create_product(client):

    product = {
        "barcode": "123456789",
        "product_name": "Organic Milk",
        "brand": "Silk",
        "category": "Drink",
        "price": 5.99,
        "stock": 10,
        "ingredients": "Milk"
    }


    response = client.post(
        "/inventory",
        json=product
    )


    assert response.status_code == 201

    data = response.json

    assert data["product_name"] == "Organic Milk"




def test_update_product(client):

    product = {
        "barcode": "123",
        "product_name": "Milk",
        "brand": "Brand",
        "category": "Drink",
        "price": 5,
        "stock": 20,
        "ingredients": "Milk"
    }


    create = client.post(
        "/inventory",
        json=product
    )


    product_id = create.json["id"]


    response = client.patch(
        f"/inventory/{product_id}",
        json={
            "price": 8
        }
    )


    assert response.status_code == 200

    assert response.json["price"] == 8



def test_delete_product(client):

    product = {
        "barcode": "456",
        "product_name": "Juice",
        "brand": "Fresh",
        "category": "Drink",
        "price": 3,
        "stock": 15,
        "ingredients": "Fruit"
    }


    create = client.post(
        "/inventory",
        json=product
    )


    product_id = create.json["id"]


    response = client.delete(
        f"/inventory/{product_id}"
    )


    assert response.status_code == 200

    assert response.json["message"] == "Product deleted successfully"