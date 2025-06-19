from app import (
    Base,
    Integer,
    String,
    Column,
    datetime,
    DateTime,
    relationship,
    ForeignKey
)


class ControlModel(Base):
    __tablename__ = "control"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("auth.id"))
    message = Column(String, index=True)
    date = Column(DateTime, default=datetime.utcnow)

    user = relationship("AuthModel", back_populates="controls")
