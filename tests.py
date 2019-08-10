# imports of your dash app
import dash
import dash_html_components as html

def test_app_layout(dash_duo):
    # define app inside the test function
    app = dash.Dash(__name__)
    app.layout = html.Div([
        html.H1("Gapminder Bubble Chart: GDP/Income vs Life Expectancy")
    ])

    # host the app locally in a thread, all dash server configs could be
    # passed after the first app argument
    dash_duo.start_server(app)

    # test for element text:
    assert dash_duo.wait_for_element("h1").text == "Gapminder Bubble Chart: GDP/Income vs Life Expectancy"