from services.openfoodfacts import search_product_by_barcode


product = search_product_by_barcode("737628064502")

print(product)