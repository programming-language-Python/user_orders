from sqlalchemy.orm import Mapped, relationship

from db.db import Base
from models.base import intpk, created_at


class User(Base):
    __tablename__ = "users"

    user_id: Mapped[intpk]
    user_name: Mapped[str]
    city: Mapped[str]
    reg_date: Mapped[created_at]

    orders: Mapped[list["Order"]] = relationship(
        back_populates="user"
    )
