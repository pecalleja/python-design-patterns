from publisher import Schedule
from subscriber import PublicRoute, PrivateRoute


if __name__ == "__main__":
    schedule = Schedule('Every day at 9:00 AM')

    for i in range(3):
        route = PublicRoute(schedule.name)
        schedule.attach(route)

    schedule.attach(PrivateRoute(schedule.name))

    schedule.name = "Only Monday at 6:00 AM"
