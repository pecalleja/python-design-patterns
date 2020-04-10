from abc import ABC, abstractmethod


class Trip(ABC):

    def __init__(self, van: dict):
        self.seats = van.get('seats', 0)

    @abstractmethod
    def available_seats(self):
        pass


class PublicTrip(Trip):

    def available_seats(self):
        return self.seats


class PrivateTrip(Trip):
    private_seats = 10

    def available_seats(self):
        return self.seats - self.private_seats
