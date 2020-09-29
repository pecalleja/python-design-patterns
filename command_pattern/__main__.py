from command import AddPointCommand
from command import RemovePointCommand
from invoker import Inventory
from receiver import Location
from receiver import Route


if __name__ == "__main__":
    inventory = Inventory()
    route = Route("Some route name")
    inventory.add_command(
        AddPointCommand(receiver=route, point=Location(1, 1))
    )
    inventory.add_command(
        AddPointCommand(receiver=route, point=Location(2, 2))
    )
    inventory.execute_pipeline()
    inventory.invoke(RemovePointCommand(receiver=route))
