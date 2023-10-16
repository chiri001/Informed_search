# Written by Rennie Kipchirchir
# Date 16/10/2023
# file contains the implementaion of A* search.

from Pancake import PancakeProblem
from priority_queue import Priority_queue

def a_star_search(problem):
    """
    @purpose: performs a uniform search on the provided problem list

    @param : problem - takes a list containing the unordered list of 
                pancakes
    @return : solution if the list of pancakes can be solved
              FAILURE if the problem cannot be solved or if frontier is 
              empty
    """


    # initialize the frontier using the initial state of problem
    start_state = tuple(problem.initial_state)
    frontier = Priority_queue() #create a queue using my custom class
    frontier.push(start_state, 0)
    
    visited = set() #set to keep track of visited states
    cost_so_far = {start_state: 0}  # track the cost of flips
    
    # loop, fails if the frontier is empty
    while not frontier.empty():

        curr = frontier.pop()
        visited.add(curr) #mark as visited

        #if curr contains the goal state then return curr
        if problem.goal_test(curr):     
            return curr
        
        # for each child
        for  index in problem.possible_actions(curr):
            #get flipped state and action cost for the flip
            new_state, action_cost = problem.successor(curr, index)
            #gets the cost for flipping the pancakes
            new_cost = problem.path_cost(cost_so_far[curr])
            
            #if child is not in frontier/visited
            if new_state not in cost_so_far and new_state not in visited:
                #insert child in frontier
                cost_so_far[new_state] = new_cost
                item_cost = new_cost + problem.heuristic(new_state)
                frontier.push(new_state, item_cost) 

            #if child is in frontier with higher cost
            elif new_state in cost_so_far and new_cost < cost_so_far[new_state]:
                #replace child in frontier with child
                cost_so_far[new_state] = new_cost
                item_cost = new_cost + problem.heuristic(new_state)
                frontier.push(new_state, item_cost) 
     
    return "FAILURE" #no solution


#get input from terminal and run a A* ssearch algorithm to reach goal
initial_stack = input("Enter the Pancake stack order by size i.e 8 4 2"
                        "(size has to be a valid number): ")
initial_stack = list(map(int, initial_stack.split()))

# find solution to problem
problem = PancakeProblem(initial_stack)
solution = a_star_search(problem)


print(f"Pancakes Before rearrangement                    : {initial_stack}")
if solution != "FAILURE":
    print(f"Pancakes Successfully rearranged non-increasingly: {solution}")
else:
    print("No Possible rearrangement to attain goal found")