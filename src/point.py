"""Module containing a Point and Line CLass"""

from math import sqrt
from attrs import define, field, asdict


@define
class Point:
    """A 3D Point"""

    x: float
    y: float
    z: float
    _desc: str = field(kw_only=True)


@define
class Line:
    """A 3D Line defined by two points"""

    p1: Point
    p2: Point

    def magnitude(self):
        """
        Calculate the magnitude of the line

        :param: self
        :return:
        """
        return sqrt(
            pow(self.p1.x - self.p2.x, 2)
            + pow(self.p1.y - self.p2.y, 2)
            + pow(self.p1.z - self.p2.z, 2)
        )


if __name__ == "__main__":
    p = Point(1.5, 2, 3, desc="Start")
    print(f"{p}")
    line = Line(p, Point(200, 4, -6, desc="End"))
    print(f"{line}")
    print(asdict(line))
    print(f"{line.magnitude():.3}")
