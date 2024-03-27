import csv
import plotly
import plotly.express as px
import pandas as pd

with open('data.txt') as f:
    reader = csv.DictReader(f, delimiter='\t')
    cs = dict()
    count = 0
    n = int(input())
    m =  int(input())
    for line in reader:
        if count > n:
            break
        count+=1
        if line['prichina_vibitiya'] in cs:
            cs[line['prichina_vibitiya']] += 1
        else:
            cs[line['prichina_vibitiya']] = 1
    for i in cs.keys():
        print(i, '- %f' % (cs[i] / count, ))
    try:
        cs.pop('убит')
        cs.pop('умер')
        cs.pop('погиб')
        cs.pop('')
    except:
        print(1)
    df = pd.DataFrame({'Причина': cs.keys(), 'Количество': cs.values()})
    df.loc[df['Количество'] < n/100/m, 'Причина'] = "Другое" 
    df = df.sort_values('Количество', ascending=True)
    fig = px.pie(df, values='Количество', names='Причина')
    fig.show()
    plotly.offline.plot(fig, filename='C:/Users/veoga/reason.html')