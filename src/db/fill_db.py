import sys
from datetime import date
from pathlib import Path

from sqlalchemy import select, delete

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import asyncio

from faker import Faker

from db.db import async_session_maker
from enums import StatusType
from models import User, Order

fake = Faker("ru_RU")

COUNT = 5_000


async def fill_db():
    async with async_session_maker() as session:
        await session.execute(delete(User))
        await session.execute(delete(Order))

        cities = [
            "Москва", "Санкт-Петербург", "Новосибирск", "Екатеринбург", "Казань",
            "Нижний Новгород", "Челябинск", "Самара", "Омск", "Ростов-на-Дону", "Уфа",
            "Красноярск", "Пермь", "Волгоград", "Воронеж", "Краснодар", "Саратов",
            "Тюмень", "Тольятти", "Ижевск", "Барнаул", "Ульяновск", "Иркутск",
            "Хабаровск", "Ярославль", "Владивосток", "Махачкала", "Томск", "Оренбург"
        ]

        users = [
            User(
                user_name=fake.user_name(),
                city=fake.random_element(cities),
                reg_date=fake.date_between_dates(
                    date_start=date(2022, 1, 1),
                    date_end=date(2026, 10, 10)
                )
            )
            for i in range(500)
        ]
        session.add_all(users)
        await session.flush()

        user_ids = (await session.scalars(select(User.user_id))).all()

        orders = [
            Order(
                order_date=fake.date_between_dates(
                    date_start=date(2025, 1, 1),
                    date_end=date(2026, 10, 10)
                ),
                amount=fake.pyfloat(positive=True, left_digits=6, right_digits=2),
                status=fake.enum(StatusType).name,
                is_test=fake.pybool(),
                user_id=fake.random_element(user_ids),
            )
            for i in range(COUNT)
        ]
        session.add_all(orders)
        await session.commit()


if __name__ == "__main__":
    asyncio.run(fill_db())
