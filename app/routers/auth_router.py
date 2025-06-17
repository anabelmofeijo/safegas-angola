from app import router


@router.get("/")
async def running():
    return {"message":"Auth is running"}