from app import BaseModel, Literal, datetime
from app import Enum


class AlertType(str, Enum):
    LEAK = "Vazamento"
    FIRE = "incendio"
    SOS = "SOS"
    OTHER = "outro"

class AlertCreate(BaseModel):
    sensor_id: int
    type: AlertType
    message: str
    
class Alert(BaseModel):
    sensor_id: int
    type: AlertType
    message: str
    resolved: bool
    timestamp: datetime

class AlertResolvedResponse(BaseModel):
    message: str
    
    
    