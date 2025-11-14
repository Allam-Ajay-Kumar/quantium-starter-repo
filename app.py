import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Load your cleaned data
df = pd.read_csv("output/pink_morsel_sales.csv")

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Sort by date
df = df.sort_values("date")

# Line chart
fig = px.line(
    df,
    x="date",
    y="sales",
    title="Daily Sales of Pink Morsels",
    labels={"date": "Date", "sales": "Total Sales ($)"}
)

# Initialize app
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(
        children="Pink Morsel Sales Visualiser",
        style={"textAlign": "center"}
    ),
    
    dcc.Graph(
        id="sales-graph",
        figure=fig
    )
])

if __name__ == "__main__":
    app.run(debug=True)
