import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd


file = pd.read_csv(filepath_or_buffer="./data/combined.csv")
# sample data
df = pd.DataFrame({
    "year": file["date"],
    "sales": file["sales"],
    "region": file["region"]
})

app = dash.Dash(__name__)

fig = px.line(df, x="year", y="sales")

app.layout = html.Div([
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)