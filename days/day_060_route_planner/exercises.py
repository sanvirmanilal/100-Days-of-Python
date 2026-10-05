"""Day 060: Project: weighted route planner. Implement these contracts after attempting them."""

def path_cost(graph, path):
    'graph maps nodes to (neighbor,weight) lists with unique neighbors and nonnegative weights. Return sum along path; paths of length <=1 cost 0. Missing edge raises ValueError.'
    raise NotImplementedError("Attempt day 060, exercise 1: path_cost")


def dijkstra_distances(graph, start):
    'Return minimum costs to all reachable nodes, including start at 0. Weights are nonnegative integers; use a heap.'
    raise NotImplementedError("Attempt day 060, exercise 2: dijkstra_distances")


def cheapest_route(graph, start, goal):
    'Return {cost, path} or None if unreachable. For equal costs choose lexicographically smallest full path. Node names are strings; weights are strictly positive, except zero-edge start==goal.'
    raise NotImplementedError("Attempt day 060, exercise 3: cheapest_route")

