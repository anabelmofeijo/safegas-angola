from app import (
    Base,
    Integer,
    Column,
    String,
    datetime,
    DateTime
)


class SensorModel(Base):
    __tablename__ = "sensor"
    
    id = Column(Integer, primary_key=True, index=True)
    sensor_id = Column(Integer, index=True)
    sensor_name = Column(String, index=True)
    type_connection = Column(String, index=True)
    location = Column(String, index=True)
    status = Column(String, index=True)
    datetime = Column(DateTime, default=datetime.utcnow())