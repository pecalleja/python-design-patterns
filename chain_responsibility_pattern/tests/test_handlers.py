import pytest
from handler import DriverValidator
from handler import TripValidator
from handler import ValidationError
from handler import VanValidator
from validation import Validator


@pytest.fixture
def request_example():
    data = {
        "van": {"id": 1, "name": "U01"},
        "driver": {"id": 1, "name": "John Doe"},
        "trip": {"id": 1, "seats": 1},
    }
    return data.copy()


def test_driver(request_example):
    result = DriverValidator().handle(request_example)
    assert result is None
    request_example["driver"]["id"] = None
    with pytest.raises(ValidationError):
        DriverValidator().handle(request_example)


def test_van(request_example):
    result = VanValidator().handle(request_example)
    assert result is None
    request_example["van"]["id"] = None
    with pytest.raises(ValidationError):
        VanValidator().handle(request_example)


def test_trip(request_example):
    result = TripValidator().handle(request_example)
    assert result is None
    request_example["trip"]["seats"] = 0
    with pytest.raises(ValidationError):
        TripValidator().handle(request_example)


def test_chain_validations(request_example):
    trip = TripValidator()
    trip.set_next(VanValidator())
    validator = Validator(trip)
    assert validator.validate(request_example) is True
    request_example["van"]["id"] = None
    assert validator.validate(request_example) is False
