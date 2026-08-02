from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from datetime import datetime

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)


class Inventory(db.Model):
    __tablename__ = "inventory"

    id = db.Column(db.Integer, primary_key=True)

    barcode = db.Column(db.String(50), unique=True, nullable=False)

    product_name = db.Column(db.String(150), nullable=False)

    brand = db.Column(db.String(100))

    category = db.Column(db.String(100))

    price = db.Column(db.Float, nullable=False)

    stock = db.Column(db.Integer, nullable=False)

    ingredients = db.Column(db.Text)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Inventory {self.product_name}>"