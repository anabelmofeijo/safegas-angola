from app import (
    Base,
    Integer,
    String,
    Column,
    datetime,
    DateTime
)


class ControlModel(Base):
    __tablename__ = "control"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    message = Column(String, index=True)
    date = Column(DateTime, default=datetime.utcnow())