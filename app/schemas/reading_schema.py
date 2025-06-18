from app import BaseModel
from app import datetime




class ReadingCreate(BaseModel):
    user_id: int
    gas_level: float
    weight: float
    temperature: float
    leak: bool
    
class ReadingResponse(BaseModel):
    id: int
    sensor_id: int
    gas_level: float
    weight: float
    temperature : float
    leak: bool
    datetime: datetime