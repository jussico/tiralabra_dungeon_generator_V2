
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def pair(self):
        return (self.x,self.y)
