from core.logger import logger
from db.session import db


async def initialize_db():
    logger.info("DB Initialization if not exist...")

    with db.get_cursor() as cursor:
        cursor.execute(
            """
               CREATE TABLE IF NOT EXISTS tickets (
                  id TEXT PRIMARY KEY,
                  subject TEXT NOT NULL,
                  description TEXT NOT NULL,
                  department TEXT,
                  priority TEXT
                )
            """
        )

    logger.info("DB initialization complete.")




