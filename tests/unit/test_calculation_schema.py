import pytest
from pydantic import ValidationError
from app.schemas.calculation import CalculationCreate, CalculationType
from app.calculations.factory import CalculationFactory

# --- Schema validation tests ---

def test_valid_add():
    c = CalculationCreate(a=10, b=5, type="Add")
    assert c.type == CalculationType.add

def test_valid_subtract():
    c = CalculationCreate(a=10, b=5, type="Sub")
    assert c.type == CalculationType.subtract

def test_valid_multiply():
    c = CalculationCreate(a=3, b=4, type="Multiply")
    assert c.type == CalculationType.multiply

def test_valid_divide():
    c = CalculationCreate(a=10, b=2, type="Divide")
    assert c.type == CalculationType.divide

def test_invalid_type_raises():
    with pytest.raises(ValidationError):
        CalculationCreate(a=1, b=2, type="Modulo")

def test_divide_by_zero_raises():
    with pytest.raises(ValidationError):
        CalculationCreate(a=5, b=0, type="Divide")

def test_missing_fields_raises():
    with pytest.raises(ValidationError):
        CalculationCreate(a=1, type="Add")   # missing b

# --- Factory tests ---

def test_factory_add():
    assert CalculationFactory.compute(CalculationType.add, 3, 4) == 7

def test_factory_subtract():
    assert CalculationFactory.compute(CalculationType.subtract, 10, 3) == 7

def test_factory_multiply():
    assert CalculationFactory.compute(CalculationType.multiply, 3, 4) == 12

def test_factory_divide():
    assert CalculationFactory.compute(CalculationType.divide, 10, 2) == 5.0

def test_factory_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        CalculationFactory.compute(CalculationType.divide, 5, 0)

def test_factory_unknown_type():
    with pytest.raises((ValueError, KeyError)):
        CalculationFactory.get_operation("Modulo")