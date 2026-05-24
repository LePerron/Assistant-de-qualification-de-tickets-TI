from pydantic import BaseModel

from schema.ticket_category import TicketCategory
from schema.priority import TicketPriority


class Ticket(BaseModel):
    id: str
    subject: str
    description: str
    department: str
    category: TicketCategory | None = None
    priority: TicketPriority | None = None
