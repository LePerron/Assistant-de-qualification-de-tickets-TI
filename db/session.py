from contextlib import contextmanager

import psycopg

from core.config import get_settings


class DbSession:
    """Gère les connexions PostgreSQL."""

    def __init__(self, database_url: str):
        self.database_url = database_url

    @contextmanager
    def get_cursor(self):
        """Gestionnaire de contexte pour obtenir un curseur SQL sécurisé."""

        try:
            with psycopg.connect(self.database_url) as conn:
                with conn.cursor() as cur:
                    yield cur

        except psycopg.OperationalError as e:
            raise RuntimeError("Database connection error") from e


settings = get_settings()
db = DbSession(settings.database_url)
