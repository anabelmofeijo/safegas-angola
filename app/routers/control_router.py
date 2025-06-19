from app import  APIRouter
from app.services.control_service import ControlDatabase
from app.schemas.control_schema import ControlOnOff

router = APIRouter()

@router.get("/")
async def running():
    return {"message":"Control is running"}

@router.post("/signal/")
async def control_on(data: ControlOnOff):
    service = ControlDatabase()
    response = service.ControlAdd(data.dict())
    return response

@router.get("/list/")
async def control_list_all():
    service = ControlDatabase()
    response = service.ControlListAll()
    return response 