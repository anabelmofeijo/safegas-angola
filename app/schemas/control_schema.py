from app import BaseModel, Enum


class TyperMessage(str, Enum):
    ON = "ligar"
    OFF = "desligar"

class ControlOnOff(BaseModel):
    user_id: int
    message: TyperMessage
    