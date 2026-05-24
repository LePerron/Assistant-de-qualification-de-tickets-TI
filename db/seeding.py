from pydantic import ValidationError

from core.logger import logger
from core.utils import read_file
from db.session import db
from schema.ticketmodel import TicketModel


def seed_db():
    seed_tickets()

def seed_tickets():
    tickets = read_file("tickets_seeding.json")

    valid_records = []
    for index, item in enumerate(tickets, start=1):
        try:
            ticket = TicketModel(**item)
            valid_records.append((ticket.id, ticket.subject, ticket.description, ticket.department))
        except ValidationError as e:
            logger.error(f"Validation error on recored {index}: {e.errors()}")

    if not valid_records:
        logger.warning("No valid records to insert.")
        return

    insert_query = """
                   INSERT INTO users (id, name, email, is_active)
                   VALUES (%s, %s, %s, %s) ON CONFLICT (id) DO NOTHING; \
                   """

    with db.get_cursor() as cursor:
        cursor.executemany(insert_query, valid_records)

    logger.info(f"Successfully seeded {len(valid_records)} records into the database.")
