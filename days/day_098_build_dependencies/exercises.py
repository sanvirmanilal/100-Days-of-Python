"""Day 098: Dependency planning. Implement these contracts after attempting them."""

def dependency_closure(dependencies, target):
    'Return set of all transitive prerequisites, excluding target. Referenced missing keys have no prerequisites. Raise ValueError for a cycle reachable from target.'
    raise NotImplementedError("Attempt day 098, exercise 1: dependency_closure")


def build_plan(dependencies, target):
    'Return prerequisites plus target in valid execution order. Among available nodes choose lexicographically smallest string. Only include target closure; reachable cycle raises ValueError.'
    raise NotImplementedError("Attempt day 098, exercise 2: build_plan")


def affected_targets(dependencies, changed):
    'Return sorted keys OR referenced nodes that are changed or transitively depend on a changed node. Include changed nodes even if absent. Handle cycles without looping.'
    raise NotImplementedError("Attempt day 098, exercise 3: affected_targets")

