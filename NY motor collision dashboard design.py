import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import folium
import numpy as np
import pandas as pd
from datetime import datetime
import plotly
from plotly import tools

data_2013 = pd.read_csv('NY collisions 2013 data')
data_2014 = pd.read_csv('NY collisions 2014 data')
data_2015 = pd.read_csv('NY collisions 2015 data')
data_2016 = pd.read_csv('NY collisions 2016 data')


years = [2013, 2014, 2015, 2016]
all_data = [data_2013, data_2014, data_2015, data_2016]
boroughs = ['Manhattan', 'Brooklyn', 'Queens', 'Bronx', 'Staten Island']

app = dash.Dash()

app.layout = html.Div([
                       html.H1(children = 'NY boroughs vehicle collision data for 2013-2016',
                               style={'textAlign': 'center'}),
                        
                        html.Div([
                        html.H2('Persons injured'),
                        html.Label('Year'),
                        dcc.Dropdown(id = 'Select Year',
                        options = [{'label': 2013, 'value' : 2013},
                                    {'label': 2014, 'value' : 2014},
                                    {'label': 2015, 'value' : 2015},
                                    {'label': 2016, 'value' : 2016}],
                                    value = 2013, style={'width': '48%'}),
                        dcc.Graph(id = 'yearly_graph'),

                        html.H2('Monthly and Yearly collision trends'),
                        html.Label('Year'),
                        dcc.Dropdown(id = 'Year selection',
                        options = [{'label': 2013, 'value' : 2013},
                                   {'label': 2014, 'value' : 2014},
                                    {'label': 2015, 'value' : 2015},
                                    {'label': 2016, 'value' : 2016}],
                                     value = 2013, style={'width': '48%'}),
                        dcc.RadioItems(id = 'Pick Category',
                        options = [
                                    {'label': 'Daily', 'value': 'Daily'},
                                    {'label': 'Monthly', 'value': 'Monthly'}
                                    ], value = 'Monthly',  style={'width': '48%'}),
                        dcc.Graph(id = 'Time_graph')]),

                        html.Div([
                        html.H2('Breakdown of Injuries data'),
                        html.Label('Year'),
                        dcc.Dropdown(id = 'Year selected',
                        options = [{'label': 2013, 'value' : 2013},
                                   {'label': 2014, 'value' : 2014},
                                    {'label': 2015, 'value' : 2015},
                                    {'label': 2016, 'value' : 2016}],
                                    value = 2013,  style={'width': '48%'}),
                        html.Label('Select Category'),
                        dcc.RadioItems(id = 'Select Category',
                        options = [
                                    {'label': 'Pedestrian', 'value': 'Pedestrian'},
                                    {'label': 'Cyclist', 'value': 'Cyclist'},
                                    {'label': 'Motorist', 'value': 'Motorist'}],
                                    value = 'Pedestrian', style={'width': '48%'}),
                        dcc.Graph(id = 'Category_graph')]),                       
                       
                        html.H2('Street intersections with highest number of collisions'),
                        html.Label('Year'),
                        dcc.Dropdown(id = 'Select a Year',
                        options = [{'label': 2013, 'value' : 2013},
                                   {'label': 2014, 'value' : 2014},
                                    {'label': 2015, 'value' : 2015},
                                    {'label': 2016, 'value' : 2016}
                                    ],
                                    value = 2013,  style={'width': '48%'}),
                                                
                        html.Iframe(id = 'map', srcDoc = open('location_map.html', 'r').read(), width = '70%', height = '500'),
                        
], style = {'columnCount': 2})

        
@app.callback(
    Output('yearly_graph', 'figure'),
    [Input('Select Year', 'value')])

