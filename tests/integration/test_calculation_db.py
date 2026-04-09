import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base
from app.models.calculation import Calculation, CalculationType as ModelCalcType
from app.models.user import User  # ensures users table is registered in metadata
from app.calculations.factory import CalculationFactory
from app.schemas.calculation import CalculationCreate, CalculationType
import os

DATABASE_URL = os.getenv(
    "TEST_DATABASE_URL",
    os.getenv("DATABASE_URL", "postgresql://user:password@localhost:55433/mydb"),
)

@pytest.fixture(scope="module")
def db_session():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)

def test_insert_add_calculation(db_session):
    schema = CalculationCreate(a=6, b=4, type="Add")
    result = CalculationFactory.compute(schema.type, schema.a, schema.b)

    calc = Calculation(
        a=schema.a, b=schema.b,
        type=ModelCalcType.add, result=result
    )
    db_session.add(calc)
    db_session.commit()
    db_session.refresh(calc)

    assert calc.id is not None
    assert calc.result == 10.0

def test_insert_divide_calculation(db_session):
    schema = CalculationCreate(a=20, b=4, type="Divide")
    result = CalculationFactory.compute(schema.type, schema.a, schema.b)

    calc = Calculation(
        a=schema.a, b=schema.b,
        type=ModelCalcType.divide, result=result
    )
    db_session.add(calc)
    db_session.commit()
    db_session.refresh(calc)

    assert calc.result == 5.0

def test_query_all_calculations(db_session):
    calcs = db_session.query(Calculation).all()
    assert len(calcs) >= 2

def test_invalid_schema_not_inserted(db_session):
    from pydantic import ValidationError
    with pytest.raises(ValidationError):
        CalculationCreate(a=5, b=0, type="Divide")  # never reaches DB
    count_before = db_session.query(Calculation).count()
    # count should be unchanged
    assert db_session.query(Calculation).count() == count_before
