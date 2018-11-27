# -*- coding: utf-8 -*-

import sys

class Igo_Board: 
    stones = []
    
    class Coordinate:
        alphabet_convert_dict = {
                            "A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7,
                            "I":8, "J":9, "K":10, "L":11, "M":12, "N":13, "O":14,
                            "P":15, "Q":16, "R":17, "S":18
                            }
        
        int_convert_dict = {
                            "1":0, "2":1, "3":2, "4":3, "5":4,
                            "6":5, "7":6, "8":7, "9":8, "10":9,
                            "11":10, "12":11, "13":12, "14":13,
                            "15":14, "16":15, "17":16, "18":17,
                            "19":18
                            }
        
        x = "A B C D E F G H I J K L M N O P Q R S"
        y = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    
    def new_game(self):
        self.stones.clear()
        
        for row in range(19):
            self.stones.append(["+"])
            for clmn in range(18):
                self.stones[row].append("+")
        
        self.turn = "black"
        self.live = True              
        self.coord = self.Coordinate()
        
        return "Starting New Game!"
                
    def change_turn(self):
        if self.turn == "black":
            self.turn = "white"
        elif self.turn == "white":
            self.turn = "black"
        
        print("\nNext is " + self.turn + "'s turn\n")
    
    def place_stone(self, y_alpha, x_int):
        
        y = self.coord.alphabet_convert_dict[y_alpha]
        x = self.coord.int_convert_dict[x_int]
        
        if self.turn == "black":
            self.stones[x][y] = "x"
        elif self.turn == "white":
            self.stones[x][y] = "o"
        
        self.show_board()
        
        self.change_turn()
    
    def show_board(self):
        print('   ' + self.coord.x)
        
        for i, row in enumerate(self.stones):
            if i < 9:
                print(' ' + str(self.coord.y[i]), end=' ')
             
            else:
                print(self.coord.y[i], end=' ')
            
            for stone in row:
               print(stone, end=' ') 
            print(end="\n")
    

            
def main():      
    Game = Igo_Board()
    print(Game.new_game())
    #Game.show_board()
        
    #print(Game.turn)
    
    while Game.live:
        Command = input("\nCommand?:\n")
        
        if Command == "plst":
#            x = int(input("x coordinate? [0-19]:\n"))
#            y = int(input("y coordinate? [0-19]:\n"))
            
            coordinate = input("Coordinate? Input example: J,10\n").split(',')
            
            x_alpha = coordinate[0]
            y_int = coordinate[1]
            
            Game.place_stone(x_alpha, y_int)
            
            print(Game.turn)
        
        elif Command == "stop":
            Game.live = False
            sys.exit("Stopping Game")
            
        elif Command == "help":
            Help = ("\nCommand list:\n\n"
                    "plst: Place stone on board \n"
                    "stop: Stop program \n"
                    "show: Show board \n"
                    "new: Start new game \n"
                    )
            
            print(Help)
            
        elif Command == "show":
            Game.show_board()
        
        elif Command == "new":
            print(Game.new_game())        
            
        else:
            print("Invalid Command\nType 'help' for command list")
            
main()

#TODO
#Add validation for place_stone method
