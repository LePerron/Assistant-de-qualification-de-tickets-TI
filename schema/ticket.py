from pydantic import BaseModel

from schema.department import Department


class Ticket(BaseModel):
    id: int
    subject: str
    description: str
    department: Department