

from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def pair(self):
        return (self.x,self.y)

# class Piste:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def pair(self):
#         return (self.x,self.y)

#     def __str__(self):
#         return f'({self.x}, {self.y})'

#     # for objects inside lists..
#     def __repr__(self):
#         return self.__str__()                