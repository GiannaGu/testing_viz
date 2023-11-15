import plotly.graph_objects as go

import pandas as pd

df = pd.read_csv('https://github.com/marestaing/hosting/blob/main/visited_states.csv?raw=true')

fig = go.Figure(data=go.Choropleth(
    locations=df['code'], # Spatial coordinates
    z = df['number students'].astype(float), # Data to be color-coded
    locationmode = 'USA-states', # set of locations match entries in `locations`
    colorscale = 'tropic',
    colorbar_title = "More people have visited",
))

fig.update_layout(
    title_text = 'How Many Kids in App Academy have visited Certain States',
    geo_scope='usa', # limite map scope to USA
)

fig.show()