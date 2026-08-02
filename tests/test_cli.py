from unittest.mock import patch, Mock

import cli


def test_view_inventory():

    mock_response = Mock()

    mock_response.json.return_value = [
        {
            "id": 1,
            "product_name": "Organic Milk",
            "brand": "Silk",
            "price": 5.99,
            "stock": 10
        }
    ]


    with patch("cli.requests.get", return_value=mock_response):

        cli.view_inventory()



def test_add_product():

    mock_response = Mock()

    mock_response.status_code = 201

    mock_response.json.return_value = {
        "id": 1,
        "product_name": "Milk"
    }


    with patch("cli.requests.post", return_value=mock_response):

        with patch(
            "builtins.input",
            side_effect=[
                "123456",
                "Milk",
                "Silk",
                "Drink",
                "5.99",
                "10",
                "Water"
            ]
        ):

            cli.add_product()



def test_delete_product():

    mock_response = Mock()

    mock_response.json.return_value = {
        "message": "Product deleted successfully"
    }


    with patch(
        "cli.requests.delete",
        return_value=mock_response
    ):

        with patch(
            "builtins.input",
            return_value="1"
        ):

            cli.delete_product()