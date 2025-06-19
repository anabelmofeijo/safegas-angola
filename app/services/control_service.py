from app.models.control_model import ControlModel
from app.config import SessionLocal


class ControlDatabase:
    
    @staticmethod
    def ControlAdd(data):
        with SessionLocal() as db:
            new_data = ControlModel(**data)
            db.add(new_data)
            db.commit()
            db.refresh(new_data)
            return {"control_added": new_data} 
        
    @staticmethod
    def ControlListAll():
        with SessionLocal() as db:
            new_data = db.query(ControlModel).all()
            if new_data:
                return new_data
            return {"error":"there is not any control in database"}