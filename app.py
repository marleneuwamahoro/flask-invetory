from flask import Flask, jsonify, request
from flask_migrate import Migrate

from config import Config
from models import db, Inventory
from schemas import InventorySchema

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

migrate = Migrate(app, db)

inventory_schema = InventorySchema()
inventories_schema = InventorySchema(many=True)

@app.route("/inventory", methods=["GET"])
def get_inventory():

    items = Inventory.query.all()

    return jsonify(inventories_schema.dump(items)), 200

@app.route("/inventory/<int:id>", methods=["GET"])
def get_item(id):

    item = Inventory.query.get(id)

    if not item:
        return jsonify({"message": "Product not found"}), 404

    return jsonify(inventory_schema.dump(item)), 200


@app.route("/inventory", methods=["POST"])
def add_product():

    data = request.get_json()

    item = Inventory(
        barcode=data["barcode"],
        product_name=data["product_name"],
        brand=data["brand"],
        category=data["category"],
        price=data["price"],
        stock=data["stock"],
        ingredients=data["ingredients"]
    )

    db.session.add(item)
    db.session.commit()

    return jsonify(inventory_schema.dump(item)), 201

@app.route("/inventory/<int:id>", methods=["PATCH"])
def update_product(id):

    item = Inventory.query.get(id)

    if not item:
        return jsonify({"message": "Product not found"}), 404

    data = request.get_json()

    for key, value in data.items():
        setattr(item, key, value)

    db.session.commit()

    return jsonify(inventory_schema.dump(item)), 200

@app.route("/inventory/<int:id>", methods=["DELETE"])
def delete_product(id):

    item = Inventory.query.get(id)

    if not item:
        return jsonify({"message": "Product not found"}), 404

    db.session.delete(item)
    db.session.commit()

    return jsonify({
        "message": "Product deleted successfully"
    }), 200

if __name__ == "__main__":
    app.run(debug=True)