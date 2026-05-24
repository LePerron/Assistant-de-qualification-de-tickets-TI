from pydantic import ValidationError, TypeAdapter
from core.logger import logger
from core.utils import read_file
from db.session import db
from schema.ticket import Ticket


async def seed_db():
    await seed_tickets()


async def seed_tickets():
    tickets_json = read_file("tickets_seeding.json")

    ticket_list_adapter = TypeAdapter(list[Ticket])
    ticket_records = []

    try:
        ticket_records = ticket_list_adapter.validate_json(tickets_json)
    except ValidationError as e:
        logger.error(f"Validation error for ticket records json: {e.errors()}")

    if not ticket_records:
        logger.warning("No valid records to insert.")
        return

    insert_query = """
                   INSERT INTO users (id, name, email, is_active)
                   VALUES (%s, %s, %s, %s) ON CONFLICT (id) DO NOTHING; \
                   """

    with db.get_cursor() as cursor:
        cursor.executemany(insert_query, ticket_records)

    logger.info(f"Successfully seeded {len(ticket_records)} records into the database.")
