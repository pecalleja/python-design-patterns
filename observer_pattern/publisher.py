from abc import ABC, abstractmethod
from subscriber import RouteSubscriber


class SchedulePublisher(ABC):

    def __init__(self, name):
        self._listeners = set()
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
        self.notify(name=name)

    @abstractmethod
    def notify(self, **kwargs):
        pass

    @abstractmethod
    def attach(self, subscriber: RouteSubscriber):
        pass

    @abstractmethod
    def detach(self, subscriber: RouteSubscriber):
        pass


class Schedule(SchedulePublisher):

    def attach(self, subscriber: RouteSubscriber):
        self._listeners |= {subscriber}

    def detach(self, subscriber: RouteSubscriber):
        self._listeners -= {subscriber}

    def notify(self, **kwargs):
        for listener in self._listeners.copy():
            listener.update(self, **kwargs)
