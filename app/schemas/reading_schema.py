from app import BaseModel, Enum
from app import datetime


class LeakType(Enum):
    FALSE = False
    TRUE = True

class ReadingCreate(BaseModel):
    sensor_id: int
    gas_level: float
    cylinder_weight: float
    temperature: float
    leak: LeakType
    
class ReadingResponse(BaseModel):
    sensor_id: int
    gas_level: float
    cylinder_weight: float
    temperature : float
    leak: LeakType
    datetime: datetime