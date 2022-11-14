import contextlib
import psycopg2
from errors import InvalidQueryFetchOption
from enum import Enum


class FetchOptions(Enum):
    FETCH_ONE = 'fetch_one'
    FETCH_MANY = 'fetch_many'
    FETCH_ALL = 'fetch_all'


class Query:
    def __init__(self, sql, params, fetch: FetchOptions):
        self.sql = sql
        self.params = params
        self.fetch = fetch

    def execute(self, curr, size=10):
        if self.fetch == FetchOptions.FETCH_ONE:
            curr.fetchone()
        elif self.fetch == FetchOptions.FETCH_MANY:
            curr.fetchMany(size)
        elif self.fetch == FetchOptions.FETCH_ALL:
            curr.fetchall()
        else:
            raise InvalidQueryFetchOption(self.fetch)


class Psql:
    def __init__(self, h, n, u, p):
        self.__DB_HOST = h
        self.__DB_NAME = n
        self.__DB_USER = u
        self.__DB_PASSWORD = p
        self.queries = []
        self.conn = None

    def close(self):
        if self.conn is not None:
            self.conn.close()
            print('Database connection closed.')

    @contextlib.contextmanager
    def connect(self):
        print('Connecting to the PostgreSQL database...')

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(
            host=self.__DB_HOST,
            database=self.__DB_NAME,
            user=self.__DB_USER,
            password=self.__DB_PASSWORD)

        # create a cursor
        cur = conn.cursor()
        try:
            yield cur
        finally:
            # Teardown script
            cur.close()
            conn.close()
            print("Database connection closed.")

    def execute(self, q: Query, print_res=False):
        with self.connect() as cur:
            cur.execute(q.sql, q.params)
            q.execute(cur)

    # def executeBatch(self): @todo setup better context management for batch queries
    #     with self.connect() as cur:
    #         for q in self.queries:
    #             cur.execute(q.sql, q.params)
    #             q.fetch(cur)
    #
    #
