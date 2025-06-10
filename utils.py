# utils.py

def add_task(task):
    with open('todo.txt', 'a') as f:
        f.write(task + '\n')

def list_tasks():
    with open('todo.txt', 'r') as f:
        return f.readlines()

def remove_task(index):
    tasks = list_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)
        with open('todo.txt', 'w') as f:
            f.writelines(tasks)
# TODO: add unit tests
