from typing import List, Literal, Optional
from pydantic import BaseModel


class Header(BaseModel):
    text: str
    value: str
    align: str = 'start'
    sortable: bool = False


class DataTable(BaseModel):
    pagination_sql_file: str
    headers: List[Header]
    default_sort_column: str


class Card(BaseModel):
    name: str
    sql_file: str
    icon: str
    data_table: Optional[DataTable] = None


class Chart(BaseModel):
    name: str
    sql_file: str
    chart_type: Literal[
        'line', 'area', 'bar', 'pie',
        'donut', 'scatter', 'bubble',
        'heatmap', 'radialBar', 'candlestick'
    ]
    options_xaxis_type: Literal['category', 'datetime', 'numeric']
    data_labels: bool = False


class Config(BaseModel):
    cards: List[Card] = []
    charts: List[Chart] = []

