from core.logger import logger
from db.session import db


def initialize_db():
    print("DB Initialization if not exist...")

    with db.get_cursor() as cursor:
        cursor.execute(
            """
               CREATE TABLE IF NOT EXISTS tickets (
                  id INT PRIMARY KEY,
                  subject VARCHAR(255) NOT NULL,
                  description VARCHAR(255) NOT NULL,
                  department VARCHAR(255) NOT NULL,
                )
            """
        )

    logger.info("DB initialization complete.")




