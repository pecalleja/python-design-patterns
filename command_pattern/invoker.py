from command import RouteCommand


class Inventory:

    steps = []

    def add_command(self, command: RouteCommand):
        self.steps.append(command)

    def execute_pipeline(self):
        for step in self.steps:
            step.execute()
