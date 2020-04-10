from publisher import Schedule
from subscriber import PublicRoute, PrivateRoute


def test_observer_pattern():
    schedule = Schedule('Every day at 9:00 AM')

    for i in range(3):
        route = PublicRoute(schedule.name)
        schedule.attach(route)
    private_route = PrivateRoute(schedule.name)
    schedule.attach(private_route)
    assert len(schedule._listeners) == 4
    schedule.name = "Only Monday at 6:00 AM"
    assert len(schedule._listeners) == 3
    assert private_route._schedule_name is None
    for route in schedule._listeners:
        assert isinstance(route, PublicRoute)
