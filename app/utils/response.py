
class Response:

    def __init__(self):
        self.success = None
        self._from = None
        self.to = None
        self.amount = None 
        



    def __str__(self):
        return str(self.__repr__())

    def __repr__(self):
        return { "success": self.success

        }

    @property
    def success(self) -> bool:
        return self.success

    @success.setter
    def success(self, value: bool):
        self.success = value

    


def response_builder() -> Response:
    pass
