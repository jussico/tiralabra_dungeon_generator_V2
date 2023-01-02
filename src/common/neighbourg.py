
from common.point import *

@dataclass(frozen=True)
class Neighbourg(Point):
    direction: int

    def piste(self):
        return Point(self.x,self.y)
