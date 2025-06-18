from app import  APIRouter
from app.services.control_service import ControlDatabase
from app.schemas.control_schema import (
    ControlOff,
    ControlOn
)

control = APIRouter()

@control.get("/")
async def running():
    return {"message":"Control is running"}

@control.post("/on/")
async def control_on(data: ControlOn):
    service = ControlDatabase()
    response = service.ControlAdd(data)
    return response

@control.post("/off/")
async def control_off(data: ControlOff):
    service = ControlDatabase()
    response = service.ControlAdd()
    return response