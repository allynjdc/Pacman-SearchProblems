import util
import search

def fringeSearching(problem, fringe, heuristic=None):
    """
    fringe Searching algorithm that takes a problem and a queuing strategy
    and performs a search given that strategy
    Written Answers for Question 1
                                                                 
    Written Answers for Question 4
    
    """

    visited = []        # List for visisted nodes
    action_list = []    # List for actions taken to get to the current node
    start = problem.getStartState()   # returns the location of the start state

    #
    if isinstance(fringe, util.PriorityQueue):
        fringe.push((start, action_list), heuristic(start, problem))
    else:
        fringe.push((start, action_list))

    #
    while fringe: 
	node, actions = fringe.pop()        

        if not node in visited:
            visited.append(node)
            if problem.isGoalState(node):
                return actions
            successors = problem.getSuccessors(node) 	#[location,direction,cost]
            for successor in successors:
                newActions = actions + [successor[1]]
                if isinstance(fringe, util.PriorityQueue):
                    newCost = problem.getCostOfActions(newActions) + \
                               heuristic(successor[0], problem)
                    fringe.push((successor[0], newActions), newCost) 
		else: 
                    fringe.push((successor[0], newActions))                 
    return []


