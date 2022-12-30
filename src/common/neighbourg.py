
from common.piste import *

@dataclass(frozen=True)
class Neighbourg(Point):
    direction: int

    def piste(self):
        return Point(self.x,self.y)
