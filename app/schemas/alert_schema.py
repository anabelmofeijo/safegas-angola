from app import BaseModel, datetime
from app import Enum


class AlertType(str, Enum):
    LEAK = "Vazamento"
    FIRE = "incendio"
    SOS = "SOS"
    OTHER = "outro"

class AlertCreate(BaseModel):
    user_id: int
    type: AlertType
    message: str
    
class Alert(BaseModel):
    user_id: int
    type: AlertType
    message: str
    resolved: bool
    alerted_at: datetime

class AlertResolvedResponse(BaseModel):
    message: str
    
    
    