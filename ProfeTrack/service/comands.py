from flask import Flask
from random import choices
from string import ascii_lowercase
from ProfeTrack.models.user import User
from ProfeTrack.service.database import db


def create_admin():

    password = "".join(choices(ascii_lowercase, k=10))

    admin = User(username="admin", password='1234', type="admin", email="admin@gmail.com")
    db.session.add(admin)
    db.session.commit()

    print("Admin User Created")
    print("-" * 15)
    print(f"Name: {admin.username}")
    print(f"Password: {'1234'}")

def init_app(app: Flask):
    @app.cli.command("createsu")
    def _():
        create_admin()