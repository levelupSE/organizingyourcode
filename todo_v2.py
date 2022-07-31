import os
from datetime import datetime
from dataclasses import dataclass

exit_command = 'done'
new_line = '\n'

def get_user_inputs(prompt):
    user_inputs = []
    while True:
        user_input = input(prompt)
        if user_input == exit_command:
            return user_inputs

        current_timestamp = int(datetime.now().timestamp())
        user_inputs.append((user_input, current_timestamp))

def run(filename, user_inputs, todos_to_csv, write_rows):
    file_contents = todos_to_csv(user_inputs)
    write_rows(filename, file_contents)

def todos_to_csv(user_inputs):
    csv_rows = [','.join([user_input, str(timestamp)]) for user_input, timestamp in user_inputs]
    return new_line.join(csv_rows) + new_line

def write_rows(filename, file_contents):
    with open(filename, 'w') as f:
        f.write(file_contents)


if __name__ == '__main__':
    filename = 'todo2.csv'
    user_inputs = get_user_inputs('What is your todo?')
    run(filename, user_inputs, todos_to_csv, write_rows)

