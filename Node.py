
class Node:
    # This class represents the node of the graph and have information about the state of the game
    # and the node child if it have one.
    
    def __init__(self, state):

        self.state = state      # Represented by a matrix the actual state of the game
        self.left_child  = None # The left child , has the same state as the parent but with an 0 in the next following blank space
        self.right_child = None # The right child , has the same state as the parent but with an 1 in the next following blank space
        return

    def create_leftChild(self, parent_state):

        for row in parent_state:
            for space in row:
                if space == -1:
                    space = 0
                    new_child = Node(parent_state)
                    self.left_child = new_child
                    return

        #if dont found in the loop it means the matrix is completed
        #TODO throw exception
        return

    def create_rightChild(self, parent_state):
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


    