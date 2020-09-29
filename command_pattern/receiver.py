from abc import ABC
from abc import abstractmethod
from dataclasses import dataclass
from math import pow
from math import sqrt
from typing import List
from typing import Optional


@dataclass()
class Location:
    latitude: float
    longitude: float

    def __str__(self):
        return f"{self.latitude},{self.longitude}"

    @property
    def x(self):
        return self.latitude

    @property
    def y(self):
        return self.longitude


class RouteReceiver(ABC):
    points = List[Location]

    @abstractmethod
    def calculate_distance(self):
        raise NotImplementedError


class Route(RouteReceiver):
    def __init__(self, name: str, points: Optional[List[Location]] = None):
        self.name = name
        self.points = points

    def calculate_distance(self) -> float:
        if not self.points or len(self.points) <= 1:
            return 0
        else:
            total = 0
            for index in range(len(self.points) - 1):
                a = abs(self.points[index].x - self.points[index + 1].x)
                b = abs(self.points[index].y - self.points[index + 1].y)
                total += sqrt(pow(a, 2) + pow(b, 2))
            return total
