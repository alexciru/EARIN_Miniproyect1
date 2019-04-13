class Game:

    def __init__(self):
        self.initial_state = None #todo change game creator
        self.list_games = []
        # we should save different games with different number of rows and different number of blank spaces
        return

    def add_game(self, initial_game_state):
        self.list_games.append(initial_game_state)

    def checksolution(self, solution):
        #this function should check if the answer is correct or no
        # TODO completar comprobar solucion
        return


    def check_row(self, solution, n_row):
        lenght = len(solution)
        last_element = solution[n_row][0]
        counter = 1
        
        for i in range(1, lenght):
            if(solution[n_row][i] == last_element):
                counter += counter
            else:
                last_element = solution[n_row][i]
                counter = 1

            if( counter > 2):
                print("Element more that 2 elemetns in the [%d][%d] ", n_row, i)
                # TODO decicdir que hacer cuando encuentra un elemento
                # this function should check if there is the same number of 0 and 1 in a row and see if
                # there is no more that two same digits togueter

        print("No elements in the same row")
        return



    def check_collum(self, solution, n_collum):
        lenght = len(solution)
        last_element = solution[0][n_collum]
        counter = 1
        
        for i in range(1, lenght):
            if(solution[i][n_collum] == last_element):
                counter += counter
            else:
                last_element = solution[i][n_collum]
                counter = 1

            if( counter > 2):
                print("Element more that 2 elemetns in the [%d][%d] ", i, n_collum)
                # TODO decicdir que hacer cuando encuentra un elemento
                # this function should check if there is the same number of 0 and 1 in a row and see if
                # there is no more that two same digits toguete1r

        print("No elements in the same collum")
        # this function should check if there is the same number of 0 and 1 in a collum and see if
        # there is no more that two same digits togueter
        return



    def check_if_unique(self, solution):
        # TODO comprobar si las columnas son unicas o no
        #check if every row and every collum is unique
        return
    
