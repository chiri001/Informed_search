
# Written by Rennie Kipchirchir
# Date 16/10/2023
# file contains PancakeProblem class. It defines a search problem

class PancakeProblem:
    """
        PancakeProblem class defines a pancakes search problem, where the goal
        is to have the pancakes arranged in a descending manner. This means
        largest pancakes at the bottom and smallest at the top
    """

    def __init__(self, initial_state):
        """
        @purpose: initializes PancakeProblem with initial state of pancakes

        @param : takes a list representing the initial order of pancakes
        """

        self.initial_state = initial_state
    
    def goal_test(self, state):
        """
        @purpose: checks whether pancakes are arranged in descending order

        @param : takes a tuple representing the current state of the order 
                 of the pancakes
        @returns : true if ordered in non_increasing order else returns false
        """

        return state == tuple(sorted(self.initial_state, reverse=True))

    def successor(self, state, posn):
        """
        @purpose: finds the succeeding order after flipping pancakes at posn

        @param : state -> tuple repesenting the current order of pancakes
                 posn -> position where the pancake is being flipped
        @returns : tuple containing new state after flip and associated cost
        @NOTE  : assumes cost for every flip to be 1
        """

        if posn < 2:
            return state, 0 #no flip to be done since only one pancake to flip
        
        # splits pancakes and reverse to get new order after flip at posn
        #add new order to remaining part after split
        flipped_pancake = state[:posn+1][::-1] 
        unflipped_pancake = state[posn+1:]
        new_state =  flipped_pancake +  unflipped_pancake
        return tuple(new_state), 1  # returns flipped state and cost of action
    
    def path_cost(self, current_cost):
        """
        @purpose: computes the cost to reach new state from current state

        @param : current_cost -> integer representing the current cost
        @returns : integer representing the new cost
        @NOTE  : assumes cost for every flip to be 1
        """
        return current_cost + 1
    
    def possible_actions(self, state):
        """
        @purpose: find possible positions to flip pancakes

        @param : state -> tuple representing the current order of pancakes
        @returns : list of integers representing possible posn to flip pancake
        """
        return list(range(1, len(state)))  # list of pancake positions

    def heuristic(self, state):
        """
        @purpose: finds an estimated cose to reach goal from given state
        
        @param : state -> a tuple representing the current order of pancakes
        @returns : estimated number of steps to reach the goal
        """
        out_of_order_pancakes = 0  # counts out of order pancakes
        for i in range(1, len(state)):
            if state[i] > state[i - 1]:
                out_of_order_pancakes += 1  # increment out of order pancakes
        return out_of_order_pancakes  # returns out of order pancakes in state

