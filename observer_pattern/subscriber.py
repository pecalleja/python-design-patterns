from abc import ABC, abstractmethod


class RouteSubscriber(ABC):

    def __init__(self, schedule_name):
        self._schedule_name = schedule_name

    @abstractmethod
    def update(self, publisher, **kwargs):
        pass


class PublicRoute(RouteSubscriber):

    def update(self, publisher, **kwargs):
        if self._schedule_name != publisher.name:
            print(
                f"The schedule changed the name "
                f"from: {self._schedule_name} "
                f"to: {publisher.name}")
            self._schedule_name = publisher.name


class PrivateRoute(RouteSubscriber):

    def update(self, publisher, **kwargs):
        if self._schedule_name != publisher.name:
            print("The schedule have changed so we leave :(")
            publisher.detach(self)
            self._schedule_name = None
