from Node import Node
from Game import *


# With this game we should check if the check games function works and how do we create the game
test_game = [[ 1,-1, 1, 1,-1, 0],
            [ 1, 1, 0, 0, 1, 0],
            [ 0, 0,-1, 1, 0, 1],
            [ 0, 1, 0, 1,-1, 1],
            [ 1, 0,-1, 0, 1, 0],
            [ 0, 1, 0, 0, 1, 1]]

test_solution = [[ 1, 0, 1, 1, 0, 0],
                 [ 1, 1, 0, 0, 1, 0],
                 [ 0, 0, 1, 1, 0, 1],
                 [ 0, 1, 0, 1, 0, 1],
                 [ 1, 0, 1, 0, 1, 0],
                 [ 0, 1, 0, 0, 1, 1]]

def main():

    game = Game()
    game.add_game(test_game)
    game.add_solution(test_solution)
    
    
    game.print_game(0)
    test_root = Node(test_game)
    print("We create the graph with the posible solution")
    test_root.create_node_child_rec()

    print("Now we look for the solution with Breadth-First")
    bfs_visited_nodes = breadth_first_search(test_root, test_solution)
    print("Solution found with BFS visiting " + str(bfs_visited_nodes) + " Nodes")

    
    print("Now we will use the informed search")
    a_visited_nodes = A_search(test_root, test_solution)
    print("Solution found with A* visiting " + str(a_visited_nodes) + " Nodes")

    return

    


if __name__ == '__main__':
    main()
