from app import (
    Base,
    Integer,
    String,
    Column,
    Boolean,
    datetime,
    DateTime,
    relationship,
    ForeignKey
)


class AlertModel(Base):
    __tablename__ = "alert"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("auth.id"))
    sensor_id = Column(Integer, ForeignKey("sensor.id"))
    type = Column(String, index=True)
    message = Column(String, index=True)
    resolved = Column(Boolean, index=True, default=False)
    alerted_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("AuthModel", back_populates="alerts")
    sensor = relationship("SensorModel", back_populates="alerts")
