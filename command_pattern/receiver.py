class Route:

    def __init__(self, route_id, route_name, is_disabled=False):
        self.id = route_id
        self.name = route_name
        self.is_disabled = is_disabled

    def serialize(self) -> dict:
        return {
            'route_id': self.id,
            'route_name': self.name,
            'is_disabled': self.is_disabled
        }
