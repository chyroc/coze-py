class CozeError(Exception):
    """
    base class for all coze errors
    """

    pass


class CozeAPIError(CozeError):
    """
    base class for all api errors
    """

    def __init__(self, code: int = None, msg: str = "", logid: str = None):
        self.code = code
        self.msg = msg
        self.logid = logid
        if code and code > 0:
            super().__init__(f"code: {code}, msg: {msg}, logid: {logid}")
        else:
            super().__init__(f"msg: {msg}, logid: {logid}")


class CozeEventError(CozeError):
    """
    base class for all event errors
    """

    def __init__(self, field: str = "", data: str = ""):
        self.field = field
        self.data = data
        if field:
            super().__init__(f"invalid event, field: {field}, data: {data}")
        else:
            super().__init__(f"invalid event, data: {data}")
