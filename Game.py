from PriorityQueue import PriorityQueue
from Node import Node
class Game:

    def __init__(self):
        self.initial_state = None
        self.list_games = []
        self.list_solutions = []
        # we should save different games with different number of rows and different number of blank spaces
        return

    def add_game(self, initial_game_state):
        self.list_games.append(initial_game_state)

    def add_solution(self, solution):
        self.list_solutions.append(solution)

    def print_game(self, index):
        print("Initial state:")
        print (self.list_games[index])
        print("Solution")
        print (self.list_solutions[index])




    

#Algorith


def breadth_first_search(root, solution):
    nodes_visited = 0
    queue = []   # we will store all the nodes that we didnt visit yet
    queue.append(root)

    while queue:
        node = queue.pop(0)
        nodes_visited += 1
        if node.state == solution:
            return nodes_visited
        else :
            queue.append(node.left_child)
            queue.append(node.right_child)
        
    print("Queue empty, solution not found")

    return -1

def A_search(root, solution):
    nodes_visited = 0
    priority = []
    priority.append(root)
    #TODO implement a priority queue
    while len(priority):
        node = priority.pop(0)
        nodes_visited += 1
        if(node.state == solution):
            return nodes_visited
        
        right_child = node.right_child
        left_child  = node.left_child

        if not (left_child == None):
            #TODO change put in the priority queue
            value = g_fution(left_child) + heuristic(left_child)
            priority.append(left_child)
            value = g_fution(right_child) + heuristic(right_child)
            priority.append(right_child)


    print("Queue empty, solution not found")
    return -1
 

# Heuristic function
# Heursitic function will check how many error are in the state and 
# how many blank space are still to be filled
#
def heuristic(node):
    #TODO cambiar function heuristica
    return 2


def g_fution(node):
    #TODO cambiar g function
    counter = len(node.state)

    return counter

