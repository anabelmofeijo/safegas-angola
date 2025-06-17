from app import BaseModel, Enum, datetime


class TyperMessage(str, Enum):
    ON = "ligar"
    OFF = "desligar"

class ControlOn(BaseModel):
    id: int
    user_id: int
    message: TyperMessage.ON
    
class ControlOff(BaseModel):
    id: int
    user_id: int
    message: TyperMessage.OFF
    date: datetime