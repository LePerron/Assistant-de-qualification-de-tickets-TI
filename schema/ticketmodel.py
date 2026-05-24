from pydantic import BaseModel

from schema.department import Department


class TicketModel(BaseModel):
    id: int
    subject: str
    description: str
    department: Department