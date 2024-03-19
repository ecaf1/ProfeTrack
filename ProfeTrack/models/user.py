from typing import List, Optional, get_args

from flask_login import UserMixin
from sqlalchemy.orm import  Mapped, mapped_column
from passlib import hash
from ProfeTrack.models.base import Base
from ProfeTrack.models.enum import type_user
from ProfeTrack.service.database import db

class User(Base, UserMixin):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(
        db.String(50),
    )
    password: Mapped[str] = mapped_column(
        db.String(50),
    )
    type: Mapped[type_user] = mapped_column(db.Enum(*get_args(type_user)))
    email: Mapped[str] = mapped_column(db.String(50), unique=True)

    def __init__(self, username: str, password: str, type: type_user, email: str):

        self.username = username
        self.password = password
        self.type = type
        self.email = email

    def __repr__(self):
        return f"<User {self.username}>"

    def verify_password(self, password):
        return (password == self.password)
    
    def create_user(self, username: str, password: str, type: type_user, email: str):
        self.username = username
        self.password = password
        self.type = type
        self.email = email
        db.session.add(self)
        db.session.commit()