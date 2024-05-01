import os
import pg8000
from dotenv import load_dotenv
from pg8000.dbapi import ProgrammingError, InterfaceError

class PGClient:

    def __init__(self) -> None:
        load_dotenv()
        self.db_params = {
            "host": os.getenv("PG_HOST"),
            "database": os.getenv("PG_INSTANCE"),
            "user": os.getenv("PG_USER"),
            "password": os.getenv("PG_PASSWORD"),
            "port": os.getenv("PG_PORT")
        }

    def get_conn(self):
        return pg8000.connect(**self.db_params)

    def execute_query(self, query):
        try:
            with self.get_conn() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query)
                    conn.commit()

        except (ProgrammingError, InterfaceError) as e:
            print(f"Database error occurred: {e}")
        
        except Exception as e:
            print(f"An error occurred: {e}")

