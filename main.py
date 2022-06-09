from asyncpg.connection import Connection
from fastapi import FastAPI, HTTPException
from fastapi.params import Depends
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi_asyncpg import configure_asyncpg

from models import (
    Analytics, Auth, Axis, Card, Chart,
    DataLabels, Options, Serie
)
from config import analytics
import config
import json
from web_app_check import check_webapp_signature

app = FastAPI()
db = configure_asyncpg(app, config.DATABASE_URL)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/web", StaticFiles(directory="web"), name="static")


def generate_cards(cards_data):
    return [
        Card(name=name, icon=analytics[name]['icon'],
             value=cards_data[name])
        for name in cards_data
    ]


def generate_charts(charts_data):
    return [
        Chart(
            name=name, type=analytics[name]['chart_type'],
            options=Options(xaxis=Axis(
                type=analytics[name]['options_xaxis_type'],
                categories=[i['category'] for i in charts_data[name]]
            ), dataLabels=DataLabels(enabled=False)),
            series=[Serie(
                name=name,
                data=[i['count'] for i in charts_data[name]]
            )]
        )
        for name in charts_data
    ]


@app.post("/data")
async def get_data(auth: Auth, con: Connection = Depends(db.connection)):
    user_data = check_webapp_signature(config.TOKEN, auth.initData)
    if not user_data:
        raise HTTPException(status_code=401, detail="Unauthorized")

    user_data["user"] = json.loads(user_data["user"])
    if user_data["user"]["id"] not in config.ADMINS:
        raise HTTPException(status_code=401, detail="Unauthorized")

    cards_data = {
        name: await con.fetchval(config.sql[name])
        for name in analytics.sections()
        if analytics[name]['type'] == 'card'
    }
    cards = generate_cards(cards_data)

    charts_data = {
        name: await con.fetch(config.sql[name])
        for name in analytics.sections()
        if analytics[name]['type'] == 'chart'
    }
    charts = generate_charts(charts_data)

    return Analytics(
        cards=cards,
        charts=charts
    )

@db.on_init
async def initialization(conn):
    await conn.execute('SELECT 1')

