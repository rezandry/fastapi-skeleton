from fastapi import APIRouter
from ..responses import success

router = APIRouter()

@router.get('/')
async def get_profile():
    return success.response([{'name': 'Reza Andriyunanto', 'age': 25}])