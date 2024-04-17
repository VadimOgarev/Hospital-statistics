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
        if "ЭГ" in line['gospital'] or "ТППГ" in line['gospital'] or "ХППГ" in line['gospital']  or "ГЛР" in line['gospital']  or "ИГ" in line['gospital']:
            if 'Поздний этап' in cs.keys():
                cs['Поздний этап'] += 1
            else:
                cs['Поздний этап'] = 1
        elif "ППГ" in line['gospital'] or "ОМСБ" in line['gospital'] or "ТППГ" in line['gospital']  or "ОДР" in line['gospital']  or "СЭО" in line['gospital']:
            if 'Ранний этап' in cs.keys():
                cs['Ранний этап'] += 1
            else:
                cs['Ранний этап'] = 1
        else:
            if 'Другое' in cs.keys():
                cs['Другое'] += 1
            else:
                cs['Другое'] = 1
    for i in cs.keys():
        print(i, '- %f' % (cs[i] / count, ))
    print(count)
    df = pd.DataFrame({'Госпитали': cs.keys(), 'Количество': cs.values()})
    df = df.sort_values('Количество', ascending=True)
    fig = px.bar(df, x='Госпитали', y='Количество')
    fig = px.pie(df, values='Количество', names='Госпитали')
    fig.show()
    plotly.offline.plot(fig, filename='C:/Users/veoga/type.html')