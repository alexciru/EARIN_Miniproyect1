    

class Node:
    # This class represents the node of the graph and have information about the state of the game
    # and the node child if it have one.
    def __init__(self, state):

        self.state = state      # Represented by a matrix the actual state of the game
        self.left_child  = None # The left child , has the same state as the parent but with an 0 in the next following blank space
        self.right_child = None # The right child , has the same state as the parent but with an 1 in the next following blank space
        return

    def create_left_child(self, parent_state):

        for row in parent_state:
            for space in row:
                if space == -1:
                    space = 0
                    new_child = Node(parent_state)
                    self.left_child = new_child
                    return 

        #if dont found in the loop it means the matrix is completed
        self.left_child = None
        return

    def create_right_child(self, parent_state):
        for row in parent_state:
            for space in row:
                if space == -1:
                    space = 1
                    new_child = Node(parent_state)
                    self.right_child = new_child   #we add the child with the state changed
                    return 
        
        #if dont fonund free space means the matrix is completed
        self.create_rightChild = None
        return


    def create_node_child_rec(self, new_state):
        self.create_left_child
        if self.left_child == None:
            return

        self.create_right_child
        if self.right_child == None:
            return

        self.create_node_child_rec(self.left_child)
        self.create_node_child_rec(self.left_child)
        return
        
    def print(self):
        print("State: " + str(self.state))
        if self.right_child == None:
            return

        self.right_child.print
        self.left_child.print

        return
        


class Graph:
    # This class will create the graph with all the states using
    def __init__(self, initial_game_state):
        self.root = Node(initial_game_state)
        self.create_graph(initial_game_state)
        return

    def create_graph(self, initial_game_state): 
        self.root.create_node_child_rec(initial_game_state)
        
        return

    
        




    

#Algorith


def breadth_first_search(graph, solution):
    return

def A_search(graph):
    # This algorithm will be called in the formed search
    return


#Heuristic function

# Creo que para la funcion heuristica deberiamos comprobar cuantas casillas estan bien,
# cuantas estan mal y cuantas estan sin completar


    