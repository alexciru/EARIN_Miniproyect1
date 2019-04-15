# File: main.py
# Authors: Alejandro Cirugeda & Juancarlos Quintana
# Description:
# This is the main function of the problem. It will execute 3 different puzzle
# inceasing the difficulty and the computantional difficuty.

from Node import Node
from Game import *
import time


# We create 3 different games with his own solutions
# Game 1: 5  blank spaces
# Game 2: 13 blank spaces
# Game 3: 17 blank spacesa
game1 = [[1, 0,-1, 1,-1, 0],
        [ 1, 1, 0, 0, 1, 0],
        [ 0, 0, 1, 1, 0, 1],
        [ 0, 1, 0, 1,-1, 1],
        [ 1,-1, 1, 0, 1, 0],
        [ 0, 1, 0, 0,-1, 1]]

solution1 =[[ 1, 0, 1, 1, 0, 0],
            [ 1, 1, 0, 0, 1, 0],
            [ 0, 0, 1, 1, 0, 1],
            [ 0, 1, 0, 1, 0, 1],
            [ 1, 0, 1, 0, 1, 0],
            [ 0, 1, 0, 0, 1, 1]]

game2 =     [[0,-1, 1,-1, 0, 1],
            [ 1,-1, -1, 0, 1, 0],
            [-1, 1, 1,-1, 1, 0],
            [-1,-1, 0, 1,-1, 1],
            [ 0,-1, 1,-1, 0, 1],
            [ 1,-1, 0, 1,-1, 0]]

solution2 = [[0, 0, 1, 1, 0, 1],
            [ 1, 1, 0, 0, 1, 0],
            [ 0, 1, 1, 0, 1, 0],
            [ 1, 0, 0, 1, 0, 1],
            [ 0, 1, 1, 0, 0, 1],
            [ 1, 0, 0, 1, 1, 0]]

game3 =     [[0,-1, 1, 0,-1, 0],
            [ 0, 1, 1, 0,-1, 1],
            [ 1, 0,-1, 1,-1,-1],
            [ 0,-1, 0,-1,-1,-1],
            [ 1,-1, 1,-1, 0, 1],
            [-1,-1,-1,-1,-1, 0]]

solution3 = [[0, 1, 1, 0, 1, 0],
            [ 0, 1, 1, 0, 0, 1],
            [ 1, 0, 0, 1, 1, 0],
            [ 0, 1, 0, 1, 1, 0],
            [ 1, 0, 1, 0, 0, 1],
            [ 1, 0, 0, 1, 0, 0]]

def main():
    #create the game and add the diferent puzzles
    game = Game()
    game.add_game(game1)
    game.add_game(game2)
    game.add_game(game3)
    game.add_solution(solution1)
    game.add_solution(solution2)
    game.add_solution(solution3)
    
    for i in range(0,3):
        if i == 0:
            initial_root = Node(game1)
            solution = solution1
            print("\n    ---- First puzzle: ----")
            
        elif i == 1:
            initial_root = Node(game2)
            solution = solution2
            print("\n    ---- Second puzzle: ----")
        else:
            initial_root = Node(game3)
            solution = solution3
            print("\n    ---- Third puzzle: ----")

        initial_root.print()
        print("\nWe create the graph with all posible solution, this may take some time")
        initial_root.create_node_child_rec()

        print("Now we look for the solution with Breadth-First")
        start_time = time.time()
        bfs_visited_nodes = breadth_first_search(initial_root, solution)
        end_time = time.time()
        print("    Solution found with BdF visiting " + str(bfs_visited_nodes) + " Nodes")
        print("    Execution time of BdF algorithm: {} ms \n" .format( round(((end_time - start_time)*1000),3))) 
        
        print("Now we will use the informed search with A*:")
        start_time = time.time()
        a_visited_nodes = A_search(initial_root, solution)
        end_time = time.time()
        print("    Solution found with A* visiting " + str(a_visited_nodes) + " Nodes")
        print("    Execution time of A* algorithm: {} ms\n" .format( round((end_time - start_time)*1000, 3))) 
    return

    
if __name__ == '__main__':
    main()
