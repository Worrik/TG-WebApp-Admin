from typing import Optional
from asyncpg.connection import Connection
from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Depends

from app.db import db
from app.config.config import data_tables_sql_queries, cards_sql_queries, cards
from app.models.data_table import DataTable

router = APIRouter(prefix="/data-table")

@router.get("/{name}")
async def get_data(
        name: str,
        page: int = 1,
        per_page: int = 10,
        sort_by: Optional[str] = None,
        desc: bool = False,
        con: Connection = Depends(db.connection)
):
    data_tables = [card.data_table for card in cards if card.name == name]
    data_table = data_tables[0] if data_tables else None

    if not data_table:
        raise HTTPException(status_code=404, detail="Data table not found")

    totalItems = await con.fetchval(cards_sql_queries[name])

    if per_page < 0:
        per_page = totalItems or 0

    order_by = (
        f"{sort_by or data_table.default_sort_column} "
        f"{'DESC' if desc else 'ASC'}",
    )

    data = await con.fetch(
        data_tables_sql_queries[name] % order_by,
        per_page, (page-1) * per_page,
    )

    if not data:
        raise HTTPException(status_code=404, detail="Is empty")

    return DataTable(
        totalItems=totalItems,
        items=data,
        headers=data_table.headers
    )

