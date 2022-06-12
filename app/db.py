from asyncpg.connection import Connection
from fastapi_asyncpg import configure_asyncpg

from app._app import app
from app.config.config import DATABASE_URL

db = configure_asyncpg(app, DATABASE_URL)


@db.on_init
async def initialization(con: Connection):
    await con.execute('SELECT 1')