def update_graph(year):
    data_2013 = pd.read_csv('NY collisions 2013 data')
    data_2014 = pd.read_csv('NY collisions 2014 data')
    data_2015 = pd.read_csv('NY collisions 2015 data')
    data_2016 = pd.read_csv('NY collisions 2016 data')

    manhattan_pop = 1664727
    brooklyn_pop = 2648771
    queens_pop = 2358582
    bronx_pop = 1471160
    statenisland_pop = 479458

    all_data = {2013: data_2013, 2014: data_2014, 2015:data_2015, 2016: data_2016}
    current_data = all_data[year]

    manhattan = current_data[current_data['UPDATED BOROUGH'] == 'MANHATTAN']
    brooklyn = current_data[current_data['UPDATED BOROUGH'] == 'BROOKLYN']
    queens = current_data[current_data['UPDATED BOROUGH'] == 'QUEENS']
    bronx = current_data[current_data['UPDATED BOROUGH'] == 'BRONX']
    staten_island = current_data[current_data['UPDATED BOROUGH'] == 'STATEN ISLAND']

    boroughs = ['Manhattan', 'Brooklyn', 'Queens', 'Bronx', 'Staten Island']

    trace1 = go.Bar(y = boroughs, x = [manhattan['NUMBER OF PERSONS INJURED'].sum(),
                                       brooklyn['NUMBER OF PERSONS INJURED'].sum(),
                                       queens['NUMBER OF PERSONS INJURED'].sum(),
                                       bronx['NUMBER OF PERSONS INJURED'].sum(),
                                       staten_island['NUMBER OF PERSONS INJURED'].sum()], orientation = 'h',
                                       marker = dict(color = ['rgba(171, 50, 96, 0.6)', 'rgba(63, 72, 204, 0.6)',
                                                              'rgba(16, 112, 2, 0.8)', 'rgba(80, 26, 80, 0.8)', 'rgba(255, 128, 2, 0.8)'])
                                       )

    trace2 = go.Bar(y = boroughs, x = [manhattan['NUMBER OF PERSONS INJURED'].sum()/manhattan_pop,
                                       brooklyn['NUMBER OF PERSONS INJURED'].sum()/brooklyn_pop,
                                       queens['NUMBER OF PERSONS INJURED'].sum()/queens_pop,
                                       bronx['NUMBER OF PERSONS INJURED'].sum()/bronx_pop,
                                       staten_island['NUMBER OF PERSONS INJURED'].sum()/statenisland_pop], orientation = 'h',
                                       marker = dict(color = ['rgba(171, 50, 96, 0.6)', 'rgba(63, 72, 204, 0.6)',
                                                              'rgba(16, 112, 2, 0.8)', 'rgba(80, 26, 80, 0.8)', 'rgba(255, 128, 2, 0.8)'])
                                       )


    
    fig = tools.make_subplots(rows=1, cols=2)
    fig.append_trace(trace1, 1, 1)
    fig.append_trace(trace2, 1, 2)
    layout = fig['layout'].update(height=500, width=900, title='Total injuries (left) and per capita injuries (right) in NY boroughs for {}'.format(year),
                                  showlegend = False)

    return {'data': fig, 'layout': layout}
    
    
@app.callback(
    Output('Category_graph', 'figure'),
    [Input('Year selected', 'value'), Input('Select Category', 'value')])

def cat_injury(year, category):
    data_2013 = pd.read_csv('NY collisions 2013 data')
    data_2014 = pd.read_csv('NY collisions 2014 data')
    data_2015 = pd.read_csv('NY collisions 2015 data')
    data_2016 = pd.read_csv('NY collisions 2016 data')

    all_data = {2013: data_2013, 2014: data_2014, 2015:data_2015, 2016: data_2016}
    current_data = all_data[year]

    manhattan = current_data[current_data['UPDATED BOROUGH'] == 'MANHATTAN']
    brooklyn = current_data[current_data['UPDATED BOROUGH'] == 'BROOKLYN']
    queens = current_data[current_data['UPDATED BOROUGH'] == 'QUEENS']
    bronx = current_data[current_data['UPDATED BOROUGH'] == 'BRONX']
    staten_island = current_data[current_data['UPDATED BOROUGH'] == 'STATEN ISLAND']

    if category == 'Pedestrian':
        boroughs = ['Manhattan', 'Brooklyn', 'Queens', 'Bronx', 'Staten Island']
        trace1 = go.Bar(y = boroughs, x = [manhattan['NUMBER OF PEDESTRIANS INJURED'].sum(),
                                       brooklyn['NUMBER OF PEDESTRIANS INJURED'].sum(),
                                       queens['NUMBER OF PEDESTRIANS INJURED'].sum(),
                                       bronx['NUMBER OF PEDESTRIANS INJURED'].sum(),
                                       staten_island['NUMBER OF PEDESTRIANS INJURED'].sum()],
                                       marker = dict(color = ['rgba(171, 50, 96, 0.6)', 'rgba(63, 72, 204, 0.6)',
                                                              'rgba(16, 112, 2, 0.8)', 'rgba(80, 26, 80, 0.8)', 'rgba(255, 128, 2, 0.8)']),
                                       orientation = 'h')

        return {'data': [trace1], 'layout': go.Layout(title = 'Pedestrian injuries in NY boroughs for {}'.format(year), height=500, width=900)}
    elif category == 'Cyclist':
        boroughs = ['Manhattan', 'Brooklyn', 'Queens', 'Bronx', 'Staten Island']
        trace1 = go.Bar(y = boroughs, x = [manhattan['NUMBER OF CYCLIST INJURED'].sum(),
                                       brooklyn['NUMBER OF CYCLIST INJURED'].sum(),
                                       queens['NUMBER OF CYCLIST INJURED'].sum(),
                                       bronx['NUMBER OF CYCLIST INJURED'].sum(),
                                       staten_island['NUMBER OF CYCLIST INJURED'].sum()],
                                       marker = dict(color = ['rgba(171, 50, 96, 0.6)', 'rgba(63, 72, 204, 0.6)',
                                                              'rgba(16, 112, 2, 0.8)', 'rgba(80, 26, 80, 0.8)', 'rgba(255, 128, 2, 0.8)']),
                                        orientation = 'h')

        return {'data': [trace1], 'layout': go.Layout(title = 'Cyclist injuries in NY boroughs for {}'.format(year), height=500, width=900)}
    else:
        boroughs = ['Manhattan', 'Brooklyn', 'Queens', 'Bronx', 'Staten Island']
        trace1 = go.Bar(y = boroughs, x = [manhattan['NUMBER OF MOTORIST INJURED'].sum(),
                                       brooklyn['NUMBER OF MOTORIST INJURED'].sum(),
                                       queens['NUMBER OF MOTORIST INJURED'].sum(),
                                       bronx['NUMBER OF MOTORIST INJURED'].sum(),
                                       staten_island['NUMBER OF MOTORIST INJURED'].sum()],
                                       marker = dict(color = ['rgba(171, 50, 96, 0.6)', 'rgba(63, 72, 204, 0.6)',
                                                              'rgba(16, 112, 2, 0.8)', 'rgba(80, 26, 80, 0.8)', 'rgba(255, 128, 2, 0.8)']),
                                       orientation = 'h')

        return {'data': [trace1],'layout': go.Layout(title = 'Motorist injuries in NY boroughs for {}'.format(year), height=500, width=900)}


