from pydantic import BaseModel


class Ticket(BaseModel):
    id: int
    name: str

