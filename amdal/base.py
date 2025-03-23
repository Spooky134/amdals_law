import numpy as np
from .point import Point


class FormulaBase:
    NAME = 'Info'
    FORMULA = 'Formula'

    def __init__(self, start, end, step):
        self._range_of_values = np.arange(start, end, step).tolist()

    def evalute(self) -> list[Point]:
        ls = []
        for val in self._range_of_values:
            ls.append(self.formula(val))

        return ls
    
    def formula(self, variable) -> Point:
        pass