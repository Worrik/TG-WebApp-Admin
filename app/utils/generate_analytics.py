from app.models.dashboard import Card, Chart, Options, DataLabels, Axis, Serie
from app.config.config import cards, charts

def generate_cards(cards_data):
    return [
        Card(
            name=card.name,
            icon=card.icon,
            value=cards_data[card.name],
            has_data_table=bool(card.data_table)
        )
        for card in cards
    ]


def generate_charts(charts_data):
    return [
        Chart(
            name=chart.name, type=chart.chart_type,
            options=Options(xaxis=Axis(
                type=chart.options_xaxis_type,
                categories=[i['category'] for i in charts_data[chart.name]]
            ), dataLabels=DataLabels(enabled=False)),
            series=[Serie(
                name=chart.name,
                data=[i['count'] for i in charts_data[chart.name]]
            )]
        )
        for chart in charts
    ]
