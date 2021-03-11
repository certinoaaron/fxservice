class Response:
    def __init__(self):
        self.success = None
        self.from_ = None
        self.to = None
        self.amount = None
        self.date = None
        self.rate = None
        self.result = None

    def __str__(self):
        return str(self.__repr__())

    def __repr__(self):
        return {
            "success": self.success,
            "query": {"from": self.from_, "to": self.to, "ammount": self.amount},
            "date": self.date,
            "rate": self.rate,
            "result": self.result,
        }

    @property
    def success(self) -> bool:
        """Getter for success attribute

        :return: if request was successful or not
        :rtype: bool
        """
        return self.success

    @success.setter
    def success(self, value: bool):
        """Setter for success attribute

        :param value: if request was successful or not
        :type value: bool
        """
        self.success = value

    @property
    def from_(self) -> str:
        """Getter for from attribute

        :return: [description]
        :rtype: str
        """
        return self.from_

    @from_.setter
    def from_(self, value: str):
        self.from_ = value


def response_builder() -> Response:
    pass
