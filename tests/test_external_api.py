from unittest.mock import patch, Mock

from services.openfoodfacts import search_product_by_barcode


def test_search_product_by_barcode():

    mock_response = {
        "status": 1,
        "product": {
            "product_name": "Organic Almond Milk",
            "brands": "Silk",
            "categories": "Beverages",
            "ingredients_text": "Water, almonds"
        }
    }


    with patch("services.openfoodfacts.requests.get") as mock_get:

        mock_get.return_value.status_code = 200

        mock_get.return_value.json.return_value = mock_response


        product = search_product_by_barcode(
            "123456789"
        )


        assert product["product_name"] == "Organic Almond Milk"

        assert product["brand"] == "Silk"

        assert product["category"] == "Beverages"