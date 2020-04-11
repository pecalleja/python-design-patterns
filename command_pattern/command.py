from abc import ABC, abstractmethod
from receiver import Route


class RouteCommand(ABC):
    route: Route

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @abstractmethod
    def execute(self):
        pass


class DisableRouteCommand(RouteCommand):

    def execute(self):
        if not hasattr(self, 'route'):
            raise ValueError("route object not defined")
        else:
            self.route.is_disabled = True
            print(f"Route {self.route.name} disabled")


class CloneRouteCommand(RouteCommand):

    def execute(self):
        if not hasattr(self, 'route'):
            raise ValueError("route object not defined")
        else:
            new_route = Route(**self.route.serialize())
            self.route = new_route
            print(f"Clone of route: {new_route.serialize()}")
            return new_route


class CreateRouteCommand(RouteCommand):

    def execute(self, **kwargs):
        new_route = Route(
            kwargs.get('route_id'),
            kwargs.get('route_name')
        )
        print(f"Created new route: {new_route.serialize()}")
        self.route = new_route
        return new_route
