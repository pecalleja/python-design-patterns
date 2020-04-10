from strategy import Trip


class TripInventory:

    def __init__(self, trip: Trip):
        self._trip = trip

    @property
    def trip(self):
        return self._trip

    @trip.setter
    def trip(self, trip: Trip):
        self._trip = trip

    def calculate(self) -> int:
        return self._trip.available_seats()
