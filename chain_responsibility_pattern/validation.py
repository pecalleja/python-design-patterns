from handler import Handler
from handler import ValidationError


class Validator:
    def __init__(self, handler: Handler):
        self.handler = handler

    def validate(self, request):
        try:
            self.handler.handle(request)
        except ValidationError:
            return False
        return True
