from app import APIRouter
from app.services.alert_service import AlertService, AlertDatabase
from app.schemas.alert_schema import Alert


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
async def post_alerts(alert: Alert):
    service = AlertDatabase()
    response = service.AlertAdd(alert_data=alert)
    return response

@alert.delete("/delete/{id}")
async def alert_delete(id: int):
    service = AlertDatabase()
    response = service.AlertDelete(id=id)
    return response