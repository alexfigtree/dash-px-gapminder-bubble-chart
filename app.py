import plotly_express as px
import dash
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash(
    __name__, external_stylesheets=["https://codepen.io/chriddyp/pen/bWLwgP.css"]
)

def generate_bubble_chart():
    return px.scatter(
        px.data.gapminder(), 
        x="gdpPercap", 
        y="lifeExp", 
        animation_frame="year", 
        animation_group="country",
        size="pop", 
        color="country", 
        hover_name="country", 
        log_x = True, 
        size_max=45, 
        range_x=[100,100000], 
        range_y=[25,90]
    )

app.layout = html.Div([
    dcc.Graph(
        id='scatter',
        figure=generate_bubble_chart()
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)