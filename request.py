@dataclass

class Reponse:
    status_code: int
    text: str
    as_dict: object
    headers: dict