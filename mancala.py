
from graphics import*

screensizex=700
screensizey=300
dx = 100
dy = 150
colors = ["blue", "green"]
Player_1_List = []
Player_2_List = []
win = GraphWin("MANCALA",screensizex,screensizey)
#win.setBackground(color_rgb(0,0,0))
sides=312
updown=150
txt = Text(Point(sides, updown),"MANCALA BY NATHAN TEKU")
txt.draw(win)
Alternate_players = 1
Score = 3
Board_Score = 0
Points = int(3)

def draw_rec(width_1,width_2,hight_p1,hight_p2,color,text_loc_x,loc_y,text_color,Board_Score):
    pt1 = Point(screensizex - width_1, screensizey - hight_p1)
    pt2 = Point(screensizex - width_2 , screensizey - hight_p2)
    square = Rectangle(pt1,pt2)
    square.setFill(color)
    label_1 = Text(Point(text_loc_x,loc_y),Board_Score)
    label_1.setTextColor(text_color)
    label_1.setSize(30)
    Player_1_List.append(Board_Score)
    square.draw(win)
    label_1.draw(win)

def initialize_Mancala_Board():
    # sfirst player
    draw_rec(650, 600, dy, 25, "green", 75, 200, "white", Board_Score)
    draw_rec(590, 525, 75, 25, "green", 142, 250, "white", Score)
    draw_rec(510, 445, 75, 25, "green", 223, 250, "white", Score)
    draw_rec(430, 365, 75, 25, "green", 304, 250, "white", Score)
    draw_rec(350, 285, 75, 25, "green", 382, 250, "white", Score)
    draw_rec(270, 205, 75, 25, "green", 463, 250, "white", Score)

    # second player
    draw_rec(140, 195, dy, 25, "blue", 532, 200, "white", Board_Score)
    draw_rec(270, 205, 80, 130, "blue", 463, 195, "white", Score)
    draw_rec(350, 285, 80, 130, "blue", 382, 195, "white", Score)
    draw_rec(430, 365, 80, 130, "blue", 304, 195, "white", Score)
    draw_rec(510, 445, 80, 130, "blue", 223, 195, "white", Score)
    draw_rec(590, 525, 80, 130, "blue", 142, 195, "white", Score)



def display_Mancala(mancala_borad):
    # Player 1
    draw_rec(650, 600, dy, 25, "green", 75, 200, "white", mancala_borad[11])
    draw_rec(590, 525, 75, 25, "green", 142, 250, "white", mancala_borad[0])
    draw_rec(510, 445, 75, 25, "green", 223, 250, "white", mancala_borad[1])
    draw_rec(430, 365, 75, 25, "green", 304, 250, "white", mancala_borad[2])
    draw_rec(350, 285, 75, 25, "green", 382, 250, "white", mancala_borad[3])
    draw_rec(270, 205, 75, 25, "green", 463, 250, "white", mancala_borad[4])

    # second player
    draw_rec(140, 195, dy, 25, "blue", 532, 200, "white", mancala_borad[5])
    draw_rec(270, 205, 80, 130, "blue", 463, 195, "white", mancala_borad[6])
    draw_rec(350, 285, 80, 130, "blue", 382, 195, "white", mancala_borad[7])
    draw_rec(430, 365, 80, 130, "blue", 304, 195, "white", mancala_borad[8])
    draw_rec(510, 445, 80, 130, "blue", 223, 195, "white", mancala_borad[9])
    draw_rec(590, 525, 80, 130, "blue",142, 195, "white", mancala_borad[10])


def couterclockwise_distribute_chips(pit, Mancala_board,player):
    chips =Mancala_board[pit]
    Mancala_board[pit] = Mancala_board[pit] - chips
    player_1_manchala_store = 11
    player_2_manchala_store = 5
    while chips > 0:
        if player == 1 and pit == 4 :
           pit = pit + 2
        elif player == 2 and pit == 10 :
           pit = pit + 2
        else:
          pit = pit + 1
        if pit > 11:
            pit = pit % 12
        if player == 1 and Mancala_board[pit] == 0 and chips == 1:
                    Mancala_board[player_1_manchala_store] = Mancala_board[player_1_manchala_store] + 1
        elif player == 2 and Mancala_board[pit] == 0 and chips == 1:
                    Mancala_board[player_2_manchala_store] = Mancala_board[player_2_manchala_store] + 1
        else:
            Mancala_board[pit] = Mancala_board[pit] + 1
        chips = chips - 1

    return  Mancala_board


def validate_player_pits(player,pit):
    if player == 1:
        if pit not in range(0,5):
            return False
        return True

    if player == 2:
        if pit not in range(6,11):
            return False
        return True

def Mancala_board():
    # Mancala board is represented by List
    return [3, 3, 3, 3, 3, 0, 3, 3, 3, 3, 3, 0]

def pick_A_winner(Mancala_board):
    if Mancala_board[5] == 3 and Mancala_board[11] == 3 :
       print("It's a tie")
       return True
    if Mancala_board[5] == 3:
        print("Player 2 Won ")
        return True
    if Mancala_board[11] == 3 :
       print("Player 1 Won ")
       return True
    return False

def pick_player_and_pit(board,Alternate_players):
    not_done = 1
    while not_done:
        rem = Alternate_players %2
        if rem == 1:
            player = 1
        else:
             player = 2

        if  player == 1:
            pit    = int(input("Player 1: Enter position to start moving chips at : positions --> 1-5 "))
            pit = pit - 1
            valid_pit = validate_player_pits(player, pit)
            if valid_pit == 0:
              print("non valid pit < enter player 1 valid pit > ")
              continue
        else:
            pit = int(input("Player 2: Enter position to start moving chips at : positions --> 7-11 "))
            pit = pit - 1
            valid_pit = validate_player_pits(player, pit)
            if valid_pit == 0:
                print("non valid pit < enter player 2 valid pit > ")
                continue

        mancala_borad = couterclockwise_distribute_chips(pit,board,player)
        display_Mancala(mancala_borad)
        done = pick_A_winner(mancala_borad)
        if done:
            not_done = 0
            return True

        Alternate_players = Alternate_players +1




def run():

    initialize_Mancala_Board()
    new_board = Mancala_board()
    done =  pick_player_and_pit(new_board,Alternate_players)
    if done:
       print('program sucessfully executed')
       # quit()


run()
win.getMouse()