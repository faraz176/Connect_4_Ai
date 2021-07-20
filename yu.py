import random as r 

class Board():
    def __init__(self):
        self.board_game = []
        self.board_dict = {}
        self.last_dropped = ''
        self.count_red_variable = 1
        self.count_yellow_variable = 1


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
        
        
        
        for i in (range(1,7)):

            if self.board_dict[(board_column, i)] == '':
                self.board_dict[(board_column, i)] = color
                self.last_dropped = (board_column, i)
                print(self.board_dict)
                break
                

        
        


    def win_checker(self):

        #Vertical Logic

        coords_to_iterate = list(self.board_dict.keys())
        count_red = 0
        count_yellow = 0 
        for i in range(len(self.board_game)):
            
            if coords_to_iterate[i-1][0] < coords_to_iterate[i][0]:
                count_red = 0 

            if self.board_dict[coords_to_iterate[i]] == 'red':
                count_red += 1
                if count_red == 4:
                    red_won = 'Red Wins!'
                    return red_won

            
            else:
                count_red = 0 

        for i in range(len(self.board_game)):

            if coords_to_iterate[i-1][0] < coords_to_iterate[i][0]:
                count_yellow = 0 

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
                        count_yellow = 0 
        
        #45 degree logic 
        piece_dropped = self.last_dropped 
        #for i in range(1,5):
        try:
            if self.board_dict[(piece_dropped[0]-1, piece_dropped[1]-1)] == 'red':
                
                self.count_red_variable += 1
                print("red: " + str(self.count_red_variable))
                if self.count_red_variable == 4:
                    red_won = 'Red Won'
                    return red_won
           
                
        except KeyError:
            None

        piece_dropped = self.last_dropped
        #for i in range(1,5):
        try:
            if self.board_dict[(piece_dropped[0]-i, piece_dropped[1]-i)] == 'yellow':
                self.count_yellow_variable += 1
                print("yellow: "+ str(self.count_yellow_variable))
                if self.count_yellow_variable == 4:
                    yellow_won = 'Yellow Won'
                    return yellow_won
            
            
        except KeyError:
            None
            

 


        
    

new_game = Board()
new_game.board()

#turn = 0 
x = None
while x != 'done':
     
    # if turn == 0:
    #     board_column = int(input('Please input a column number from (0-6) '))
    #     color = input('please input a color red or yellow ')
    #     new_game.piece_drop(board_column, color)
    #     turn += 1
    
        board_column = int(input('Please input a column number from (0-6) '))
        color = input('please input a color red or yellow ')
        new_game.piece_drop(board_column, color)
        #turn += 1
    # else:
    #     choose = [0,1,2,3,4,5,6]
    #     color_ai = 'yellow'
    #     ai_column = r.choice(choose)
    #     board_column = ai_column
    #     color = color_ai
    #     new_game.piece_drop(board_column, color)
    #     turn = 0 


        vz = new_game.win_checker()
        if vz != None:
            print(vz)
            x = 'done'
    




        
            

            








