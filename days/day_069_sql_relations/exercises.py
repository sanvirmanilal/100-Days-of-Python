"""Day 069: Relational joins and aggregates. Implement these contracts after attempting them."""

def task_owners(connection):
    'Tables users(id,name), tasks(id,user_id,done). Return (task_id,user_name) for matching users only, ordered task_id.'
    raise NotImplementedError("Attempt day 069, exercise 1: task_owners")


def user_task_counts(connection):
    'Return (user_id,count) for ALL users including those with zero tasks, ordered user_id. Same schema as above.'
    raise NotImplementedError("Attempt day 069, exercise 2: user_task_counts")


def completion_rates(connection):
    'Return (user_id, rate) for all users ordered user_id. rate is completed tasks / all tasks, or 0.0 for none. done is 0 or 1.'
    raise NotImplementedError("Attempt day 069, exercise 3: completion_rates")

