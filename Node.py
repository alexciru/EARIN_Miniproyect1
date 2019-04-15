# File: Node.py
# Authors: Alejandro Cirugeda & Juancarlos Quintana
# Description:
# The class Node will be in charge of storing the searchable space. Will be represented by a graph
# with all the posibles solution to the puzzle

import copy

class Node:
    # This class represents the node of the graph and have information about the state of the game
    # and the node child if it have one and the depth where the node is situated.

    def __init__(self, state):

        self.state = state      # Represented by a matrix the actual state of the game
        self.left_child  = None # The left child , has the same state as the parent but with an 0 in the next following blank space
        self.right_child = None # The right child , has the same state as the parent but with an 1 in the next following blank space
        self.depth       = 0    # The depth of the node that will be use for the informaed search
        return


    def create_left_child(self):
        new_state = copy.deepcopy(self.state) # Create new matrix
        n_row, n_collum   = 0, 0
        
        for row in new_state:   
            n_collum = 0
            for space in row:
                if space == -1:
                    new_state[n_row][n_collum] = 0   # We chance the value to 0
                    new_child = Node(new_state)
                    self.left_child = new_child      # We add the child with the state changed
                    new_child.depth = self.depth + 1 # increase the valjue of the depth
                    return 
                n_collum += 1
            n_row += 1
        
        #if dont found free space, it means the matrix is completed
        self.left_child = None
        return


    def create_right_child(self):
        new_state = copy.deepcopy(self.state) # Create new matrix
        n_row, n_collum   = 0, 0
        
        for row in new_state:   
            n_collum = 0
            for space in row:
                if space == -1:
                    new_state[n_row][n_collum] = 1   # We chance the value to 1
                    new_child = Node(new_state)
                    self.right_child = new_child     # We add the child with the state changed
                    new_child.depth = self.depth + 1 # increase the valjue of the depth
                    return 
                n_collum += 1
            n_row += 1
        
        #if dont fonund free space, it means the matrix is completed
        self.right_child = None
        return


    # This function will create the hole graph from the initial state
    def create_node_child_rec(self):
        if self == None:
            return
        self.create_left_child()
        if self.left_child == None:
            return

        self.create_right_child()
        if self.right_child == None:
            return

        self.left_child.create_node_child_rec()
        self.right_child.create_node_child_rec()
        return
    
    #funtion in charche to print the states
    def print(self):
        if self == None:
            return

        print("State: " + str(self.state))
        if self.left_child != None:
            self.left_child.print()

        if self.right_child != None:
            self.right_child.print()

        return
        

