"""Day 070: Project: task tracker. Implement these contracts after attempting them."""

class TaskTracker:
    'add(title) returns sequential ID starting at 1; nonempty string title required or ValueError. list_tasks() returns fresh records {id,title,done}, insertion order, initially done=False.'

    def __init__(self):
        raise NotImplementedError("Attempt day 070, exercise 1: TaskTracker")


def complete_tasks(tasks, ids):
    'Return fresh records with done=True for supplied IDs; retain other fields. Unknown requested ID raises KeyError; do not mutate input.'
    raise NotImplementedError("Attempt day 070, exercise 2: complete_tasks")


def task_report(tasks):
    'Return {total,completed,pending}; pending is sorted titles of tasks with done=False. Each record has title and boolean done.'
    raise NotImplementedError("Attempt day 070, exercise 3: task_report")

