from repositories import UserRepository
from services import UserService


def user_service() -> UserService:
    return UserService(UserRepository)
