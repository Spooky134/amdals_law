from .point import Point
from .amdal_a import AmdalA


class AmdalNetworkA(AmdalA):
    NAME = 'dependence of R on a (Amdal network)'
    FORMULA = 'R = 1 / (a + (1 - a) / n) + ca * ct'
    
    def __init__(self, a_start: float, a_end: float, step: float=0.1, n: int=5, ca: float=0.1, ct: float=0.1):
        super().__init__(a_start, a_end, step, n)
        self._ca = ca
        self._ct = ct
        
    
    def formula(self, variable) -> Point:
        return Point(variable, 1/(variable+((1-variable)/self._n)) + self._ca * self._ct)