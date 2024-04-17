import csv
import plotly
from math import sqrt
import datetime
import plotly.express as px
import time
import pandas as pd
import plotly.graph_objects as go

cs = dict()
n2= 0
n = int(input())
#m = int(input())
df = pd.DataFrame({})

with open('data.txt') as f:
    reader = csv.DictReader(f, delimiter='\t')
    count = 0
    for line in reader:
        try:
            line['data_vibitiya'] = datetime.datetime.strptime(line['data_vibitiya'][6:], '%Y')
            if count > n:
                break
            count+=1
            n2 +=1
            if not((line['gospital'], line['data_vibitiya']) in cs.keys()):
                cs[(line['gospital'], line['data_vibitiya'])] = [line['shirota'], line['dolgota'], 1]
            else:
                cs[(line['gospital'], line['data_vibitiya'])][2] += 1
        except:
            print('')
        count +=1
    print([i[2] for i in cs.values()])

df = pd.DataFrame({'Hosp': [i[0] for i in cs.keys()], 'dt': [i[1] for i in cs.keys()], 'pop' :[int(i[2]) * 10 for i in cs.values()], 'pop1' :[int(i[2]) for i in cs.values()], 'lat' : [i[0] for i in cs.values()], 'lon': [i[1] for i in cs.values()]})
#df = df[df['pop2'] > n2/1000]
df['text'] = df['Hosp'].astype(str) + '<br>Amount ' + (df['pop']).astype(str)
limits = [(0,200),(300,1000),(1100,2000),(2100,5000),(5000,300000)]
colors = ["royalblue","crimson","lightseagreen","orange","lightgrey"]
cities = []
df = df[df['dt'] >= '1941']
df = df[df['dt'] <= '1946']
fig = px.scatter_geo(df, lat = 'lat', lon = 'lon',  color="pop1", hover_name='text',
                     size="pop",
                     animation_frame="dt",
                     projection="natural earth",
                     locationmode = 'country names')
fig.update_layout(
        title_text = 'Интерактивная карта'
        )
plotly.offline.plot(fig, filename='C:/Users/veoga/map.html')

fig.show()