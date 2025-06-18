from app import (
    Base,
    Integer,
    Column,
    datetime,
    Boolean,
    DateTime,
    Float
)


class ReadingModel(Base):
    __tablename__= "reading"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    gas_level = Column(Float)
    weight = Column(Float)
    temperature = Column(Float)
    leak = Column(Boolean, index=True)
    date = Column(DateTime, default=datetime.utcnow())