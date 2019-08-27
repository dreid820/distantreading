import pandas as pd
import plotly.plotly as py
from plotly.graph_objs import *
import plotly.graph_objs as go

py.sign_in('DarrenReid', 'jpQpwEdZELDOTBgpr5tI')

df = pd.read_csv(r"E:\spreadsheet.csv")



tracepeace = go.Bar(
    x = df.Year,
    y = df.Peaceful,
    name = 'Peaceful',
    text = 'Peaceful',
    textposition = 'auto'
)


traceurban = go.Bar(
    x = df.Year,
    y = df.Urban,
    name = 'Urban',
    text = 'Urban',
    textposition = 'auto'
)

traceinstitution = go.Bar(
    x = df.Year,
    y = df.Institutions,
    name = 'Institutions',
    text = 'Institutions',
    textposition = 'auto'
)

tracetech = go.Bar(
    x = df.Year,
    y = df.Technology,
    name = 'Technology',
    text = 'Technology',
    textposition = 'auto'
)

tracetemperance = go.Bar(
    x = df.Year,
    y = df.Temperance,
    name = 'Temperance',
    text = 'Temperance',
    textposition = 'auto'
)

tracecleanliness = go.Bar(
    x = df.Year,
    y = df.Cleanliness,
    name = 'Cleanliness',
    text = 'Cleanliness',
    textposition = 'auto'
)

traceruleoflaw = go.Bar(
    x = df.Year,
    y = df.Rule_of_Law,
    name = 'Rule of Law',
    text = 'Rule of Law',
    textposition = 'auto'
)

tracehonest = go.Bar(
    x = df.Year,
    y = df.Honest,
    name = 'Honest',
    text = 'Honesty',
    textposition = 'auto'
)

traceliberty = go.Bar(
    x = df.Year,
    y = df.Liberty,
    name = 'Liberty',
    text = 'Liberty',
    textposition = 'auto'
)

traceclothed = go.Bar(
    x = df.Year,
    y = df.Clothed,
    name = 'Clothed',
    text = 'Clothing',
    textposition = 'auto'
)

tracespirituality = go.Bar(
    x = df.Year,
    y = df.Spirituality,
    name = 'Spirituality',
    text = 'Spirituality',
    textposition = 'auto'
)

traceagriculture = go.Bar(
    x = df.Year,
    y = df.Agriculture,
    name = 'Agriculture',
    text = 'Agriculture',
    textposition = 'auto'
)

tracemonog = go.Bar(
    x = df.Year,
    y = df.Monogamy,
    name = 'Monogamy',
    text = 'Monogamy',
    textposition = 'auto'
)

traceindustry = go.Bar(
    x = df.Year,
    y = df.Industry,
    name = 'Industry',
    text = 'Industry',
    textposition = 'auto'
)

traceart = go.Bar(
    x = df.Year,
    y = df.Art,
    name = 'Art',
    text = 'Art',
    textposition = 'auto'
)

traceeducated = go.Bar(
    x = df.Year,
    y = df.Educated,
    name = 'Educated',
    text = 'Education',
    textposition = 'auto'
)

traceactive = go.Bar(
    x = df.Year,
    y = df.Active,
    name = 'Active',
    text = 'Active',
    textposition = 'auto'
)

tracecommerce = go.Bar(
    x = df.Year,
    y = df.Commerce,
    name = 'Commerce',
    text = 'Commerce',
    textposition = 'auto'
)

tracemanners = go.Bar(
    x = df.Year,
    y = df.Manners,
    name = 'Manners',
    text = 'Manners',
    textposition = 'auto'
)
data = [tracepeace, traceurban, traceinstitution, tracetech, tracetemperance, tracecleanliness, tracemanners, tracecommerce, traceactive, traceeducated, traceart, traceindustry, tracemonog, traceagriculture, tracespirituality, traceclothed, traceliberty, tracehonest, traceruleoflaw]
layout = go.Layout(
    barmode='stack'
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='stacked-bar')

py.image.save_as(fig, filename='stacked_bar_plot.png')

from IPython.display import Image
Image('stacked_bar_plot.png')

