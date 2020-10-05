from abc import ABC
from abc import abstractmethod
from typing import Any
from typing import Optional


class ValidationError(Exception):
    pass


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler):
        raise NotImplementedError

    @abstractmethod
    def handle(self, request: Any) -> Optional[Any]:
        raise NotImplementedError


class BaseHandler(Handler):
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any) -> Optional[Any]:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


class VanValidator(BaseHandler):
    def handle(self, request: Any) -> Optional[Any]:
        van = request.get("van")
        if van.get("id"):
            return super().handle(request)
        else:
            raise ValidationError("Invalid van")


class DriverValidator(BaseHandler):
    def handle(self, request: Any) -> Optional[Any]:
        driver = request.get("driver")
        if driver.get("id"):
            return super().handle(request)
        else:
            raise ValidationError("Invalid driver")


class TripValidator(BaseHandler):
    def handle(self, request: Any) -> Optional[Any]:
        trip = request.get("trip")
        seats = trip.get("seats")
        if seats and seats > 0:
            return super().handle(request)
        else:
            raise ValidationError("Trip haven't enough seats")
