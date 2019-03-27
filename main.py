from Node import Node 
from Node import Graph
from Game import Game


# With this game we should check if the check games function works and how do we create the game
testgame = [[ 1,-1, 1, 1,-1, 0],
            [ 1, 1, 0, 0, 1, 0],
            [ 0, 0,-1, 1, 0, 1],
            [ 0, 1, 0, 1,-1, 1],
            [ 1, 0,-1, 0, 1, 0],
            [ 0, 1, 0, 0, 1, 1]]



def main():

    print("Initial state:  ")
    test_root = Node(testgame)
    test_root.print()

    
    # print("")
    # test_root.create_left_child()
    # test_root.print()

    # print("")
    # test_root.create_right_child()
    # test_root.print()
    print("We execute the recursive funtion")

    test_root.create_node_child_rec()
    print("")
    test_root.print()

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