from app import BaseModel, Enum


class TyperMessage(str, Enum):
    ON = "ligar"
    OFF = "desligar"

class ControlOn(BaseModel):
    message: TyperMessage.ON
    
class ControlOff(BaseModel):
    message: TyperMessage.OFF
    
    