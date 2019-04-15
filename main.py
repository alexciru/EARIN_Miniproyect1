# File: main.py
# Authors: Alejandro Cirugeda & Juancarlos Quintana
# Description:
# This is the main function of the problem. It will execute 3 different puzzle
# inceasing the difficulty and the computantional difficuty.
#
from Node import Node
from Game import *


# We create 3 different games with his own solutions
#Game 1: 5  blank spaces
#Game 2: 9  blank spaces
#Game 3: 17 blank spacesa
game1 = [[1, 0,-1, 1,-1, 0],
        [ 1, 1, 0, 0, 1, 0],
        [ 0, 0, 1, 1, 0, 1],
        [ 0, 1, 0, 1,-1, 1],
        [ 1,-1, 1, 0, 1, 0],
        [ 0, 1, 0, 0,-1, 1]]

solution1 = [[ 1, 0, 1, 1, 0, 0],
            [ 1, 1, 0, 0, 1, 0],
            [ 0, 0, 1, 1, 0, 1],
            [ 0, 1, 0, 1, 0, 1],
            [ 1, 0, 1, 0, 1, 0],
            [ 0, 1, 0, 0, 1, 1]]

game2 =     [[0,-1, 1, 1, 0, 1],
            [ 1,-1, -1, 0, 1, 0],
            [ 0, 1, 1,-1, 1, 0],
            [ 1, 0, 0, 1,-1, 1],
            [ 0,-1, 1,-1, 0, 1],
            [ 1,-1, 0, 1,-1, 0]]

solution2 = [[0, 0, 1, 1, 0, 1],
            [ 1, 1, 0, 0, 1, 0],
            [ 0, 1, 1, 0, 1, 0],
            [ 1, 0, 0, 1, 0, 1],
            [ 0, 1, 1, 0, 0, 1],
            [ 1, 0, 0, 1, 1, 0]]



game3 =     [[0,-1,-1, 0,-1, 0],
            [-1, 1, 1,-1,-1, 1],
            [ 1, 0, 0, 1, 1, 0],
            [-1,-1,-1,-1,-1,-1],
            [ 1,-1, 1,-1,-1, 1],
            [ 1,-1, 0, 1,-1, 0]]

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
    
    
    game.print_game(0)
    test_root = Node(game1)
    print("We create the graph with the posible solution")
    test_root.create_node_child_rec()

    print("Now we look for the solution with Breadth-First")
    bfs_visited_nodes = breadth_first_search(test_root, solution1)
    print("Solution found with BFS visiting " + str(bfs_visited_nodes) + " Nodes")

    
    print("Now we will use the informed search")
    a_visited_nodes = A_search(test_root, solution1)
    print("Solution found with A* visiting " + str(a_visited_nodes) + " Nodes")

    return

    


if __name__ == '__main__':
    main()
