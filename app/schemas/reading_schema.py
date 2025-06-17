from app import BaseModel, Enum
from app import datetime


class LeakType(Enum):
    FALSE = False
    TRUE = True

class ReadingCreate(BaseModel):
    id: int
    user_id: int
    gas_level: float
    weight: float
    temperature: float
    leak: LeakType
    
class ReadingResponse(BaseModel):
    id: int
    sensor_id: int
    gas_level: float
    weight: float
    temperature : float
    leak: LeakType
    datetime: datetime