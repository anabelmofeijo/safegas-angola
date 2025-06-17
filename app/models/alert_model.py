from app import (
    Base,
    Integer,
    String,
    Column,
    Boolean,
    datetime,
    DateTime
)

class AlertModel(Base):
    __tablename__ = "alert"
    
    id = Column(Integer, primary_key=True, index=True)
    sensor_id = Column(Integer, primary_key=True, index=True)
    type = Column(String, index=True)
    message = Column(String, index=True)
    resolved = Column(Boolean, index=True)
    alerted_at = Column(DateTime, default=datetime.utcnow)
    
    