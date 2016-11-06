import plotly 

plotly.tools.set_credentials_file(username='theCreedo', api_key='r7ucea0gce')

import plotly.plotly as py
import plotly.graph_objs as go

data = [go.Bar(x=['Anger', 'Disgust', 'Joy', 'Fear', 'Sadness'],y=[20, 14, 23, 5, 12] )]

py.iplot(data, filename='basic-bar')