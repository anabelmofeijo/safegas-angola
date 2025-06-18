from app.models.reading_model import ReadingModel
from app.config import SessionLocal


class ReadingService:
    
    @staticmethod
    def ReadingAdd(data):
        with SessionLocal() as db:
            new_data = ReadingModel(**data)
            db.add(new_data)
            db.commit()
            db.refresh(new_data)
            db.close()
            return {"response": new_data}
        
    @staticmethod
    def ReadingList():
        with SessionLocal() as db:
            reading = db.query(ReadingModel).all()
            if reading:
                return reading
            return {"error": "there is not data on database"}
        
    @staticmethod
    def ReadingById(id: int):
        with SessionLocal() as db:
            response = db.query(ReadingModel).get(id)
            if response:
                return response
            return {"response": "not found"}
        
    @staticmethod
    def ReadingUserById(user_id: int):
        with SessionLocal() as db:
            response = db.query(ReadingModel).get(user_id)
            if response:
                return response
            return {"error": "user not found"}