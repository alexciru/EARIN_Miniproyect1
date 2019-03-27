import copy

class Node:
    # This class represents the node of the graph and have information about the state of the game
    # and the node child if it have one.
    def __init__(self, state):

        self.state = state      # Represented by a matrix the actual state of the game
        self.left_child  = None # The left child , has the same state as the parent but with an 0 in the next following blank space
        self.right_child = None # The right child , has the same state as the parent but with an 1 in the next following blank space
        return

    def create_left_child(self):
        new_state = copy.deepcopy(self.state) # Create new matrix
        n_row, n_collum   = 0, 0  # intialize values to find the blank space
        
        for row in new_state:   
            n_collum = 0
            for space in row:
                if space == -1:
                    print("-1 in {} - {}" .format(n_row, n_collum))
                    
                    new_state[n_row][n_collum] = 0  # We chance the value to 0
                    new_child = Node(new_state)
                    self.left_child = new_child   # We add the child with the state changed
                    return 
                n_collum += 1
            n_row += 1
        
        #if dont fonund free space means the matrix is completed
        print("there is no more child to create")
        self.left_child = None
        return

    def create_right_child(self):

        new_state = copy.deepcopy(self.state) # Create new matrix
    
        n_row, n_collum   = 0, 0  # intialize values to find the blank space
        
        for row in new_state:   
            n_collum = 0
            for space in row:
                if space == -1:
                    # print("-1 in {} - {}" .format(n_row, n_collum))
                    new_state[n_row][n_collum] = 1  # We chance the value to 1
                    new_child = Node(new_state)
                    self.right_child = new_child   # We add the child with the state changed
                    return 
                n_collum += 1
            n_row += 1
        
        #if dont fonund free space means the matrix is completed
        self.right_child = None
        return


    def create_node_child_rec(self):
        if self == None:
            return
        self.create_left_child()
        if self.left_child == None:
            print("No existe hijo izq")
            return

        self.create_right_child()
        if self.right_child == None:
            return

        self.left_child.create_node_child_rec()
        self.right_child.create_node_child_rec()
        return
        
    def print(self):
        if self == None:
            return

        print("State: " + str(self.state))
        
        if self.left_child != None:
            self.left_child.print()

        if self.right_child != None:
            self.right_child.print()

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


    