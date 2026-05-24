from contextlib import contextmanager
from core.config import get_settings
import psycopg

settings = get_settings()


class DbSession:
    """Classe de configuration pour gérer les sessions PostgreSQL."""

    def __init__(self):
        self.database_url = settings.database_url

    @contextmanager
    def get_cursor(self):
        """Gestionnaire de contexte pour obtenir un curseur SQL sécurisé."""

        with psycopg.connect(self.database_url) as conn:
            with conn.cursor() as cur:
                try:
                    yield cur
                except psycopg.OperationalError as e:
                    print(f"Database connection error: {e}")
                except Exception:
                    raise


db = DbSession()
