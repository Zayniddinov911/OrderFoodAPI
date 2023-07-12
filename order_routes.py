from fastapi import APIRouter

order_router = APIRouter(
    prefix="/order",
    tags=['Orders']
)

@order_router.get('/')
async def hello():
    return {"message": "Hello this is order_router"}