@app.callback(
    Output('Time_graph', 'figure'),
    [Input('Year selection', 'value'), Input('Pick Category', 'value')])



def time_cat(year, category):
    all_data = {2013: data_2013, 2014: data_2014, 2015:data_2015, 2016: data_2016}
    current_data = all_data[year]

    if category == 'Daily':
        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        data = current_data['DAY'].value_counts().sort_index()
        trace1 = go.Scatter(x = days, y = data, line=dict(color='rgb(63, 72, 204)'))

        return {'data': [trace1],'layout': go.Layout(title = 'Daily distribution of collisions in NY boroughs for {}'.format(year))}
            
    else:
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        data = current_data['MONTH'].value_counts().sort_index()
        trace1 = go.Scatter(x = months, y = data, line=dict(color='rgb(63, 72, 204)'))

        return {'data': [trace1],'layout': go.Layout(title = 'Monthly distribution of collisions in NY boroughs for {}'.format(year), height = 500, width = 900)}


@app.callback(
    Output('map', 'srcDoc'),
    [Input('Select a Year', 'value')])

def nyc_map(year):
    NY_COORDINATES = (40.730610, -73.935242)
    ny_map = folium.Map(location=NY_COORDINATES, zoom_start=12)

    def map_locations():
        all_data = {2013: data_2013, 2014: data_2014, 2015:data_2015, 2016: data_2016}
    
        current_data = all_data[year]
        on = current_data.groupby(['ON STREET NAME', 'CROSS STREET NAME']).count().sort_values('ZIP CODE', ascending = False).head().index.get_level_values(0)
        cross = current_data.groupby(['ON STREET NAME', 'CROSS STREET NAME']).count().sort_values('ZIP CODE', ascending = False).head().index.get_level_values(1)

        lats = []
        longs = []
        for i in range(0,5):
            lat = current_data[(current_data['ON STREET NAME'] == on[i]) & (current_data['CROSS STREET NAME'] == cross[i])].mean()['LATITUDE']
            long = current_data[(current_data['ON STREET NAME'] == on[i]) & (current_data['CROSS STREET NAME'] == cross[i])].mean()['LONGITUDE']
            lats.append(lat)
            longs.append(long)
        

        text_on = [item.rstrip() for item in on]
        text_cross = [item.rstrip() for item in cross]
        all_text = [text_on[i] + ' & ' + text_cross[i] for i in range(0, 5)]

        d = {'Latitude': lats, 'Longitude': longs, 'name': all_text}
        mydata = pd.DataFrame(d)

        for i in range(0, 5):
            folium.Marker(location = [mydata.iloc[i]['Latitude'],mydata.iloc[i]['Longitude'] ], popup = mydata.iloc[i]['name']).add_to(ny_map)

        return ny_map
    location_map = map_locations()

    location_map.save('location_map.html')
    return open('location_map.html', 'r').read()
    
           
if __name__ == '__main__':
    app.run_server(debug=True)  
