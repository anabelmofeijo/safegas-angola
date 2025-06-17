from app import router


@router.get("/")
async def running():
    return {"message":"Reading is running"}