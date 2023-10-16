# Written by Rennie Kipchirchir
# Date 16/10/2023
# file contains the implementaion of a priority queue using heapq

import heapq

class Priority_queue:
    """
    A class meant to implement functionality of a priority queue using the 
    heapq python library.
    """

    def __init__(self):
        """
        @purpose: intializes an empty priority queue
        """
        self.elements = []
    
    def empty(self):
        """
        @purpose: checks if the priority queue is empty

        @return : True if the queue is empty false if otherwise
        """
        return len(self.elements) == 0
    
    def push(self, item, priority):
        """
        @purpose: inserts an item into the priotity queue using the provided
                  priority
        @param: item -> item to be inserted
                priority -> priority of the item
        """
        heapq.heappush(self.elements, (priority, item))

    def pop(self):
        """
        @purpose: pops the item with the smallest priority
        @param: the item with the smallest priority
        @NOTE: items with smallest cost are regarded as ones with 
                the  highest priority
        """
        return heapq.heappop(self.elements)[1] #pops item with smallest cost