from typing import Annotated

from fastapi import APIRouter, Depends

from services import UserService
from .dependencies import user_service

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get("")
async def get_users(
        user_service: Annotated[UserService, Depends(user_service)],
):
    users = await user_service.get()
    return users
