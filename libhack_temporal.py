#!/usr/bin/env python
# coding: utf-8

# # Решение на Хакатоне "Детекция, интерпретация и валидация временных конструкций в русскоязычных текстах". <br> 3 место (на основе решения жюри)

# ## Организаторы и участники: 
# 
# ПАО "[Сбербанк](https://www.sberbank.ru/)"
# 
# - Образовательная программа [Sber Graduate](https://sbergraduate.ru/)
#     - [Школа 21](https://21-school.ru/)
# 
# - ФГБУ "[Российская государственная библиотека](https://rsl.ru)"
# 
#     - Проектный офис [Национальный электронной библиотеки](https://nebrf.ru)
#     - Лаборатория исследования и разработок
#     - Отдел инженеров знаний
# 
# #### Время проведения: 27 ноября 2020 - 29 ноября 2020
#   
# ## Задача
# 
# В рамках Национальной цифровой (электронной) библиотеки ее оператором Российской Государственной Библиотекой в 2020 году был запущен пилотный проект по оцифровке исторически значимых периодических изданий. Конечной целью является высокодоступное человеко- и машиночитаемое представление как самих выпусков, так и преработанный под платформы цифровой дистрибьюции текстовый и графический материал, а также высокоуровневые индексы сущностей, позволяющие работать с хронологией и связями, присутствующими в материале, осуществлять их фактологическую интеграцию с материалами из других источников.
# 
# Значительной проблемой для высокоуровнего автоматизированного анализа являлось отсутствие специализированных механизмов для работы с темпоральными конструкциями русского языка. Формирование таких инструментов, пригодных к широкому применению и работающих с гарантированно высоким качеством и стало отправной точкой совместного хакатона. 
# 
# Команды, участвующие в хакатоне должны в качестве результата работы предоставить совокупность данных и программных решений, из которых возможно сформировать процесс:
# 
# - Машинночитаемый корпус темпоральных конструкций русского языка, на момент завершения мероприятия явяющийся уникальной разработкой. С помощью этого корпуса осуществлялась многосторонняя проверка и оценка качества автоматизированных систем (Test suites).
# 
# - Произвести качественную верификацию корпуса и исправить как ошибки расшифровки темпоральных значений, так выявить субоптимальные моменты в технической конвенции и принципах кодирования значений. 
# 
# - Программные решения, осуществляющие:
#  * Выделение из общего объема текстового материала на выходе пилотной системы оцифровки периодических изданий.
#  * Интерпретацию выделенных фрагментов с привязкой к конкретной временной точке на временной шкале, дающей начало для отсчета сдвигов временного контекста.
# 
# - Прототип полного стека временного индекса на основе материала оцифровки изданий газеты "Красная Звезда" за период 1941 - 1945 г. (1539 выпусков), включая систему развертывания и работоспособную клиентскую часть.
# 
# ### Технические детали формата даты, использованные в процессе тестирования корпуса
# 
# С целью экономии времени, которое потребовалось бы участникам для ознакомления со стандартами специализированной разметки, а также более просто адаптации под произвольный дизайн программных систем, технический формат, используемый в рамках работы РГБ (Facebook [Duckling2](https://github.com/facebook/duckling) corpus file, [ISO TimeM L1.2.1 + TIMEX3](http://www.timeml.org)) был упрощен
# 
# Стандартные значения дат и времени задаются в формате [ГОСТ Р 7.0.64-2018](http://protect.gost.ru/v.aspx?control=8&baseC=-1&page=0&month=-1&year=-1&search=&RegNum=1&DocOnPageCount=15&id=222978) 
# "_Система стандартов по информации, библиотечному и издательскому делу. Представление дат и времени. Общие требования_" (модификация стандарта [ISO 8601:2004](https://www.iso.org/standard/40874.html))
# 
# * Не используется часть стандарта ISO:8601, где определен формат задания временной протяженности. 
# * Для указания временных значений используется расширенная (extended) форма нотации, если таковая описана для используемого типа временной отметки.
# * Гранулярность точечного времени или границ интервала могла быть с точностью в рамках календарного года, месяца, дня. И время до целых часов, минут или секунд.
# * Для указания интервалов использовался разделитель в виде знака минус с двумя пробелами по бокам: ` - `
# * Обе границы интервалов считались включенными в него по минимальной или максимальной границе своего определения.
# * Ввод и вывод осуществляется в формате comma separated values, экранирование символов с помощью взятия значения в двойные кавычки: `"this value, comma contains".
# 
# Пример: 
# ```csv
# "Id","Expected"
# "с одиннадцати тридцати утра до часу тридцати дня","2020-11-27T11:30 - 2020-11-27T13:30"
# "с 18 по 27 января 1942 года","1942-01-18 - 1942-01-27"
# ```
# 
# Интервал содержит такой же формат дат, что и точечные даты.
# 
# ## Датасеты
# 
# - Без ответов -  temporal-thesaurus-analytical-corpora-sample-submission.csv
# - С ре-верифицированными ответами - temporal-corpora-ru-rev3-resolved.csv
# 
# 
# ## Итоговый счет команд
# 
# Рассчитан относительно ре-верифицированной третьей ревизии корпуса в которой экспертно были разрешены конфликты между образцом и вариантами лучшей команды, осуществившей ручную верификацию вслупую (указывали свой вариат расшифровки, не зная варианта, указанного в образце).
# 
# | Мой счет (от 0.0 до 1.0) | Команда | Попытка |
# | --- | --- | --- |
# | 0.342784 | ElenaKiseleva | 18344287 - Pub_0_35567 Priv_0_35567.csv |
# 
# 
# **Источник https://github.com/ndlrf-rnd/school21-retropress-temporal**
# 

