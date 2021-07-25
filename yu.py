import random as r 


class Board():
    def __init__(self, color1,):
        cock = []
        for i in range(1,7):
            for z in range(0,7):
                cock.append([])
        self.color_player_1 = color1
        self.color_player_2 = ''
        self.turn = 0
        self.board_game = []
        self.moves_ready = []
        self.board_dict = {}
        self.last_dropped = ''
        self.count_red_variable = 1
        self.count_yellow_variable = 1
        self.looking_board = cock
        self.game_turn = 0 


    def board(self):
        row_wise = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        column_wise = [1,2,3,4,5,6]
        for i,k in enumerate(row_wise):
            for z in column_wise:
                coordinate = (i,z)
                self.board_game.append(coordinate)
        for i in range(len(self.board_game)):
            self.board_dict[self.board_game[i]] = '' 





    def weird_board(self):

            for i in range(1,7):
                for z in range(0,7):
                    self.looking_board.append([])

                        
            for i in range(len(self.board_game)):
                self.looking_board[i] = self.board_game[i]


    
    def board_look(self):
        
        #Mapping


        
            for i in range(len(self.board_game)):
                if self.looking_board[i] == self.last_dropped:
                    self.looking_board[i] = self.color_player_2


            num_to_iterate = 0
            num_to_end = 6 
            for i in range(1,8):
            
                print(self.looking_board[num_to_iterate:num_to_end])
                num_to_iterate += 6
                num_to_end += 6 



  
        

    def piece_drop(self, board_column):
        #coord = (board_column,row_location)
        
        
        
        for i in (range(1,7)):
            if self.turn == 0:

                if self.board_dict[(board_column, i)] == '':
                    self.board_dict[(board_column, i)] = self.color_player_1
                    self.color_player_2 = self.color_player_1
                    self.last_dropped = (board_column, i)
                    #print(self.board_dict)
                    self.turn +=1
                    break
            else:
                if self.color_player_1 == 'red':
                    color_2 = 'yellow'
                if self.board_dict[(board_column, i)] == '':
                    self.board_dict[(board_column, i)] = color_2
                    self.color_player_2 = color_2
                    self.last_dropped = (board_column, i)
                    #print(self.board_dict)
                    self.turn = 0
                    break

                

   

                
    def availiable_moves(self):
        self.moves_ready = []

        for i in range(0,7):
            for z in range(1,7):

                
                if self.board_dict[(i,z)] == '':
                    space = (i,z)
                    self.moves_ready.append(space)
                    break
        return self.moves_ready
        
    
    
              
        
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
                    red_won = 'red'
                    return red_won

            
            else:
                count_red = 0 

        for i in range(len(self.board_game)):

            if coords_to_iterate[i-1][0] < coords_to_iterate[i][0]:
                count_yellow = 0 

            if self.board_dict[coords_to_iterate[i]] == 'yellow':
                count_yellow += 1
                if count_yellow == 4:
                    yellow_won = 'yellow'
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
                            red_won = 'red'
                            return red_won
                    else:
                        count_red = 0 

        for i in range(0,7):
            for z in range(1,6,5):
                    coords_to_check = (i,z)
                    if self.board_dict[coords_to_check] == 'yellow':
                        count_yellow += 1
                        if count_yellow == 4:
                            yellow_won = 'yellow'
                            return yellow_won
                    else:
                        count_yellow = 0 
        
        #45 degree logic 
        piece_dropped = self.last_dropped 
        try:
            if self.board_dict[(piece_dropped[0]-1, piece_dropped[1]-1)] == 'red':
                
                self.count_red_variable += 1
                print("red: " + str(self.count_red_variable))
                if self.count_red_variable == 4:
                    red_won = 'red'
                    return red_won
           
                
        except KeyError:
            None

        piece_dropped = self.last_dropped
        try:
            if self.board_dict[(piece_dropped[0]-1, piece_dropped[1]-1)] == 'yellow':
                self.count_yellow_variable += 1
                print("yellow: "+ str(self.count_yellow_variable))
                if self.count_yellow_variable == 4:
                    yellow_won = 'yellow'
                    return yellow_won
            
            
        except KeyError:
            None

    # def minimax(self):
    #     if self.turn == 0:
    #         maximizingPlayer = self.color_player_1
    #     if self.turn == 1:
    #         maximizingPlayer = 'yellow'
    #     other_player = 'yellow'
        
    #     if self.win_checker() == other_player:
    #         return {'position': None, 'score': 1 * (len(self.availiable_moves) + 1) if other_player == maximizingPlayer else -1 * (
    #                     len(self.availiable_moves()) + 1)}

    #     elif not self.availiable_moves():
    #         return{'position': None, 'score':0}

    #     if self.color_player_1 == maximizingPlayer:
    #         best = {'position': None, 'score': -math.inf}
        
    #     else:
    #         best = {'position': None, 'score': math.inf}

    #     for possible_move in self.availiable_moves():
    #         self.piece_drop(possible_move)
    #         sim_score = self.minimax(self, other_player)


    #         self.piece_drop[possible_move] = ' '
    #         sim_score['position'] = possible_move

    #         if self.color_player_1 == maximizingPlayer:
    #             if sim_score['score'] > best['score']:
    #                 best = sim_score

    #         else:
    #             if sim_score['score'] < best['score']:
    #                 best = sim_score
        
    #     return best


    def AI(self):
        if self.turn == 1:


            if self.game_turn == 0:
                num_choose = r.randint(0,6)
                best_move = num_choose
                self.game_turn += 1
                return best_move
                

            moves_to_consider = []
            for i in self.moves_ready:
                try:

                    if self.board_dict[i[0], i[1] - 1] == 'yellow':
                        move_possible_1 = 0.8
                        moves_to_consider.append((i, move_possible_1))
                
                    elif self.board_dict[i[0] - 1, i[1]] == 'yellow':
                        move_possible_2 = 0.8
                        moves_to_consider.append((i, move_possible_2)) 

                    elif self.board_dict[i[0] -1,  i[1] -1] == 'yellow':
                        move_possible_3 = 0.8
                        moves_to_consider.append((i, move_possible_3))

                    elif self.board_dict[i[0], i[1] - 1] == 'red':
                        move_possible_4 = 0.8
                        moves_to_consider.append((i, move_possible_4))
                
                    elif self.board_dict[i[0] - 1, i[1]] == 'red':
                        move_possible_5 = 0.6
                        moves_to_consider.append((i, move_possible_5)) 

                    elif self.board_dict[i[0] -1,  i[1] -1] == 'red':
                        move_possible_6 = 0.3
                        moves_to_consider.append((i, move_possible_6))

                except KeyError:
                    None

                   


            # best_move = ''
            # biggest_move = moves_to_consider[0][1]
            # for i in range(len(moves_to_consider)):
            #     if moves_to_consider[i][1] > biggest_move:
            #         biggest_move = moves_to_consider[i][1]
            #         best_move = moves_to_consider[i][0]
            best_move = moves_to_consider

            return best_move
        




                
                


      


            

 


        
    

new_game = Board('red')
new_game.board()
new_game.weird_board()

turn = 0 
x = None
while x != 'done':
     
    if turn == 0:
        board_column = int(input('Please input a column number from (0-6) '))
        new_game.piece_drop(board_column)
        new_game.board_look()
        print(new_game.availiable_moves())
        turn += 1

             
        
    else:
        #print(new_game.availiable_moves())
        # print(new_game.turn)
        print(new_game.AI())

        # board_column = int(input('Please input a column number from (0-6) '))
        # AI_move = new_game.AI()
        # column_AI = AI_move[0]
        # new_game.piece_drop(board_column)
        # new_game.board_look()
        # print(new_game.availiable_moves())
        turn = 0 
    


    vz = new_game.win_checker()
    if vz != None:
        print(vz)
        x = 'done'
    




        
            

            








