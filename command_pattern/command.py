from abc import ABC
from abc import abstractmethod

from receiver import Location
from receiver import RouteReceiver


class RouteCommand(ABC):
    def __init__(self, receiver: RouteReceiver):
        self.receiver = receiver

    @abstractmethod
    def execute(self, **kwargs):
        pass


class AddPointCommand(RouteCommand):
    def __init__(self, receiver: RouteReceiver, point: Location):
        super(AddPointCommand, self).__init__(receiver)
        self.point = point

    def execute(self):
        try:
            if not self.receiver.points:
                self.receiver.points = [self.point]
            else:
                self.receiver.points.append(self.point)
            return self.receiver.calculate_distance()
        except IndexError:
            return False

    def __repr__(self):
        return f"<AddPoint({self.point})>"


class RemovePointCommand(RouteCommand):
    def execute(self):
        try:
            self.receiver.points.pop()
            return self.receiver.calculate_distance()
        except IndexError:
            return False

    def __repr__(self):
        return "<RemovePoint()>"
