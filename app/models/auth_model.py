from app import (
    Base,
    Integer,
    String,
    Column,
    datetime,
    DateTime
)


class AuthModel(Base):
    __tablename__ = "auth"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    password = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.utcnow())
    
    