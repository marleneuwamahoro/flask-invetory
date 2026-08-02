import sys
import os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

import pytest

from app import app
from models import db


@pytest.fixture
def client():

    app.config["TESTING"] = True

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

    with app.test_client() as client:

        with app.app_context():

            db.create_all()

            yield client

            db.session.remove()

            db.drop_all()