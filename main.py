from Node import *
#from Node import Graph

from Game import Game


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


    print("Initial state:  ")
    test_root = Node(test_game)
    test_root.print()
    print("Solution:")
    print(test_solution)


    print("We create the graph with the posible solution")
    test_root.create_node_child_rec()

    print("Now we look for the solution with Breadth-First")
    solution = breadth_first_search(test_root, test_solution)

    if solution:
        print("The solution is:")
        solution.print()

    return

    


if __name__ == '__main__':
    main()


"""
testgame = [[ 1, 0, 1, 1, 0, 0],
            [ 1, 1, 0, 0, 1, 0],
            [ 0, 0, 1, 1, 0, 1],
            [ 0, 1, 0, 1, 0, 1],
            [ 1, 0, 1, 0, 1, 0],
            [ 0, 1, 0, 0, 1, 1]]
"""