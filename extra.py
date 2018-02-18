import util
import search

def genericSearch(problem, fringe, heuristic=None):
    """
    Generic search algorithm that takes a problem and a queuing strategy
    and performs a search given that strategy
    Written Answers for Question 1
    1. The exploration order is what I would have expected. The search goes as
       deep as it can, before exploring other paths (as would be expected with 
       depth first search).
    2. No, Pacman does not go to all of the explored squares on the way to the 
       goal. He follows a path that does not lead him to any dead-ends, even if
       dead ends were explored. In my implementation, the length for a 
       MediumMaze was 130.
    3. This is not the least-cost solution -- there is clearly a cheaper 
       solution that Pacman does not take on the MediumMaze. This is because
       DFS will return the first solution that it finds that solves the problem,
       not the best solution.
    Written Answers for Question 4
    1. With OpenMaze, BFS, UCS, and A* all find the shortest path to the goal, 
       with BFS and UCS expanding the same number of search nodes (682) and A*
       expanding the least amount of nodes (535). All paths have a cost of 54.
       DFS does find the solution as well, but is not the shortest -- the cost
       of the path found with DFS was 298. This is because DFS does not look 
       for the shortest path.
    """

    visited = []        # List of already visisted nodes
    action_list = []    # List of actions taken to get to the current node
    start = problem.getStartState()   # Starting state of the problem
	
    print "initial: ",start

    # Push a tuple of the start state and blank action list onto the given
    # fringe data structure. If a priority queue is in use, then calculate
    # the priority using the heuristic
    if isinstance(fringe, util.PriorityQueue):
        fringe.push((start, action_list), heuristic(start, problem))
    else: #isinstance(fringe, util.Stack) or isinstance(fringe, util.Queue):
        fringe.push((start, action_list))

    # While there are still elements on the fringe, expand the value of each 
    # node for the node to explore, actions to get there, and the cost. If the
    # node isn't visited already, check to see if node is the goal. If no, then
    # add all of the node's successors onto the fringe (with relevant 
    # information about path and cost associated with that node)
    while fringe: 
	node, actions = fringe.pop()
	print "node: ", node
	print "action: ", actions         

        if not node in visited:
            visited.append(node)
            if problem.isGoalState(node):
                return actions
            successors = problem.getSuccessors(node)
            for successor in successors:
                coordinate, direction, cost = successor
                newActions = actions + [direction]
                if isinstance(fringe, util.Stack) or isinstance(fringe, util.Queue):
                    fringe.push((coordinate, newActions))
                elif isinstance(fringe, util.PriorityQueue):
                    newCost = problem.getCostOfActions(newActions) + \
                               heuristic(coordinate, problem)
                    fringe.push((coordinate, newActions), newCost)                  
    return []


