

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
        
        
        

    def piece_drop(self, board_column, row_location, color):
        coord = (board_column,row_location)
        
            
        if coord in self.board_dict.keys():
            if self.board_dict[coord] != '':
                    
                print(self.board_dict)
                    
                    
            else:
                self.board_dict[coord] = color
                print(self.board_dict)


    def win_checker(self):
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



        
            
            

            
            
            

        




new_game = Board()
new_game.board()
#z = new_game.piece_drop(1, 2, 'red')
#print(z)

x = None
while x != 'done':
    x = input("Please type 'done' to end game ")
    board_column = int(input('Please input a column number from (0-6) '))
    row_location = int(input('Please input a row number (1-6) '))

    color = input('please input a color red or yellow ')
    new_game.piece_drop(board_column, row_location, color)

    vz = new_game.win_checker()
    if vz != None:
        print(vz)
        x = 'done'
    




        
            

            








