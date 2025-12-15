import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# Load processed data
df = pd.read_csv("processed_sales.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Sort by date
df = df.sort_values("Date")

# Create line chart
fig = px.line(
    df,
    x="Date",
    y="Sales",
    color="Region",
    title="Pink Morsel Sales Over Time",
    labels={
        "Date": "Date",
        "Sales": "Total Sales"
    }
)

# Add vertical line for price increase date
fig.add_vline(
     x=pd.to_datetime("2021-01-15"),
    line_dash="dash",
    line_color="red"
)

# Create Dash app
app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(
            "Soul Foods – Pink Morsel Sales Visualiser",
            style={"textAlign": "center"}
        ),

        dcc.Graph(figure=fig)
    ]
)

if __name__ == "__main__":
    app.run(debug=True)
