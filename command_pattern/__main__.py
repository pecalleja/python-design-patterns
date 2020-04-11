from command import CreateRouteCommand, DisableRouteCommand, CloneRouteCommand
from invoker import Inventory


if __name__ == '__main__':
    inventory = Inventory()
    create = CreateRouteCommand()
    route = create.execute(route_id=1, route_name="New Route")

    disable = DisableRouteCommand(route=route)
    clone = CloneRouteCommand(route=route)

    inventory.add_command(disable)
    inventory.add_command(clone)
    inventory.execute_pipeline()
