from app import APIRouter
from app.services.alert_service import AlertService, AlertDatabase
from app.schemas.alert_schema import AlertCreate


alert = APIRouter()


@alert.get("/")
async def running():
    return {"message":"alert is running"}

@alert.get("/list/")
async def create():
    service = AlertService()
    response = service.AlertListAll()
    return response

@alert.post("/post/")
async def post_alerts(alert: AlertCreate):
    service = AlertDatabase()
    response = service.AlertAdd(alert_data=alert.dict())
    return response

@alert.delete("/delete/{id}")
async def alert_delete(id: int):
    service = AlertDatabase()
    response = service.AlertDelete(id=id)
    return response