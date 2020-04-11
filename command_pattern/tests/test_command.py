from command import CreateRouteCommand, DisableRouteCommand, CloneRouteCommand
from invoker import Inventory


def test_command_pattern():
    inventory = Inventory()
    create = CreateRouteCommand()
    route = create.execute(route_id=1, route_name="New Route")
    disable = DisableRouteCommand(route=route)
    clone = CloneRouteCommand(route=route)
    assert route is clone.route
    assert route.is_disabled is False
    assert clone.route.is_disabled is False
    inventory.add_command(disable)
    inventory.add_command(clone)
    inventory.execute_pipeline()
    assert route is not clone.route
    assert clone.route.is_disabled is True
