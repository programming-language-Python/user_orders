from datetime import date

from pydantic import BaseModel


class UserQuerySchema(BaseModel):
    user_id: int
    user_name: str
    order_id: int
    order_date: date
    amount: float
    order_numbering: int
    sum_amount: float
