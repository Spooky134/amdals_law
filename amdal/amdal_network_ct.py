from .point import Point
from .base import FormulaBase


class AmdalNetworkCt(FormulaBase):
    NAME = 'dependence of R on ct (Amdal network)'
    FORMULA = 'R = 1 / (a + (1 - a) / n) + ca * ct'
    
    def __init__(self, ct_start: float, ct_end: float, step: float=0.1, n: int=5, a: float=0.1, ca: float=0.1):
        super().__init__(ct_start, ct_end, step)
        self._n = n
        self._a = a
        self._ca = ca

    
    def formula(self, variable) -> Point:
        return Point(variable, 1/(self._a + ((1-self._a)/self._n)) + self._ca * variable)