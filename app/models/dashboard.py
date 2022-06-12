from pydantic import BaseModel
from typing import List, Optional


class Card(BaseModel):
    name: str
    value: int
    icon: str
    has_data_table: Optional[bool] = False


class Axis(BaseModel):
    type: str
    categories: List


class DataLabels(BaseModel):
    enabled: bool


class Options(BaseModel):
    xaxis: Axis
    dataLabels: DataLabels


class Serie(BaseModel):
    name: Optional[str] = None
    data: List


class Chart(BaseModel):
    name: str
    type: str
    options: Options
    series: List[Serie]


class Analitics(BaseModel):
    cards: List[Card]
    charts: List[Chart]

