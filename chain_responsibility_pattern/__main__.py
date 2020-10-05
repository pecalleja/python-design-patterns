from handler import DriverValidator
from handler import TripValidator
from handler import VanValidator
from validation import Validator

if __name__ == "__main__":
    request = {
        "van": {"id": 1, "name": "U01"},
        "driver": {"id": 1, "name": "John Doe"},
        "trip": {"id": 1, "seats": 1},
    }
    van = VanValidator()
    driver = DriverValidator()
    trip = TripValidator()
    validations = van.set_next(driver).set_next(trip)
    result = Validator(validations).validate(request)
    print(f"validating request: {request}, result: {result}")
