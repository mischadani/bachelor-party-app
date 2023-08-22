import os
from psycopg_pool import ConnectionPool

pool = ConnectionPool(conninfo=os.environ["postgresql://bach_party_user:bach_party_$@db/bach_party"])