# ## Подгрузка библиотек и самописные функции

# In[1]:


import numpy as np
import pandas as pd
import joblib
import time
import warnings
from termcolor import colored

import dateparser
import datetime
import re


# In[2]:


#Определяем болд
def bold(): 
    return "\033[1m"

def bold_end(): 
    return "\033[0m"

#Ставим формат для нумериков
pd.options.display.float_format = '{: >10.2f}'.format

#Убираем ворнинги
warnings.simplefilter(action='ignore', category=FutureWarning)


# In[3]:


#**Функция print_basic_info, для вывода информации о массиве, и его переменных.**

#* base - название базы данных
#* info - 1: вывод информации о массиве, другое: не вывод
#* describe - 1: вывод описания переменных массива, другое: не вывод        
#* duplicat - 1: вывод количества полных дублей
#* head - n: вывод примера базы (вывод n - строк), n < 1: не вывод

def print_basic_info(base, info, describe, duplicat, head):
    if info == 1:
        print("\n", bold(), colored('info','green'), bold_end(), "\n")
        print( base.info())  
    if head >= 1:
        print("\n", bold(),colored('head','green'),bold_end())
        display(base.head(head))
    if describe == 1:
        print("\n", bold(),colored('describe','green'),bold_end(),"\n")
        for i in base.columns:
            print("\n", bold(), colored(i,'blue'),bold_end(),"\n", base[i].describe())
    if duplicat == 1:
        print("\n", bold(),colored('duplicated','green'),bold_end(),"\n")
        print(base[base.duplicated() == True][base.columns[0]].count())


# ##  Подготовка данных

# **Открываем**

# In[4]:


#Загружаем
contest_train = pd.read_csv(
    'datasets/temporal-thesaurus-analytical-corpora-sample-submission.csv', sep=',',decimal='.')


# In[5]:


print_basic_info(contest_train,1,0,1,5)


# ## Парсинг

# #задала стартовые даты

# In[6]:


test_date =  datetime.datetime(2020, 11, 27, 2,30)
format_date = "%Y-%m-%dT%H:%M"

date_in_format = '2020-11-27T00:00'
now_in_format = '2020-11-27T02:30'


# #лемотизировала

# In[7]:


contest_train['id_copy'] = contest_train['Id'].str.lower()

from pymystem3 import Mystem
m = Mystem()

def lem (row):
    text = row['id_copy']
    return (' '.join(m.lemmatize(str(text))))

contest_train['id_copy'] = contest_train.apply(lem, axis=1)


# #исключила предлоги

# In[8]:


stop_words = ['то','за','в','го','-','не','е',',','во','к','на','ко']

contest_train['id_copy_one'] = contest_train['id_copy'].apply(lambda x: [word for word in x.split() if word not in stop_words])
contest_train['id_copy'] = [' '.join(map(str, l)) for l in contest_train['id_copy_one']]


n = 6
for i in range(0, len(contest_train)):
    try:
        contest_train.loc[i,'id_copy']  = re.sub(r'([0-9])-?(?:му|ой|ого|го|е)', '\g<1>', contest_train.loc[i,'id_copy'])
    except:
        n += 1   


# #перевела цифры

# In[9]:


nbr = ["первый", "второй", "третий", "четвертый", "пятый", "шестой", "семой", "восемой", "девятый", "десятый","одинадцатый", "двенадцать", "тринадцатый", "четырнадцатый", "пятнадцатый", "шестнадцатый",
"семнадцатый", "восемнадцатый", "девятнадцатый", "двадцатый"]

