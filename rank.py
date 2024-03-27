import csv
import plotly.express as px
import pandas as pd
import plotly

with open('data.txt') as f:
    reader = csv.DictReader(f, delimiter='\t')
    cs = dict()
    n =int(input())
    m = float(input())
    count = 0
    for line in reader:
        if count > n:
            break
        count+=1
        if line['rank'] in cs:
            cs[line['rank']] += 1
        else:
            cs[line['rank']] = 1
    for i in cs.keys():
        print(i, '- %f' % (cs[i] / count, ))
    n -= cs['красноармеец'] - cs['краснофлотец'] - cs['']
    cs.pop('')
    cs.pop('красноармеец')
    cs.pop('краснофлотец')
    try:
        cs.pop('гв. красноармеец')
    except:
        print(1)
    try:
        cs.pop('мл. командир')
    except:
        print(1)
    try:
        cs.pop('сотрудник')
    except:
        print(1)
    try:
        cs.pop('[неразборсиво]')
    except:
        print(1)
    print(count)
    df = pd.DataFrame({'Звание': cs.keys(), 'Количество': cs.values()})
    #df = df[['лейтенант', 'мл. лейтенант', 'старшина', 'ефрейтор']]
    df = df[df['Количество'] > n/100/m]
    df = df.sort_values('Количество', ascending=True)
    fig = px.bar(df, x='Звание', y='Количество', width = 1000)
    fig.show()
    plotly.offline.plot(fig, filename='C:/Users/veoga/month.html')