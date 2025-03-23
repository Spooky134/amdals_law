from .point import Point
from .amdal_n import AmdalN


class AmdalNetworkN(AmdalN):
    NAME = 'dependence of R on n (Amdal network)'
    FORMULA = 'R = 1 / (a + (1 - a) / n) + ca * ct'

    def __init__(self, n_start: int, n_end: int, step: int=0.1, a: float=0.1, ca: float=0.1, ct: float=0.1):
        super().__init__(n_start, n_end, step, a)
        self._ca = ca
        self._ct = ct

    def formula(self, variable) -> Point:
        return Point(variable, 1/(self._a+((1-self._a)/variable)) + self._ca * self._ct )