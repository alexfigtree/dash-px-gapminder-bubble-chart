# dash-plotly-gapminder-bubble chart
Income vs Life Expectancy by Country from 1952 to 2007

## To get started:
```
pip3 install plotly_express
pip3 install dash
```



## To start the app: 
```
python3 app.py 
```

On Google Chrome, navigate to http://127.0.0.1:8050/ or whatever port specified in your terminal

### Features: 
- Deselect/select specific countries by either clicking on their respective bubbles or on the list on the right.
- Use the Play button on the bottom to walk through each year and update the chart with the data for that year 


## Testing
```
pip3 install dash[testing]
```

Install web drivers for Google Chrome (see https://dash.plot.ly/testing), then: 

```
pytest tests.py
```

## To Do: 
- write more tests for dash_core_components
- convert small colored circles on right hand side list to checkboxes
