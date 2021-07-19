

class Board():
    def __init__(self):
        self.board_game = []
        self.board_dict = {}


    def board(self):
        row_wise = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        column_wise = [1,2,3,4,5,6]
        for i,k in enumerate(row_wise):
            for z in column_wise:
                coordinate = (i,z)
                self.board_game.append(coordinate)
        for i in range(len(self.board_game)):
            self.board_dict[self.board_game[i]] = ''        
        
        
        

    def piece_drop(self, board_column, color):
        #coord = (board_column,row_location)
        
        
        
        for i in reversed(range(1,7)):
            if self.board_dict[(board_column, i)] == '':
                self.board_dict[(board_column, i)] = ''
            else:
                self.board_dict[(board_column, i)] = color
                print(self.board_dict)
                
        
        


    def win_checker(self):

        #Vertical Logic

        coords_to_iterate = list(self.board_dict.keys())
        count_red = 0
        count_yellow = 0 
        for i in range(len(self.board_game)):
            if self.board_dict[coords_to_iterate[i]] == 'red':
                count_red += 1
                if count_red == 4:
                    red_won = 'Red Wins!'
                    return red_won
            else:
                count_red = 0 

        for i in range(len(self.board_game)):
            if self.board_dict[coords_to_iterate[i]] == 'yellow':
                count_yellow += 1
                if count_yellow == 4:
                    yellow_won = 'Yellow Wins!'
                    return yellow_won
            else:
                count_yellow = 0 

            
        #Horizonatal Logic
        for i in range(0,7):
            for z in range(1,6,5):
                    coords_to_check = (i,z)
                    if self.board_dict[coords_to_check] == 'red':
                        count_red += 1
                        if count_red == 4:
                            red_won = 'Red Wins!'
                            return red_won
                    else:
                        count_red = 0 

        for i in range(0,7):
            for z in range(1,6,5):
                    coords_to_check = (i,z)
                    if self.board_dict[coords_to_check] == 'yellow':
                        count_yellow += 1
                        if count_yellow == 4:
                            yellow_won = 'Yellow Wins!'
                            return yellow_won
                    else:
                        yellow_red = 0 
        
        #45 degree logic 


 


        
        






new_game = Board()
new_game.board()


x = None
while x != 'done':
    board_column = int(input('Please input a column number from (0-6) '))
    color = input('please input a color red or yellow ')
    new_game.piece_drop(board_column, color)

    vz = new_game.win_checker()
    if vz != None:
        print(vz)
        x = 'done'
    




        
            

            








