import csv
import time
import datetime
import plotly
import plotly.express as px
import pandas as pd

n = int(input()) # сколько мы хотим записей посмотреть (нужно, если смотреть часть бд)
with open('data.txt') as f: #открываем файл записей
    reader = csv.DictReader(f, delimiter='\t') #конвертируем d csv
    cs = dict() #словарь
    count = 0 # счётчик считанных записей
    for line in reader: # цикл, считывающий записи
        try:  #  если в записи всё хорошо, обрабатываем её
            if  count > n: # если уже посмотрели нужные n записей, заканчиваем считывание
                break
            line['data_vibitiya'] = datetime.datetime.strptime(line['data_vibitiya'][3:], '%m.%Y') # записываем месяц и год в datetime
            count+=1 # запоминаем, что считали ещё 1 строку
            if line['data_vibitiya'] in cs: # если уже создан ключ словаря на этот месяц и год, запоминаем, что ещё 1 раненый выпустился в это время
                cs[line['data_vibitiya']] += 1
            else: # если ключ не создан, создаём
                cs[line['data_vibitiya']] = 1
        except: # если в записи серъёезня ошибка или проруска, пропускаем её
            print('')
    for i in cs.keys(): # для каждого ключа выводим в терминал (не в диаграмму), это не особенно нужно, просто для интереса
        print(i, '- %f' % (cs[i] / count, ))
    df = pd.DataFrame({'Дата': cs.keys(), 'Количество': cs.values()}) # конвертируем словарь в datetime 
    df = df[df['Количество'] >= 100] # отбрасываем месяца, где слишком мало больных (это из мирных времён, ведь бд - просто считанные архивы, не только с 2 мировой, или люди просто не ту дату не записали)
    df = df[df['Дата'] >= '1941/06'] # отбрасываем всё, что было до войны
    df = df.sort_values('Дата', ascending=True) # сортируем данные по возрастанию даты
    fig = px.bar(df, x='Дата', y='Количество') # создаём гистограмму
    fig.show() # выводим диаграмму
    plotly.offline.plot(fig, filename='C:/Users/veoga/month.html') # сохраняем диаграмму
