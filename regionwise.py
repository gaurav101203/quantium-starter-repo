import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

DATA_PATH = "./data/combined.csv"

data = pd.read_csv(DATA_PATH)
data = data.sort_values(by="date")

# Dash instance
dash_app = Dash(__name__)

dash_app.layout = html.Div([
    
    # Header
    html.H1(
        "Pink Morsel Visualizer",
        id="header"
    ),

    # Region Picker
    dcc.RadioItems(
        id="region-picker",
        options=[{"label": "All", "value": "All"}] + [
            {"label": r, "value": r} for r in data["region"].unique()
        ],
        value="All",
        inline=True
    ),

    # Visualization
    dcc.Graph(id="visualization")
])

@dash_app.callback(
    Output("visualization", "figure"),
    Input("region-picker", "value")
)
def update_chart(selected_region):

    if selected_region == "All":
        filtered = data
        fig = px.line(
            filtered,
            x="date",
            y="sales",
            color="region",
            title="Sales in All Regions"
        )
    else:
        filtered = data[data["region"] == selected_region]
        fig = px.line(
            filtered,
            x="date",
            y="sales",
            title=f"Sales in {selected_region}"
        )

    return fig


if __name__ == "__main__":
    dash_app.run(debug=True)