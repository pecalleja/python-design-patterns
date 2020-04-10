from strategy import PrivateTrip, PublicTrip
from context import TripInventory


def test_strategy_pattern():
    van = {
        "seats": 19
    }
    private_trip = PrivateTrip(van)
    public_trip = PublicTrip(van)
    context = TripInventory(private_trip)
    assert context.calculate() == van.get('seats') - private_trip.private_seats
    context.trip = public_trip
    assert context.calculate() == van.get('seats')
