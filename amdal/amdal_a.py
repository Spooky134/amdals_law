from .point import Point
from .base import FormulaBase


class AmdalA(FormulaBase):
    NAME = 'dependence of R on a (Amdal basic)'
    FORMULA = 'R = 1 / (a + (1 - a) / n)'

    def __init__(self, a_start: float, a_end: float, step: float=0.1, n: int=5):
        super().__init__(a_start, a_end, step)
        self._n = n
    
    def formula(self, variable) -> Point:
        return Point(variable, 1/(variable+((1-variable)/self._n)))