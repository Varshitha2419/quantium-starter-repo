from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

print("Starting Dash app...")

df = pd.read_csv("processed_sales.csv")
df["Date"] = pd.to_datetime(df["Date"])

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Soul Foods – Pink Morsel Sales Visualiser"),

    dcc.RadioItems(
        id="region",
        options=[
            {"label": "All", "value": "all"},
            {"label": "North", "value": "north"},
            {"label": "East", "value": "east"},
            {"label": "South", "value": "south"},
            {"label": "West", "value": "west"},
        ],
        value="all",
        inline=True
    ),

    dcc.Graph(id="graph")
])

@app.callback(
    Output("graph", "figure"),
    Input("region", "value")
)
def update(region):
    if region == "all":
        dff = df
    else:
        dff = df[df["Region"].str.lower() == region]

    fig = px.line(dff, x="Date", y="Sales", color="Region")
    return fig

if __name__ == "__main__":
    app.run(debug=True)
