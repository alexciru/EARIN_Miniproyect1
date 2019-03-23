
class Node:
    # This class represents the node of the graph and have information about the state of the game
    # and the node child if it have one.


    State        # Represented by a matrix the actual state of the game
    leftChild    # The left child , has the same state as the parent but with an 0 in the next following blank space
    rightChild   # The right child , has the same state as the parent but with an 1 in the next following blank space

    def __init__(self, state):
        return

    def create_leftChild(self, childState):
        
        return

    def create_rightChild(self, childState):
        return


class Game:

    initial_state 

    def __init__(self, numberRows):
        # we should save different games with different number of rows and different number of blank spaces
        return

    def checksolution(self, solution):
        #this function should check if the answer is correct or no
        self.check_collum(self, solution)
        self.check_row(self, solution)
        self.check_if_unique(self, solution)
        return


    def check_row(self, solution):
        # this function shouold check if there is the same number of 0 and 1 in a row and see if
        # there is no more that two same digits togueter

        return

    def check_collum(self, solution):
        # this function shouold check if there is the same number of 0 and 1 in a collum and see if
        # there is no more that two same digits togueter
        return

    def check_if_unique(self, solution):
        #check if every row and every collum is unique
        return
    



#Algorith


def breadth_first_search(graph, solution):
    # This algorithm will be called in the informed search
    queue, visited = set()
    while queue
        node = queue.pop(0)
        if vertex not in visited:
            visited.add(node)
            #check solution

            #TODO bfs

            #queue.extend(graph[vertex] - visited)
    
    return visited

def A_search(graph):
    # This algorithm will be called in the formed search
    return


#Heuristic function

# Creo que para la funcion heuristica deberiamos comprobar cuantas casillas estan bien,
# cuantas estan mal y cuantas estan sin completar.




    