from app import (
    Base,
    Integer,
    Column,
    datetime,
    Boolean,
    DateTime,
    Float,
    relationship,
    ForeignKey
)


class ReadingModel(Base):
    __tablename__ = "reading"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("auth.id"))
    sensor_id = Column(Integer, ForeignKey("sensor.id"))
    gas_level = Column(Float)
    weight = Column(Float)
    temperature = Column(Float)
    leak = Column(Boolean, index=True)
    date = Column(DateTime, default=datetime.utcnow)

    user = relationship("AuthModel", back_populates="readings")
    sensor = relationship("SensorModel", back_populates="readings")