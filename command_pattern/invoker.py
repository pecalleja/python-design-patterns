from command import RouteCommand


class Inventory:

    steps = []

    def add_command(self, command: RouteCommand):
        self.steps.append(command)

    def execute_pipeline(self):
        for step in self.steps:
            result = step.execute()
            print(f"Executing: {step}, result: {result}")

    @staticmethod
    def invoke(command: RouteCommand):
        result = command.execute()
        print(f"Executing: {command}, result: {result}")
        return result