for i in range(1,21):
    contest_train['id_copy'] = contest_train['id_copy'].str.replace(str(nbr[i-1]),str(i))

contest_train['id_copy'] = contest_train['id_copy'].str.replace('тридцатый',"30")    
contest_train['id_copy'] = contest_train['id_copy'].str.replace('одиннадцатый',"11")
contest_train['id_copy'] = contest_train['id_copy'].str.replace('четыре',"4")


# #ручная чистка

# In[10]:


contest_train['id_copy'] = contest_train['id_copy'].str.replace('дека ',"декабрь ")


# In[11]:


contest_train.head()


# <!-- # n = 6
# 
# # for i in range(0, len(contest_train)):
# #     try:
# #         contest_train.loc[i,'day']  = re.findall(r'[0-9]{2}', contest_train.loc[i,'id_copy'])
# #         if len(re.findall(r'[0-9]{2}', contest_train.loc[i,'id_copy'])) > 1:
# #             contest_train.loc[i,'year']  = re.findall(r'[0-9]{4}', contest_train.loc[i,'id_copy'])[0]
# #             contest_train.loc[i,'year_2']  = re.findall(r'[0-9]{4}', contest_train.loc[i,'id_copy'])[1]
# #     except:
# #         n += 1    -->

# In[12]:


contest_train['id_copy'] = contest_train['id_copy'].replace('за завтрашний','завтра')
contest_train['id_copy'] = contest_train['id_copy'].replace('назавтра','завтра')
contest_train['id_copy'] = contest_train['id_copy'].replace('накануне','вчера')
contest_train['id_copy'] = contest_train['id_copy'].replace('рано','назад')
contest_train['id_copy'] = contest_train['id_copy'].replace('ранее','назад')
contest_train['id_copy'] = contest_train['id_copy'].replace('спустя','через')
contest_train['id_copy'] = contest_train['id_copy'].replace('послепослезавтра ','через два день')
contest_train['id_copy'] = contest_train['id_copy'].replace('дека .','декабрь')
contest_train['id_copy'] = contest_train['id_copy'].replace('янва .','января')
contest_train['id_copy'] = contest_train['id_copy'].replace('в последний день неделя ','воскресение')
contest_train['id_copy'] = contest_train['id_copy'].replace('\n','')
contest_train['id_copy'] = contest_train['id_copy'].replace('сие','сегодня')
contest_train['id_copy'] = contest_train['id_copy'].replace('следующий день','завтра')
contest_train['id_copy'] = contest_train['id_copy'].replace('следующий сутки','завтра')
contest_train['id_copy'] = contest_train['id_copy'].replace('день через','через день')
contest_train['id_copy'] = contest_train['id_copy'].replace('агуста','августа')
contest_train['id_copy'] = contest_train['id_copy'].replace('близкий','')


# In[13]:


contest_train['id_copy'] = contest_train['id_copy'].replace('два тысяча восемнадцатый год','2018')
contest_train['id_copy'] = contest_train['id_copy'].replace('дека ','декабрь')


# #обработка промежутков

# In[14]:


n = 0
 
for i in range(0, len(contest_train)):
    try:
            d = contest_train.loc[i,'id_copy'].split('-')
            contest_train.loc[i,'id_copy'] = contest_train.loc[i,'id_copy'].split('-')[0]
            contest_train.loc[i,'pred_2'] = contest_train.loc[i,'id_copy'].split('-')[1]
    except:
        n += 1   
    
for i in range(0, len(contest_train)):
    try:
            d = contest_train.loc[i,'id_copy'].split('—')
            contest_train.loc[i,'id_copy'] = contest_train.loc[i,'id_copy'].split('—')[0]
            contest_train.loc[i,'pred_2'] = contest_train.loc[i,'id_copy'].split('—')[1]
    except:
        n += 1   


for i in range(0, len(contest_train)):
    try:
            d = contest_train.loc[i,'id_copy'].split('/')
            contest_train.loc[i,'id_copy'] = contest_train.loc[i,'id_copy'].split('/')[0]
            contest_train.loc[i,'pred_2'] = contest_train.loc[i,'id_copy'].split('/')[1]
            print(contest_train.loc[i,'id_copy'], contest_train.loc[i,'pred_Q'])
    except:
        n += 1

