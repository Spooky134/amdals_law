from .point import Point
from .base import FormulaBase


class AmdalN(FormulaBase):
    NAME = 'dependence of R on n (Amdal basic)'
    FORMULA = 'R = 1 / (a + (1 - a) / n)'

    def __init__(self, n_start: int, n_end: int, step: int=1, a: float=0.1):
        super().__init__(n_start, n_end, step)
        self._a = a
    
    def formula(self, variable) -> Point:
        return Point(variable, 1/(self._a+((1-self._a)/variable)))