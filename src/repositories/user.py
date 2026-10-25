from datetime import date

from sqlalchemy import select, func, and_
from sqlalchemy.orm import aliased

from db.db import async_session_maker
from enums import StatusType
from models import User, Order
from schemas import UserQuerySchema


class UserRepository:
    model = User

    async def get(self) -> list[UserQuerySchema]:
        async with async_session_maker() as session:
            query = self._get_query_user_latest_order_by_date()
            res = await session.execute(query)
            return [
                UserQuerySchema(
                    user_id=r.user_id,
                    user_name=r.user_name,
                    order_id=r.order_id,
                    order_date=r.order_date,
                    amount=r.amount,
                    order_numbering=r.order_numbering,
                    sum_amount=r.sum_amount
                )
                for r in res.all()
            ]

    def _get_query_user_latest_order_by_date(self):
        u = aliased(self.model)
        sub_query_order = self._get_sub_query_order()
        return (
            select(
                u.user_id,
                u.user_name,
                sub_query_order.c.order_id,
                sub_query_order.c.order_date,
                sub_query_order.c.amount,
                sub_query_order.c.order_numbering,
                sub_query_order.c.sum_amount
            )
            .join(sub_query_order, sub_query_order.c.user_id == u.user_id)
            .filter(and_(
                u.city.ilike("%москва%"),
                u.reg_date >= date(2024, 1, 1),
                sub_query_order.c.last_order == 1
            ))
            .order_by(
                sub_query_order.c.amount.desc()
            )
        )

    def _get_sub_query_order(self):
        o = aliased(Order)
        return (
            select(
                o.user_id,
                o.order_id,
                o.order_date,
                o.amount,
                func.row_number().over(
                    partition_by=o.user_id,
                    order_by=(o.order_date.asc(), o.order_id.asc()),
                ).label("order_numbering"),
                func.row_number().over(
                    partition_by=o.user_id,
                    order_by=(o.order_date.desc(), o.order_id.desc()),
                ).label("last_order"),
                func.sum(o.amount)
                .over(partition_by=o.user_id)
                .label("sum_amount")
            )
            .filter(and_(
                o.is_test == False,
                o.status == StatusType.COMPLETED.name
            ))
            .subquery("sub_query_order")
        )
