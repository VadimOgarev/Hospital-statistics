import csv
import plotly.express as px
import pandas as pd
import plotly

with open('data.txt') as f:
    reader = csv.DictReader(f, delimiter='\t')
    cs = dict()
    n = int(input())
    count = 0
    for line in reader:
        if count > n:
            break
        count+=1
        if line['gospital'] in cs:
            cs[line['gospital']] += 1
        else:
            cs[line['gospital']] = 1
    for i in cs.keys():
        print(i, '- %f' % (cs[i] / count, ))
    print(count)
    c, s = 0, 0
    for i in cs.keys():
        s += cs[i]
        c+=1
    avg = s/c
    s = 0
    for i in cs.keys():
        s += abs(avg-cs[i])
    print(avg, s/c)
    '''
    df = pd.DataFrame({'Госпитали': cs.keys(), 'Количество': cs.values()})
    df = df[df['Количество'] > n/100/m]
    df = df.sort_values('Количество', ascending=True)
    fig = px.bar(df, x='Госпитали', y='Количество')
    fig.show()
    plotly.offline.plot(fig, filename='C:/Users/veoga/amount.html')'''
