from asyncpg.connection import Connection
from fastapi import APIRouter
from fastapi.param_functions import Depends

from app.db import db
from app.config.config import cards_sql_queries, charts_sql_queries
from app.utils.generate_analytics import generate_cards, generate_charts
from app.models.dashboard import Analitics

router = APIRouter(prefix="/dashboard")


@router.get("/")
async def get_data(con: Connection = Depends(db.connection)) -> Analitics:
    cards_data = {
        name: await con.fetchval(query)
        for name, query in cards_sql_queries.items()
    }
    cards = generate_cards(cards_data)

    charts_data = {
        name: await con.fetch(query)
        for name, query in charts_sql_queries.items()
    }
    charts = generate_charts(charts_data)

    return Analitics(
        cards=cards,
        charts=charts
    )
