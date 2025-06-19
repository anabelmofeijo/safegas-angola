from app import (
    Base,
    Integer,
    String,
    Column,
    datetime,
    DateTime,
    relationship
)


class AuthModel(Base):
    __tablename__ = "auth"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    password = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    sensors = relationship("SensorModel", back_populates="user", cascade="all, delete")
    readings = relationship("ReadingModel", back_populates="user", cascade="all, delete")
    alerts = relationship("AlertModel", back_populates="user", cascade="all, delete")
    controls = relationship("ControlModel", back_populates="user", cascade="all, delete")
   