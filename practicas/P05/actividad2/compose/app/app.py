import os
import psycopg
from flask import Flask

app = Flask(__name__)

@app.get("/")
def index():
    with psycopg.connect(os.environ["DATABASE_URL"]) as conn:
        with conn.cursor() as cur:
            cur.execute("CREATE TABLE IF NOT EXISTS visitas (id serial PRIMARY KEY, fecha timestamptz DEFAULT now())")
            cur.execute("INSERT INTO visitas DEFAULT VALUES")
            cur.execute("SELECT count(*) FROM visitas")
            count = cur.fetchone()[0]
    return f"<h1>Equipo 8 - Sistemas Distribuidos</h1><p>Visitas registradas en PostgreSQL: {count}</p>"
