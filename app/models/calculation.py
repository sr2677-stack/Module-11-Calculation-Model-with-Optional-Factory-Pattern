from sqlalchemy import Column, Integer, Float, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.database import Base
import enum

class CalculationType(str, enum.Enum):
    add      = "Add"
    subtract = "Sub"
    multiply = "Multiply"
    divide   = "Divide"

class Calculation(Base):
    __tablename__ = "calculations"

    id      = Column(Integer, primary_key=True, index=True)
    a       = Column(Float, nullable=False)
    b       = Column(Float, nullable=False)
    type    = Column(Enum(CalculationType), nullable=False)
    result  = Column(Float, nullable=True)  # stored on insert
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    owner = relationship("User", back_populates="calculations")