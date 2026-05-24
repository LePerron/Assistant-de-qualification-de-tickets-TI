from contextlib import contextmanager
from core.config import get_settings

import psycopg


class DbSession:
    """Classe de configuration pour gérer les sessions PostgreSQL."""

    def __init__(self, database_url):
        self.db_url = f"postgresql://{get_settings().db_user}:{get_settings().db_password}@{get_settings().db_host}:{get_settings().db_port}/{get_settings().dbname}"

    @contextmanager
    def get_cursor(self):
        """Gestionnaire de contexte pour obtenir un curseur SQL sécurisé."""

        with psycopg.connect(self.db_url) as conn:
            with conn.cursor() as cur:
                try:
                    yield cur
                except psycopg.OperationalError as e:
                    print(f"Database connection error: {e}")
                except Exception:
                    raise


db = DbSession(get_settings().database_url)
