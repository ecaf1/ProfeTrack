from sqlalchemy.orm import Mapped, mapped_column
from ProfeTrack.service.database import db

class Base(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
