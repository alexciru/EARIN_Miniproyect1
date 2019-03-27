
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
    print(testgame)


    test_root = Node(testgame)
    test_root.print()







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