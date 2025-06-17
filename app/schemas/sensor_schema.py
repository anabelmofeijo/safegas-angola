from app import BaseModel, datetime, Enum


class TypeConnection(str, Enum):
    WIFI = "wi-fi"
    CABLE = "cabeada"

class Status(str, Enum):
    ON = "ligado"
    OFF = "desligado"

class SensorRegister(BaseModel):
    id: int
    sensor_id: int
    sensor_name: str
    type_connection: TypeConnection
    status: Status

class SensorResponse(BaseModel):
    id: int
    sensor_id : int
    sensor_name: str
    type_connection: TypeConnection
    location: str
    status: Status
    last_reading: datetime