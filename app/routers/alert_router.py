from app import APIRouter
from app.services.alert_service import AlertService


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
async def post_alerts():
    pass
