from pydantic import BaseModel
from typing import List, Optional


class Auth(BaseModel):
    initData: str


class Card(BaseModel):
    name: str
    value: int
    icon: str


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


class Analytics(BaseModel):
    cards: List[Card]
    charts: List[Chart]

