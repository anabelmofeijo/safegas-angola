from app.models.alert_model import AlertModel
from app.config import SessionLocal


class ControlDatabase:
    
    @staticmethod
    def ControlAdd(data):
        with SessionLocal() as db:
            new_data = AlertModel(**data)
            db.add(new_data)
            db.commit()
            db.refresh(new_data)
            return {"control_added": new_data}