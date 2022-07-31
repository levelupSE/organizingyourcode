import os
import datetime

filename = 'todos1.csv'

todos = []

while True:
    todo = input('What is your todo?')
    if todo == 'done':
        break

    todos.append([todo, int(datetime.datetime.now().timestamp())])

with open(filename, 'a') as f:
    for todo, timestamp in todos:
        f.write(f'{todo},{timestamp}\n')
