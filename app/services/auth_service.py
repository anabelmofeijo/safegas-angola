from app.models.auth_model import AuthModel
from app.config import SessionLocal


class AuthDatabase:
    
    @staticmethod
    def AuthAdd(user_data: dict):
        with SessionLocal() as db:
            new_user = AuthModel(**user_data)
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
            return {"new_user": new_user}
        
    @staticmethod
    def AuthDelete(id: int):
        with SessionLocal() as db:
            user = db.query(AuthModel).get(id)
            if user:
                db.delete(user)
                db.commit()
                return {"message": "User deleted"}
            return {"error": "User not found"}

    @staticmethod
    def AuthFind(email):
        with SessionLocal() as db:
            user = db.query(AuthModel).get(email)
            if user:
                return user
            return {"error": "User not found"}

class AuthService:
    
    database = AuthDatabase()
    
    @staticmethod
    def AuthListUsers():
        with SessionLocal() as db:
            users = db.query(AuthModel).all()
            if users:
                return users
            return {"error": "there are not users in database"}
        
    def AuthRegister(self, user_data):
        self.database.AuthAdd(user_data)
        
    def AuthLogIn(self, email):
        response = self.database.AuthFind(email)
        if response:
            return response
        
    def AuthDeleteService(self, id):
        response = self.database.AuthDelete(id)
        if response:
            return response
        