from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.db import Base
from models.base import intpk, created_at

from src.enums import StatusType


class Order(Base):
    __tablename__ = "orders"

    order_id: Mapped[intpk]
    order_date: Mapped[created_at]
    amount: Mapped[float]
    status: Mapped[StatusType]
    is_test: Mapped[bool]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id", ondelete="CASCADE"))

    user: Mapped["User"] = relationship(
        back_populates="orders"
    )
