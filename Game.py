# File: Game.py
# Authors: Alejandro Cirugeda & Juancarlos Quintana
# Description:
#
#
from queue import PriorityQueue
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
    priority.append((1, root))

    while len(priority):
        min_value = priority[0][0]
        min_index = 0
        for i in range(0, len(priority)):
            print(priority[i][0])
            if  priority[i][0] < min_value:
                min_value = priority[i][0]
                min_index = i
        
        tupla = priority.pop(min_index)
        node = tupla[1]
        nodes_visited += 1
        if(node.state == solution):
            return nodes_visited
        
        right_child = node.right_child
        left_child  = node.left_child

        if not (left_child == None):
            value = g_fution(left_child) + heuristic(left_child, solution)
            #print("Value = " + str(value))
            priority.append((value, left_child))

            value = g_fution(right_child) + heuristic(right_child, solution)
            priority.append((value, right_child))


    print("Queue empty, solution not found")
    return -1
 

# Heuristic function
# Heursitic function will compare the actual state with the solution and count 
# the numer of errors 
def heuristic(node, solution):
    err_counter = 0
    lenght = len(node.state)
    for i in range(0, lenght):
        for j in range(0, lenght):
            if(node.state[i][j] != solution[i][j]):
                err_counter += 1  

    return err_counter


def g_fution(node):

    return node.depth

