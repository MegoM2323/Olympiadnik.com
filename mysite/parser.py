import requests
from bs4 import BeautifulSoup
import sqlite3
from random import randint


def get_task(number):
    url = 'https://www.problems.ru/view_problem_details_new.php?id=' + str(number)
    response = requests.get(url)
    if response.status_code != 200:
        return False
    soup = BeautifulSoup(response.text, 'html.parser')

    if 'Ошибка' in soup.get_text():
        print('NOT EXSIST')
        return False
    content = soup.find('div', {'class': 'componentboxcontents'})

    data = content.find('table', {'class': 'problemdetailscaptiontable'})
    data = ' '.join(str(data.get_text()).split())

    themes = data[:data.rfind(']') + 1].strip()
    difficulty = data[data.rfind(']') + 1: data.find('Клас')].strip()
    classes = data[data.find('Клас'): data.find('Присл')].strip()

    themes = [i.strip()[:-2] for i in themes.split('[')[1:]]
    difficulty = difficulty[difficulty.find(':') + 1:].strip()
    classes = classes[classes.find(':') + 1:].strip().split(',')

    # print(themes)
    # print(difficulty)
    # print(classes)

    txt = soup.get_text()
    '''
    Условие
    Подсказка
    Решение
    Ответ
    '''
    tip = ''
    reply = ''
    if 'Условие' in txt and 'Решение' in txt:
        if 'Подсказка' not in txt and 'Ответ' not in txt:
            content = txt[txt.find('Условие') + 9: txt.find('Подсказка')].strip()
            tip = txt[txt.find('Подсказка') + 11: txt.find('Решение')].strip()
            solution = txt[txt.find('Решение') + 9: txt.find('Ответ')].strip()
            reply = txt[txt.find('Ответ') + 9: txt.find('Источники и прецеденты использования')].strip()
        elif 'Подсказка' in txt:
            content = txt[txt.find('Условие') + 9: txt.find('Подсказка')].strip()
            tip = txt[txt.find('Подсказка') + 11: txt.find('Решение')].strip()
            solution = txt[txt.find('Решение') + 9: txt.find('Источники и прецеденты использования')].strip()
        elif 'Ответ' in txt:
            content = txt[txt.find('Условие') + 9: txt.find('Решение')].strip()
            solution = txt[txt.find('Решение') + 9: txt.find('Ответ')].strip()
            reply = txt[txt.find('Ответ') + 9: txt.find('Источники и прецеденты использования')].strip()
        else:
            content = txt[txt.find('Условие'): txt.find('Решение')]
            solution = txt[txt.find('Решение'):txt.find('Источники и прецеденты использования')]
    else:
        return False
    # print(soup.)
    # print(soup.select('sub + h3 + i + p'))

    # for i in [' '.join(i.get_text().split()) for i in soup.find_all('br')]:
    #    print(i)
    # print(soup)
    res = {
        'title': randint(1, 100000),
        'themes': themes,
        'difficulty': difficulty,
        'classes': classes,
        'content': content,
        'tip': tip,
        'reply': reply,
        'solve': solution,
        'views': 0,
    }
    return res


def put_in_base(data):
    try:
        connection = sqlite3.connect('db.sqlite3')
        cursor = connection.cursor()
        sqlite_insert_query = """INSERT INTO task_manager_tasks
                              (title, themes, difficulty, classes, content, tip, reply, solve, views)
                              VALUES
                              (?, ?, ?, ?, ?, ?, ?, ?, ?);"""
        count = cursor.execute(sqlite_insert_query, [str(i) for i in data.values()])
        connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if connection:
            connection.close()


for i in range(87950, 88130):
    try:
        res = get_task(i)
        if not isinstance(res, bool):
            put_in_base(res)
        else:
            print('Error', i)
    except Exception:
        print(Exception)


def get_proxies():
    url = 'http://free-proxy.cz/en/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    proxy = []
    for item in soup.find('tbody').find_all('tr'):
        proxy.append([i.get_text() for i in item.find_all('td')])
    print(proxy)
