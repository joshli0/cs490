import os
import psycopg2

con = psycopg2.connect(os.environ["DATABASE_URL"], sslmode="require")