from app.models.sensor_model import SensorModel
from app.config import SessionLocal


class SensorService:
    
    @staticmethod
    def SensorAdd(data: dict):
        with SessionLocal() as db:
            new_data = SensorModel(**data)
            db.add(new_data)
            db.commit()
            db.refresh(new_data)
            return new_data
        
    @staticmethod
    def SensorDelete(id: int):
        with SessionLocal() as db:
            response = db.query(SensorModel).get(id)
            if response:
                db.delete(response)
                db.commit()
                return {"message": "user deleted successfully"}
            return {"error":"sensor not found"}
        
    @staticmethod
    def SensorListAll():
        with SessionLocal() as db:
            sensors = db.query(SensorModel).all()
            if sensors:
                return sensors
            return {"error":"there is not sensors in database"}
            
    @staticmethod
    def FindSensor(sensor_name: str):
        with SessionLocal() as db:
            sensor = db.query(SensorModel).filter(SensorModel.sensor_name == sensor_name).first()
            if sensor:
                return sensor
            return {"error": "sensor not found"}