from pydantic import BaseModel, field_validator, model_validator
from enum import Enum
from typing import Optional

class CalculationType(str, Enum):
    add      = "Add"
    subtract = "Sub"
    multiply = "Multiply"
    divide   = "Divide"

class CalculationCreate(BaseModel):
    a:       float
    b:       float
    type:    CalculationType
    user_id: Optional[int] = None

    @field_validator("type")
    @classmethod
    def type_must_be_valid(cls, v):
        allowed = {e.value for e in CalculationType}
        if v not in allowed:
            raise ValueError(f"type must be one of {allowed}")
        return v

    @model_validator(mode="after")
    def check_no_divide_by_zero(self):
        if self.type == CalculationType.divide and self.b == 0:
            raise ValueError("b cannot be zero when type is Divide")
        return self

class CalculationRead(BaseModel):
    id:      int
    a:       float
    b:       float
    type:    CalculationType
    result:  Optional[float]
    user_id: Optional[int]

    model_config = {"from_attributes": True}