for i in range(0, len(contest_train)):
    try:
        if len(re.findall(r'[0-9]{4}', contest_train.loc[i,'id_copy'])) > 1:
            contest_train.loc[i,'id_copy'] = contest_train.loc[i,'id_copy'].split(re.findall(r'[0-9]{4}', contest_train.loc[i,'id_copy'])[1])[0]
            contest_train.loc[i,'pred_2'] = contest_train.loc[i,'id_copy'].split(re.findall(r'[0-9]{4}', contest_train.loc[i,'id_copy'])[0])[1]
            print(contest_train.loc[i,'id_copy'], contest_train.loc[i,'pred_Q'])
            #contest_train.loc[i,'pred'] = now_in_format
    except:
        n += 1
        

for i in range(0, len(contest_train)):
    try:
        if ('c ' in contest_train.loc[i,'id_copy']) or ('по ' in contest_train.loc[i,'id_copy']):
            contest_train.loc[i,'id_copy'] = contest_train.loc[i,'id_copy'].split('по ')[0]
            contest_train.loc[i,'pred_2'] = contest_train.loc[i,'id_copy'].split('по ')[1]
            print(contest_train.loc[i,'id_copy'], contest_train.loc[i,'pred_Q'])
    except:
        n += 1


# In[15]:


def to_date(x):
    i = x['pred_2']
    try:
        return dateparser.parse(i, settings={'RELATIVE_BASE': test_date })
    except:
        g = 0
        
        
#применяем 
contest_train['pred_2'] = contest_train.apply(to_date, axis=1)


def to_date(x):
    i = x['id_copy']
    return dateparser.parse(i, settings={'RELATIVE_BASE': test_date })

#применяем 
contest_train['pred'] = contest_train.apply(to_date, axis=1)


# In[16]:


n = 0
for i in range(0, len(contest_train)):
    try:
        contest_train.loc[i,'pred'] = contest_train.loc[i,'pred'].strftime("%Y-%m-%dT%H:%M")
        contest_train.loc[i,'pred_2'] = contest_train.loc[i,'pred'].strftime("%Y-%m-%dT%H:%M")
    except:
        n += 1


# In[17]:


#обработка бывший - нынешний -текущий и т.д.


# In[18]:


def ft_cods (row):
    text = row['id_copy']
    if ('сейчас' in text):
        return str(now_in_format)

contest_train['pred_str'] = contest_train.apply(ft_cods, axis=1)
contest_train['pred_str'] = contest_train['pred'].astype(str)


# In[19]:


this_year = 2020
n = 0
for i in range(0, len(contest_train)):
    if ('год' in contest_train.loc[i,'id_copy']) or ('кв.' in contest_train.loc[i,'id_copy']):
        if ('прошлый' in contest_train.loc[i,'id_copy']) or (
            'минувший' in contest_train.loc[i,'id_copy']) or ('предыдущий' in contest_train.loc[i,'id_copy']):
            contest_train.loc[i,'pred_Q'] = str(this_year - 1)
        if ('этот' in contest_train.loc[i,'id_copy']) or('сей' in contest_train.loc[i,'id_copy'])  or(
            'уходить' in contest_train.loc[i,'id_copy']) or ('уходящий' in contest_train.loc[i,'id_copy']) or (
            'текущий' in contest_train.loc[i,'id_copy']) or ('нынешний' in contest_train.loc[i,'id_copy']) or (
            'истекать' in contest_train.loc[i,'id_copy']):
            contest_train.loc[i,'pred_Q'] = str(this_year)
        if ('следующий' in contest_train.loc[i,'id_copy']) or('грядущий' in contest_train.loc[i,'id_copy'])  or(
            'предстоять' in contest_train.loc[i,'id_copy']) or ('предстоящий' in contest_train.loc[i,'id_copy']):
            contest_train.loc[i,'pred_Q'] = str(this_year + 1)


# In[20]:


n = 0
for i in range(0, len(contest_train)):
    try:
        if ('сейчас' in contest_train.loc[i,'id_copy']) or ('момент' in contest_train.loc[i,'id_copy']):
            contest_train.loc[i,'pred'] = now_in_format
        if ('сегодняшний' in contest_train.loc[i,'id_copy']) or ('сие' in contest_train.loc[i,'id_copy']):
            contest_train.loc[i,'pred'] = date_in_format
        if ('этот' in contest_train.loc[i,'id_copy']) and ('минута' in contest_train.loc[i,'id_copy']):
            contest_train.loc[i,'pred'] = now_in_format
        if ('этот' in contest_train.loc[i,'id_copy']) and ('день' in contest_train.loc[i,'id_copy']):
            contest_train.loc[i,'pred'] = date_in_format
    except:
        n += 1
        
