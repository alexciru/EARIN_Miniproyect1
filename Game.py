class Game:

    def __init__(self):
        self.initial_state = None #todo change game creator
        # we should save different games with different number of rows and different number of blank spaces
        return

    def checksolution(self, solution):
        #this function should check if the answer is correct or no
        self.check_collum(solution)
        self.check_row(solution)
        self.check_if_unique(solution)
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
    