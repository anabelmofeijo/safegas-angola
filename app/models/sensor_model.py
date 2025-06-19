from app import (
    Base,
    Integer,
    Column,
    String,
    datetime,
    DateTime,
    relationship,
    ForeignKey
)


class SensorModel(Base):
    __tablename__ = "sensor" 
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("auth.id"))
    sensor_name = Column(String, index=True)
    type_connection = Column(String, index=True)
    location = Column(String, index=True)
    status = Column(String, index=True)
    datetime = Column(DateTime, default=datetime.utcnow)

    user = relationship("AuthModel", back_populates="sensors")
    readings = relationship("ReadingModel", back_populates="sensor", cascade="all, delete")
    alerts = relationship("AlertModel", back_populates="sensor", cascade="all, delete")