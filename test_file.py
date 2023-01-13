'''def second_task():
    my_list = [{'name': 'Oleg', 'age': 23}, {'name': 'Vasya', 'age': 19}]
    return sorted(my_list, key=lambda x: x['age'])


print(second_task())


def fourth_task():
    list1 = ['Oleg', 'Vasya', 'Anna']
    list2 = ['Ivanov', 'Sidorov', 'Petrova']
    return [(i,j) for i, j in zip(list1, list2)]


print(fourth_task())


my_lambda = lambda x, y: x+y
print(my_lambda(3, 5))


def sixth_task():
    list_ = [
        {'name': 'Alex', 'age': 25},
        {'name': 'Oleg', 'age': 23},
        {'name': 'Anna', 'age': 32},
        {'name': 'Igor', 'age': 50},
        {'name': 'Anton', 'age': 17},
    ]
    return list(filter(lambda x: 18 <= x['age'] <= 30 and x['name'][0] == 'A', list_))


print(sixth_task())
'''


from bs4 import BeautifulSoup as bs
import requests

def get_leaderboard_honor():
    new_r = requests.get('https://www.codewars.com/users/leaderboard')
    new_soup = bs(new_r.content, 'html.parser')
    mass = []
    for i in new_soup.select('table tr'):
        mass.append(i.find("td", attrs={'class': "honor"}))
    return [int(i.text.replace(',', '')) for i in mass[1:]]


print(get_leaderboard_honor())
