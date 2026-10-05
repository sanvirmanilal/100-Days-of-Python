"""Day 100: Capstone: workflow engine. Implement these contracts after attempting them."""

def ready_tasks(dependencies, completed):
    'dependencies maps task names to prerequisite name lists; all prerequisites are keys. Return sorted uncompleted tasks whose prerequisites are ALL completed. Do not mutate inputs.'
    raise NotImplementedError("Attempt day 100, exercise 1: ready_tasks")


def workflow_layers(dependencies):
    'Return execution layers: each contains ALL currently ready tasks sorted, then mark whole layer complete. All prerequisites must be keys or KeyError. Cycles raise ValueError.'
    raise NotImplementedError("Attempt day 100, exercise 2: workflow_layers")


def run_workflow(dependencies, outcomes):
    'Validate full graph as above before running. outcomes maps every task to boolean success (missing raises KeyError). Process valid layers. State success/failed by outcome when all prerequisites succeeded; otherwise blocked. Return task->state dict. Empty graph returns {}.'
    raise NotImplementedError("Attempt day 100, exercise 3: run_workflow")

