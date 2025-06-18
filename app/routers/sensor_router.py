from app import APIRouter
from app.services.sensor_service import SensorService
from app.schemas.sensor_schema import SensorRegister


sensor = APIRouter()

@sensor.get("/")
async def running():
    return {"message":"sensor is running"}

@sensor.post("/register/")
async def sensor_register(data: SensorRegister):
    service = SensorService()
    response = service.SensorAdd(data=data)
    return response

@sensor.get("/list/")
async def list_sensor():
    service = SensorService()
    response = service.SensorListAll()
    return response

@sensor.get("/find/{sensor_name}")
async def find_sensor(sensor_name: str):
    service = SensorService()
    response = service.FindSensor(sensor_name)
    return response

@sensor.delete("/delete/{id}")
async def delete_sensor(id: int):
    service = SensorService()
    response = service.SensorDelete(id)
    return response