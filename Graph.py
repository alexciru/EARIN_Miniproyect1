
class graph:
    # This class will create the graph with all the states using
    def __init__(self, initial_game_state):
        self.root = Node(initial_game_state)
        self.create_graph()
        return

    def create_graph(self): #MAYBE THIS FUNCTION SHOULD BE RECURSIVE

        #TODO start creating the graph with all the posibles solution that may have
        queue = []
        queue.append(self.root)

        #loop
            self.root.create_leftChild(self.root.state)
            self.root.create_rightChild(self.root.state)
            queue.append(self)
        return