import json
from environs import Env

from app.models.config import Config

env = Env()
env.read_env()

DATABASE_URL = env.str("DATABASE_URL")
TOKEN = env.str("TOKEN")
ADMINS = env.list("ADMINS", subcast=int)

config = Config(**json.loads(open('config.json').read()))
cards = config.cards
charts = config.charts

cards_sql_queries = {
    card.name: open(card.sql_file).read()
    for card in cards
}

charts_sql_queries = {
    chart.name: open(chart.sql_file).read()
    for chart in charts
}

data_tables_sql_queries = {
    card.name: open(card.data_table.pagination_sql_file).read()
    for card in cards if card.data_table
}

