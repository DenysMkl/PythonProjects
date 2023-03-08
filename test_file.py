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

'''from bs4 import BeautifulSoup as bs
import requests

def get_leaderboard_honor():
    new_r = requests.get('https://www.codewars.com/users/leaderboard')
    new_soup = bs(new_r.content, 'html.parser')
    mass = []
    for i in new_soup.select('table tr'):
        mass.append(i.find("td", attrs={'class': "honor"}))
    return [int(i.text.replace(',', '')) for i in mass[1:]]


print(get_leaderboard_honor())
'''


'''def lengthOfLongestSubstring(s):
    d = {i:[] for i in set(s)}
    for i in set(s):
        for ind, value in enumerate(s):
            if i == value:
                d[value].append(ind)
    for i in d:
        d[i].append(len(s))
    return d

print(lengthOfLongestSubstring('pwwkew'))'''
'''from collections import deque


def mark_sort(x):
    priors = {'*': 0, '/': 0, '+': 1, '-': 1}
    return priors.get(x)


def calculate(s: str) -> int:
    s = list(s.replace(" ", ""))
    values, marks = '', ''

    counter = 0
    while counter < len(s):
        if s[counter].isdigit() or s[counter] == '.':
            values += s[counter]
            marks += " "
        else:
            marks += s[counter]
            values += " "
        counter += 1
    if not marks.strip():
        return int(values)
    values, marks = list(map(lambda x: int(x) if '.' not in x else float(x), values.split())), marks.split()

    if len(marks) == len(values):
        values[0] = -values[0]
        marks.pop(0)

    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '/': lambda a, b: a / b,
        '*': lambda a, b: a * b
    }
    prioritets = sorted(marks, key=mark_sort)
    find_all = {
        '+': deque([ind for ind, value in enumerate(marks) if value == '+']),
        '-': deque([ind for ind, value in enumerate(marks) if value == '-']),
        '/': deque([ind for ind, value in enumerate(marks) if value == '/']),
        '*': deque([ind for ind, value in enumerate(marks) if value == '*'])
    }
    positions = []
    for i in prioritets:
        deleted = find_all[i].popleft()
        positions.append(deleted)

    a, b, c = (values[positions[0]], marks[positions[0]], values[positions[0] + 1])

    s = ''.join(s)
    s = s.replace(str(a) + b + str(c), str(int(operations[b](a, c))),1)
    print(s)
    return calculate(s) if any(list(map(lambda x: x in "+-/*" and len(values) > 2, s))) else int(s) if '.' not in s else int(float(s))'''

import itertools
def countFairPairs(nums, lower: int, upper: int):
    checker = lambda x, y: lower <= nums[x]+nums[y] <= upper and 0 <= x < y < len(nums)
    counter = 0
    for i in list(itertools.combinations(range(len(nums)), 2)):
        if checker(*i):
            counter+=1
    return counter
    #return checker()


slovo = 'abcabcbb'

def find(s):
    char_set, max_len, start = set(), 0, 0
    for i, c in enumerate(s):
        while c in char_set:
            char_set.remove(s[start])
            start += 1
        char_set.add(c)
        max_len = max(max_len, i - start + 1)
    return max_len, start

#print(find(slovo))


mass = [-5, -2, -1, 2, 4, 10, 12, 15]

def binSearch(mass, target):
    start, end = 0, len(mass)-1

    while start <= end:
        mid = (start+end)//2
        if mass[mid] == target:
            return mid
        elif mass[mid] < target:
            start = mid+1
        else:
            end = mid-1

    return start

#print(binSearch(mass, 10))

def findTheDifference(s: str) -> int:
    set_s, max_len, cur_len = set(), 0, 0
    for val, i in enumerate(s):
        while i in set_s:
            set_s.remove(s[cur_len])
            cur_len += 1
        set_s.add(i)
        max_len = max(max_len, val - cur_len + 1)

    return max_len

#print(findTheDifference('abcabcbb'))


def repeatedSubstringPattern(s):
    repl = ''.join(sorted(set(s), key=lambda x: s.index(x)))
    if repl == s:
        return False
    while repl in s:
        s = s.replace(repl, ' ', 1)
    return not s

print(repeatedSubstringPattern('abab'))