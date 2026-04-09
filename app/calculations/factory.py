from app.models.calculation import CalculationType

class AddOperation:
    def compute(self, a: float, b: float) -> float:
        return a + b

class SubOperation:
    def compute(self, a: float, b: float) -> float:
        return a - b

class MultiplyOperation:
    def compute(self, a: float, b: float) -> float:
        return a * b

class DivideOperation:
    def compute(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

class CalculationFactory:
    _operations = {
        CalculationType.add:      AddOperation(),
        CalculationType.subtract: SubOperation(),
        CalculationType.multiply: MultiplyOperation(),
        CalculationType.divide:   DivideOperation(),
    }

    @classmethod
    def get_operation(cls, calc_type: CalculationType):
        op = cls._operations.get(calc_type)
        if not op:
            raise ValueError(f"Unknown calculation type: {calc_type}")
        return op

    @classmethod
    def compute(cls, calc_type: CalculationType, a: float, b: float) -> float:
        return cls.get_operation(calc_type).compute(a, b)