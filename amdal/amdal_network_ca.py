from .point import Point
from .base import FormulaBase


class AmdalNetworkCa(FormulaBase):
    NAME = 'dependence of R on ca (Amdal network)'
    FORMULA = 'R = 1 / (a + (1 - a) / n) + ca * ct'
    
    def __init__(self, ca_start: float, ca_end: float, step: float=0.1, n: int=5, a: float=0.1, ct: float=0.1):
        super().__init__(ca_start, ca_end, step)
        self._n = n
        self._a = a
        self._ct = ct

    
    def formula(self, variable) -> Point:
        return Point(variable, 1/(self._a+((1-self._a)/self._n)) + variable * self._ct )