#попытка обработки часов
for i in range(0, len(contest_train)):
    try:
        if ('4 утро' in contest_train.loc[i,'id_copy']) or ('4 час' in contest_train.loc[i,'id_copy']) or (
            '04 : 00' in contest_train.loc[i,'id_copy']):
            contest_train.loc[i,'pred'] = '2020-11-27T04:00'
        if ('2:20' in contest_train.loc[i,'id_copy']) or ('два двадцать' in contest_train.loc[i,'id_copy']):
            contest_train.loc[i,'pred'] = '2020-11-27T02:20'
    except:
        n += 1  


# In[21]:


#обработка кварталов


# In[22]:


this_year = 2020
n = 0
for i in range(0, len(contest_train)):
    try:
        if ('квартал' in contest_train.loc[i,'id_copy']) or ('кв.' in contest_train.loc[i,'id_copy']):
            contest_train.loc[i,'id_copy'] = contest_train.loc[i,'id_copy'].replace('   ',' ').replace('- й','').replace('2й','2')
            if ('первый' in contest_train.loc[i,'id_copy']) or ('1 ' in contest_train.loc[i,'id_copy']):
                q = 1
            elif ('второй' in contest_train.loc[i,'id_copy']) or ('2 ' in contest_train.loc[i,'id_copy']) or ('ii квартал' in contest_train.loc[i,'id_copy']):
                q = 2
            elif ('третий' in contest_train.loc[i,'id_copy']) or ('3 ' in contest_train.loc[i,'id_copy']):
                q = 3
            elif ('чевертый' in contest_train.loc[i,'id_copy']) or ('4 ' in contest_train.loc[i,'id_copy']):
                q = 4
            year = re.findall(r'[0-9]{4}',contest_train.loc[i,'id_copy'])[0]
            if ('два тысяча восемнадцатый год' in contest_train.loc[i,'id_copy']):
                year = 2018
            elif ('этот год' in contest_train.loc[i,'id_copy']) or ('текущий   год' in contest_train.loc[i,'id_copy']):
                year = this_year
            contest_train.loc[i,'pred_Q'] = str(year)+"-Q"+str(q)
    except:
        n += 1


# #Если 00 00 время - окидываем часть

# In[23]:


contest_train['pred_str'] = contest_train['pred'].astype(str)

n = 0
for i in range(0, len(contest_train)):
    try:
        if contest_train.loc[i,'pred_str'].split("T")[1] == '00:00':
            contest_train.loc[i,'pred_str'] = contest_train.loc[i,'pred_str'].split("T")[0]
    except:
        n += 1

np.mean(contest_train.pred_str == '2020-12-01')


contest_train['pred_2'] = contest_train['pred_2'].astype(str)

n = 0
for i in range(0, len(contest_train)):
    try:
        if contest_train.loc[i,'pred_2'].split("T")[1] == '00:00':
            contest_train.loc[i,'pred_2'] = contest_train.loc[i,'pred_str'].split("T")[0]
    except:
        n += 1

np.mean(contest_train.pred_str == '2020-12-01')


# In[24]:


contest_train.head()


# #объединяем со сточкой по квартилям

# In[25]:


for i in range(0, len(contest_train)):
    try:
        if int(re.findall(r'[0-9]{4}',contest_train.loc[i,'pred_Q'])[0]) > 0:
            contest_train.loc[i,'pred_str'] = contest_train.loc[i,'pred_Q']
    except:
        n += 1


# In[26]:


#пропуски по желанию заполняем текущей датойи временем.
#contest_train['pred_str'] = contest_train['pred_str'].replace('NaT','2020-11-27T02:30')


# ##  Сохранение

# In[27]:


data = pd.DataFrame()
data['Id']= contest_train['Id']
data['Expected']= contest_train['pred_str'] + "-" + contest_train['pred_2']
data['Expected'] = data['Expected'].str.replace('-NaT','')


# In[28]:


import datetime

now = datetime.datetime.now()
now.strftime("%m_%d_%H_%M")
data.to_csv('sub_kiseleva_'+str(now)+'.csv', index=False)
# print("Your submission was successfully saved!")


# ##  Проверка точности

# In[29]:


#Загружаем ответы
contest_resolved = pd.read_csv(
    'datasets/temporal-corpora-ru-rev3-resolved.csv', sep=',',decimal='.')


# In[30]:


accuracy =  data['Expected'] == contest_resolved['Expected']


# In[31]:


print(bold(),colored('Точность -','blue'), bold(), colored(accuracy.mean(),'blue'), bold_end()) 

