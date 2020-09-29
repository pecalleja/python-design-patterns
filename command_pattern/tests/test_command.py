import pytest
from command import AddPointCommand
from command import RemovePointCommand
from invoker import Inventory
from receiver import Location
from receiver import Route


@pytest.fixture()
def point1():
    return Location(0, 0)


@pytest.fixture()
def point2():
    return Location(3, 4)


@pytest.fixture()
def route():
    return Route("New Route")


def test_commands(point1, point2, route):
    command1 = AddPointCommand(route, point1)
    assert command1.execute() == 0
    command2 = AddPointCommand(route, point2)
    assert command2.execute() == 5
    command3 = RemovePointCommand(route)
    assert command3.execute() == 0


def test_invoker(point1, point2, route):
    command1 = AddPointCommand(route, point1)
    command2 = RemovePointCommand(route)
    invoker = Inventory()
    invoker.add_command(command1)
    invoker.add_command(command2)
    invoker.execute_pipeline()
    assert not command1.receiver.points
    assert invoker.invoke(command2) is False
