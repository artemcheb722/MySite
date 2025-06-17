from fastapi import APIRouter, Body, UploadFile


products_router = APIRouter()

@products_router.post('/')
async def create_product(
    main_image: UploadFile,
    images: list[UploadFile],
    title: str = Body(max_length=100),
    description: str = Body(max_length=1000),
    price: float = Body(gt=1),
):
    pass