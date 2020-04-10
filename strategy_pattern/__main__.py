from strategy import PrivateTrip, PublicTrip
from context import TripInventory

if __name__ == '__main__':
    van = {
        "seats": 19
    }
    private_trip = PrivateTrip(van)
    public_trip = PublicTrip(van)
    context = TripInventory(private_trip)
    print(f"Private Trip available seats: {context.calculate()}")
    context.trip = public_trip
    print(f"Public Trip available seats: {context.calculate()}")
