import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import plotly.plotly as py
import plotly.figure_factory as ff
import plotly
import seaborn as sns


# set plotly credentials
plotly_APIKEY = 'wD6IQCGUH31C3PQUWOBx'
plotly.tools.set_credentials_file(username='connorfarley', api_key='wD6IQCGUH31C3PQUWOBx')

# read in the data
df = pd.read_csv('fatal_US_crashes.csv', encoding='latin-1', index_col='Event_Date') # read in the data, set the index
df.index = pd.to_datetime(df.index) # make index a datetime index


#convert numeric columns to numeric values (i.e. not strings)
df['Number_of_Engines'] = pd.to_numeric(df['Number_of_Engines'], errors='coerce')

#Eliminate non-US localities; only interested in US
df.dropna(subset=['County_FIPS'], inplace=True)
df.dropna(subset=['State_FIPS'], inplace=True)

fips_columns = ['State_FIPS', 'County_FIPS']
injury_columns = ['Total_Serious_Injuries','Total_Minor_Injuries','Total_Uninjured']

for column in fips_columns:
    df[column] = df[column].astype(dtype=int) #convert strings to int values

for column in injury_columns:
    df[column] = pd.to_numeric(df[column], errors='coerce')
    df[column] = df[column].fillna(value=0)


df_all = df

df_all['State_FIPS'] = df_all['State_FIPS'].apply(lambda x: str(x).zfill(2))
df_all['County_FIPS'] = df_all['County_FIPS'].apply(lambda x: str(x).zfill(3))
df_all['FIPS'] = df_all['State_FIPS'] + df_all['County_FIPS']

sums = df_all.groupby(['FIPS'])[['Total_Fatal_Injuries']].sum()

a = []

for b in sums['Total_Fatal_Injuries']:
    a.append(b)

colorscale = ["#f7fbff","#ebf3fb","#deebf7","#d2e3f3","#c6dbef","#b3d2e9","#9ecae1",
              "#85bcdb","#6baed6","#57a0ce","#4292c6","#3082be","#2171b5","#1361a9",
              "#08519c","#0b4083","#08306b"]

endpts = list(np.linspace(1, 100, len(colorscale) - 1))
fips = df_all.groupby(['FIPS'])[['Total_Fatal_Injuries']].sum().index.tolist()
values = a

fig = ff.create_choropleth(
    fips=fips,
    values=values,
    scope=['usa'],
    binning_endpoints=endpts,
    colorscale=colorscale,
    show_state_data=False,
    round_legend_values=True,
    show_hover=True,
    centroid_marker={'opacity': .5},
    asp=2.9,
    title='US By Aviation Fatalities since 1982',
    legend_title='# of Fatalities'
    )
py.plot(fig, filename='choropleth_usa')

"""
#---------------------------------------------------------------------------------------------------------------------#

df_plane = df[df['Aircraft_Category']==' Airplane ']

df_plane['State_FIPS'] = df_plane['State_FIPS'].apply(lambda x: str(x).zfill(2))
df_plane['County_FIPS'] = df_plane['County_FIPS'].apply(lambda x: str(x).zfill(3))
df_plane['FIPS'] = df_plane['State_FIPS'] + df_plane['County_FIPS']

sums = df_plane.groupby(['FIPS'])[['Total_Fatal_Injuries']].sum()

c = []

for d in sums['Total_Fatal_Injuries']:
    c.append(d)


colorscale = ["#f7fbff","#ebf3fb","#deebf7","#d2e3f3","#c6dbef","#b3d2e9","#9ecae1",
              "#85bcdb","#6baed6","#57a0ce","#4292c6","#3082be","#2171b5","#1361a9",
              "#08519c","#0b4083","#08306b"]

endpts = list(np.linspace(1, 100, len(colorscale) - 1))
fips = df_plane.groupby(['FIPS'])[['Total_Fatal_Injuries']].sum().index.tolist()
values = c

fig = ff.create_choropleth(
    fips=fips, values=values, scope=['usa'],
    binning_endpoints=endpts, colorscale=colorscale,
    show_state_data=False,
    show_hover=True, centroid_marker={'opacity': 0},
    asp=2.9, title='US Counties By Airplane Fatalities since 1982',
    legend_title='# of Fatalities'
)
py.plot(fig, filename='choropleth_plane')

#---------------------------------------------------------------------------------------------------------------------#

df_heli = df[df['Aircraft_Category']==' Helicopter ']

df_heli['State_FIPS'] = df_heli['State_FIPS'].apply(lambda x: str(x).zfill(2))
df_heli['County_FIPS'] = df_heli['County_FIPS'].apply(lambda x: str(x).zfill(3))
df_heli['FIPS'] = df_heli['State_FIPS'] + df_heli['County_FIPS']

sums = df_heli.groupby(['FIPS'])[['Total_Fatal_Injuries']].sum()

e = []

for f in sums['Total_Fatal_Injuries']:
    e.append(f)


colorscale = ["#f7fbff","#ebf3fb","#deebf7","#d2e3f3","#c6dbef","#b3d2e9","#9ecae1",
              "#85bcdb","#6baed6","#57a0ce","#4292c6","#3082be","#2171b5","#1361a9",
              "#08519c","#0b4083","#08306b"]

endpts = list(np.linspace(1, 12, len(colorscale) - 1))
fips = df_heli.groupby(['FIPS'])[['Total_Fatal_Injuries']].sum().index.tolist()
values = e

fig = ff.create_choropleth(
    fips=fips, values=values, scope=['usa'],
    binning_endpoints=endpts, colorscale=colorscale,
    show_state_data=False,
    show_hover=True, centroid_marker={'opacity': 0},
    asp=2.9, title='US Counties By Helicopter Fatalities since 1982',
    legend_title='# of Fatalities'
)
py.plot(fig, filename='choropleth_heli')

#---------------------------------------------------------------------------------------------------------------------#


df_balloon = df[df['Aircraft_Category']==' Balloon ']

df_balloon['State_FIPS'] = df_balloon['State_FIPS'].apply(lambda x: str(x).zfill(2))
df_balloon['County_FIPS'] = df_balloon['County_FIPS'].apply(lambda x: str(x).zfill(3))
df_balloon['FIPS'] = df_balloon['State_FIPS'] + df_balloon['County_FIPS']

sums = df_balloon.groupby(['FIPS'])[['Total_Fatal_Injuries']].sum()

g = []

for h in sums['Total_Fatal_Injuries']:
    g.append(h)


colorscale = ["#f7fbff","#ebf3fb","#deebf7","#d2e3f3","#c6dbef","#b3d2e9","#9ecae1",
              "#85bcdb","#6baed6","#57a0ce","#4292c6","#3082be","#2171b5","#1361a9",
              "#08519c","#0b4083","#08306b"]

endpts = list(np.linspace(1, 12, len(colorscale) - 1))
fips = df_balloon.groupby(['FIPS'])[['Total_Fatal_Injuries']].sum().index.tolist()
values = g

fig = ff.create_choropleth(
    fips=fips, values=values, scope=['usa'],
    binning_endpoints=endpts, colorscale=colorscale,
    show_state_data=False,
    show_hover=True, centroid_marker={'opacity': 0},
    asp=2.9, title='US Counties By Balloon Fatalities since 1982',
    legend_title='# of Fatalities'
)
py.plot(fig, filename='choropleth_balloon')
"""