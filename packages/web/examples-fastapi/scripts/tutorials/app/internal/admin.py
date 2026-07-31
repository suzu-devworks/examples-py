from typing import Any

from fastapi import APIRouter

router = APIRouter()


@router.post("/")
async def update_admin() -> Any:
    # spell-checker:disable-next-line
    return {"message": "Admin getting schwifty"}
