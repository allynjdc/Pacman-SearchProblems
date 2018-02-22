import util
import search


#
# 1st METHOD
# will be used in search.py (Q1, Q2, & Q4)
#
def fringeSearching(problem, fringe, heuristic=None):
    # fringe Searching algorithm that takes a problem and a queuing strategy
    # and performs a search given that strategy
    
    #
    # visited is a List for visisted nodes
    # action_list is a List for actions taken to get to the current node
    visited = []        
    action_list = []   

    #
    # if the IF-condition satisfies, then it will simply push to the fringe
    # which is equal to util.PriorityQueue (it means we are using A* / UCS
    # if the heuristic is null) the tuple with 3 elements; 1st element is 
    # the location of the Starting node, 2nd element is the action_list in
    # which we'll store there the consequtive actions that pacman will take
    # from the starting node up to the current node, 3rd element is the
    # heuristic (the default value of heuristic is null). In the ELSE-condition,
    # it will simply push to the fringe which is either equal to util.Stack
    # (if DFS) or util.Queue (if BFS).
    if isinstance(fringe, util.PriorityQueue):
        fringe.push((problem.getStartState(), action_list), heuristic(problem.getStartState(), problem))
    else:
        fringe.push((problem.getStartState(), action_list))

    #
    # while fringe is not empty, it will pop the (if STACK) last node or the
    # (if QUEUE) first node, then the node will append to the visited list if
    # its not yet in the visited node list before. If the unvisited node is the
    # Goal State then it will return the actions (a list of consequtive actions
    # that pacman will take from the starting node up to the end / goal node).
    # Else, we'll check all the successors of the node and simply push them to
    # the fringe (if Stack/Queue, it will push the successor node and its
    # action || if its a Priority Queue, we'll solve first its actual cost then
    # push the successor node, its action, and its actual cost).
    while fringe: 
	node, actions = fringe.pop()   
        if not node in visited:
            visited.append(node)
            if problem.isGoalState(node):
                return actions
            for successor in problem.getSuccessors(node): 	#[location,direction,cost]
                if isinstance(fringe, util.PriorityQueue):
                    actual_Cost = problem.getCostOfActions(actions + [successor[1]]) + \
                               heuristic(successor[0], problem)
                    fringe.push((successor[0], actions + [successor[1]]), actual_Cost) 
		else: 
                    fringe.push((successor[0], actions + [successor[1]]))                 
    return []

#
# 2nd METHOD
# will be used in searchAgents.py (Q8)
#
def findingDistance(position, foods):
    index = 0
    final_dist = None
    for i in range(len(foods)):
    	distance = util.manhattanDistance(position, foods[i])
    	if final_dist == None or final_dist > distance:
      	    final_dist = distance
      	    index = i
    return index, final_dist


