import pg8000
from dotenv import load_dotenv
from pg8000.dbapi import ProgrammingError, InterfaceError

class PGClient:

    def __init__(self, host, database, password, user='postgres', port=5432) -> None:
        load_dotenv()
        self.db_params = {
            "host": host,
            "database": database,
            "user": user,
            "password": password,
            "port": port
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
            with self.get_conn() as conn:
                conn.rollback()
        
        except Exception as e:
            print(f"An error occurred: {e}")
            with self.get_conn() as conn:
                conn.rollback()

    def fetch_query(self, query):
        try:
            with self.get_conn() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query)
                    return cursor.fetchall()

        except (ProgrammingError, InterfaceError) as e:
            print(f"Database error occurred: {e}")
            with self.get_conn() as conn:
                conn.rollback()
        
        except Exception as e:
            print(f"An error occurred: {e}")
            with self.get_conn() as conn:
                conn.rollback()
            
