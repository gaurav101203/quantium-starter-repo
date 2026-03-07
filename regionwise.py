import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

DATA_PATH = "./data/combined.csv"

data = pd.read_csv(DATA_PATH)
data = data.sort_values(by="date")

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Visualizer"),
    dcc.RadioItems(
        id="region-selector",
        options=[{"label":"All","value":"All"}] + [
            {"label": r, "value": r} for r in data["region"].unique()
        ],
        value=data["region"].unique()[0],  # default region
        inline=True
    ),
    dcc.Graph(id="sales-chart")
])

@app.callback(
    Output("sales-chart", "figure"),
    Input("region-selector", "value")
)
def update_chart(selected_region):
    if selected_region == "All":
        filtered = data
        fig = px.line(filtered, x="date", y="sales", color="region",
                      title="Sales in All Regions")
    else:
        filtered = data[data["region"] == selected_region]
        fig = px.line(filtered, x="date", y="sales",
                      title=f"Sales in {selected_region}")
    return fig

if __name__ == "__main__":
    app.run(debug=True)