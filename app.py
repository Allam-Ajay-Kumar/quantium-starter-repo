import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# Load cleaned data
df = pd.read_csv("output/pink_morsel_sales.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

app = dash.Dash(__name__)

# Layout
app.layout = html.Div(
    style={
        "fontFamily": "Arial",
        "backgroundColor": "#f4f6f8",
        "padding": "40px"
    },
    children=[
        html.H1(
            "Pink Morsel Sales Visualiser",
            style={
                "textAlign": "center",
                "color": "#2c3e50",
                "marginBottom": "30px",
                "fontSize": "40px"
            }
        ),

        html.Div(
            style={
                "width": "300px",
                "margin": "auto",
                "padding": "20px",
                "backgroundColor": "white",
                "borderRadius": "8px",
                "boxShadow": "0 0 12px rgba(0,0,0,0.1)"
            },
            children=[
                html.Label(
                    "Select Region:",
                    style={"fontWeight": "bold", "fontSize": "18px"}
                ),
                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    inputStyle={"marginRight": "10px"},
                    labelStyle={"display": "block", "margin": "8px 0"},
                    style={"marginTop": "10px", "fontSize": "16px"}
                ),
            ]
        ),

        html.Div(
            style={
                "width": "90%",
                "margin": "40px auto",
                "backgroundColor": "white",
                "padding": "20px",
                "borderRadius": "10px",
                "boxShadow": "0 0 12px rgba(0,0,0,0.1)"
            },
            children=[
                dcc.Graph(id="sales-graph")
            ]
        )
    ]
)

# Callback to update graph when region changes
@app.callback(
    Output("sales-graph", "figure"),
    Input("region-filter", "value")
)
def update_graph(selected_region):
    if selected_region == "all":
        filtered = df
    else:
        filtered = df[df["region"] == selected_region]

    fig = px.line(
        filtered,
        x="date",
        y="sales",
        title=f"Pink Morsel Sales ({selected_region.capitalize()})",
        labels={"date": "Date", "sales": "Sales ($)"}
    )

    fig.update_layout(
        plot_bgcolor="#fdfdfd",
        paper_bgcolor="#ffffff",
        title_x=0.5
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)
