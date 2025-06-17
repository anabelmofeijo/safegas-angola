from app.models.alert_model import AlertModel
from config import SessionLocal


class AlertDatabase:
    
    @staticmethod
    def AlertAdd(alert_data: dict):
        with SessionLocal() as db:
            new_alert = AlertModel(**alert_data)
            db.add(new_alert)
            db.commit()
            db.refresh(new_alert)
            db.close()
            return {"new_alert": new_alert}
        
    @staticmethod
    def AlertDelete(id: int):
        with SessionLocal() as db:
            alert = db.query(AlertModel).get(id)
            if alert:
                db.delete(alert)
                db.commit()
                return {"message": "Alert Deleted"}
            return { "error": "Alert not found!"}
        
class AlertService:
    
    @staticmethod
    def AlertListAll():
        with SessionLocal() as db:
            alerts = db.query(AlertModel).all()
            if alerts:
                return alerts
            return {"error": "there is not alerts in database"}