"""
Extra Credit
You can also add on to your Battleship! program to make it more complex and fun to play.
Here are some ideas for enhancements-maybe you can think of some more!

1. Make multiple battleships: you'll need to be careful because you need to make sure that
you don't place battleships on top of each other on the game board. You'll also want to 
make sure that you balance the size of the board with the number of ships so the game is 
still challenging and fun to play.

2. Make battleships of different sizes: this is trickier than it sounds. All the parts of
the battleship need to be vertically or horizontally touching and you'll need to make sure
you don't accidentally place part of a ship off the side of the board.

3. Make your game a two-player game.

4. Use functions to allow your game to have more features like rematches, statistics and
more!

Some of these options will be easier after we cover loops in the next lesson. Think about
coming back to Battleship! after a few more lessons and see what other changes you can
make!
"""

from random import randint

#declare variables
col_alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"]
score = "0:0"

#declare functions

#generate random row and column
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

#generate battleship size
def random_size(max_size):
    return randint(1, max_size)

#display all boards and statistics
def print_boards():
    print "******** Player 1 ********"
    print "   " + " ".join(col_alpha[:board_size])
    cnt = 1
    for row in game_board1:
        if len(str(cnt)) == 1:
            print " " + str(cnt) + " " + " ".join(row)
        else:
            print str(cnt) + " " + " ".join(row)
        cnt += 1
    print "Ships left: %d" % ship_left1
    print ch1
    print ""
    if selection == 1:
        print "******** Computer ********"
    else:
        print "******** Player 2 ********"
    print "   " + " ".join(col_alpha[:board_size])
    cnt = 1
    for row in game_board2:
        if len(str(cnt)) == 1:
            print " " + str(cnt) + " " + " ".join(row)
        else:
            print str(cnt) + " " + " ".join(row)
        cnt += 1
    print "Ships left: %d" % ship_left2
    print ch2

# search for ship from a spot
def search_ship(spot_x, spot_y, ship_size, search_board):
    for x in range(spot_x - (ship_size - 1), spot_x + (ship_size)):
        for y in range(spot_y - (ship_size - 1), spot_y + (ship_size)):
            if x >= 0 and x < board_size and y >= 0 and y < board_size and \
                search_board[x][y] != " " and (x != spot_x or y != spot_y):
                return True
    return False

# search for coordinates
def search_coor(x, y, lst):
    xy = str(x + 1) + col_alpha[y]
    for i in lst:
        for j in i:
            if j == xy:
                return str(lst.index(i)) + "_" + str(i.index(j))
    return False
    
# random chance for getting nearby coordinate after shock wave
def get_random_coor(tmp_ship):
    x = randint(1, 2)       # random chance (50% chance here)
    print x
    if x == 1:              # or any number between random chance
        i = randint(0, len(tmp_ship) - 1)
        if len(tmp_ship[i]) > 0:
            j = randint(0, len(tmp_ship[i]) - 1)
            tmp_x = int(tmp_ship[i][j][:-1]) + randint(-1, 1)               # + random number
            tmp_y = col_alpha.index(tmp_ship[i][j][-1:]) + randint(-1, 1)   # for nearby coordinate
            if tmp_x < 1:
                tmp_x = 1
            if tmp_y < 0:
                tmp_y = 0
            if tmp_x > board_size:
                tmp_x = board_size
            if tmp_y >= board_size:
                tmp_y = board_size - 1
            return str(tmp_x) + col_alpha[tmp_y]
    return False

# change formation
def change_formation(tmp_ship, tmp_size):
    new_ships = []
    tmp_cnt = 0
    for i in range(1000):
        new_ship = []
        if len(tmp_ship[tmp_cnt]) > 0:
            empty_spot = True
            tmp_x = randint(0, board_size - 1)
            tmp_y = randint(0, board_size - 1)
            if tmp_x < tmp_size[tmp_cnt]:
                tmp_x = tmp_size[tmp_cnt]
            if tmp_y < tmp_size[tmp_cnt]:
                tmp_y = tmp_size[tmp_cnt]
            if tmp_x > board_size - tmp_size[tmp_cnt]:
                tmp_x = board_size - tmp_size[tmp_cnt]
            if tmp_y > board_size - tmp_size[tmp_cnt]:
                tmp_y = board_size - tmp_size[tmp_cnt]
            for j in range(len(new_ships)):
                for x in range(len(new_ships[j])):
                    ship_x = int(new_ships[j][x][:-1]) - 1
                    ship_y = col_alpha.index(new_ships[j][x][-1:])
                    if ship_x >= tmp_x - tmp_size[tmp_cnt] and ship_x <= tmp_x + tmp_size[tmp_cnt] and \
                        ship_y >= tmp_y - tmp_size[tmp_cnt] and ship_y <= tmp_y + tmp_size[tmp_cnt]:
                        empty_spot = False
                        break
                if not empty_spot:
                    break
            if empty_spot:
                ship_x = tmp_x - int(tmp_ship[tmp_cnt][0][:-1])
                ship_y = tmp_y - col_alpha.index(tmp_ship[tmp_cnt][0][-1:])
                for j in range(len(tmp_ship[tmp_cnt])):
                    new_ship.append(str(int(tmp_ship[tmp_cnt][j][:-1]) + ship_x) + col_alpha[col_alpha.index(tmp_ship[tmp_cnt][j][-1:]) + ship_y])
                new_ships.append(new_ship)
                tmp_cnt += 1
        else:
            new_ships.append([])
            tmp_cnt += 1
        if tmp_cnt == len(tmp_ship):
            break
    return new_ships


#welcome and selection screen
print "**********************"
print "***  Battleship 2  ***"
print "**********************"
print ""

for matches in range(1000):
    # reset variables
    game_board1 = []
    game_board2 = []
    ship1 = []
    ship_size1 = []
    ship2 = []
    ship_size2 = []
    board_size = 5
    ships = 1
    ship_max_size = 1
    ch1 = "P1:  Fire at will! Fire at will!"
    ch2 = "Com: Come on!!"
    player = 1
    toggle = " "
    round_cnt = 1
    revenge = False
    recharge1 = False
    recharge2 = False
    shoot_x1 = []
    shoot_y1 = []
    shoot_x2 = []
    shoot_y2 = []
    shockwave1 = False
    shockwave2 = False
    exit = False

    # print menus
    print "Select Play Mode:"
    print "(1) Player vs. Computer"
    print "(2) Player vs. Player"
    print "* Anytime you can press 'q' or 'Q' for quiting this game."

    #getting selection
    for i in range(5):
        selection = raw_input("Enter your play mode(1 or 2): ")
        if selection == "1" or selection == "2":
            break
        elif selection.lower() == "q":
            print "Sys: That's too bad. Hope to see you soon!"
            exit = True
            break
        if i == 4:
            print "Sys: You don't want to play this game. Do you?"
            exit = True
            break
    if exit:
        break
    selection = int(selection)
    if selection == 2:
        ch2 = "P2:  Watch out!!"
    print ""

    #getting level selection
    #Easy:     5x5   1 battleship
    #Advanced: 10x10 5 battleships in different sizes
    #Hell:     20x20 9 battleships in different sizes and will change formation
    print "Select Game Mode:"
    print "(1) Easy Mode"
    print "(2) Advanced Mode"
    print "(3) Hell Mode"
    for i in range(5):
        gamemode = raw_input("Enter your game mode(1, 2 or 3): ")
        if gamemode == "1" or gamemode == "2" or gamemode == "3":
            break
        elif gamemode.lower() == "q":
            print "Sys: That's too bad. Hope to see you soon!"
            exit = True
            break
        if i == 4:
            print "Sys: You don't really want to play this game. Do you?"
            exit = True
            break
    if exit:
        break
    gamemode = int(gamemode)
    if gamemode == 2:
        board_size = 10
        ships = 5
        ship_max_size = 2
        gamemode = "Advanced Mode"
    elif gamemode == 3:
        board_size = 20
        ships = 9
        ship_max_size = 3
        gamemode = "Hell Mode"
    else:
        gamemode = "Easy Mode"
    ship_left1 = ships
    ship_left2 = ships
    print ""

    # initialize
    for player in range(2):
        board = []
        ship_cnt = 0

        # create full size of blank board
        for x in range(board_size):
            board.append([" "] * board_size)

        # generate ships locations
        for i in range(1000):    # assume we haven't learned while loop yet
            empty_spot = False
            tmp_row = random_row(board)
            tmp_col = random_col(board)
            tmp_size = random_size(ship_max_size)
            gap = 1
    
            #check if tmp ship is over existing ships
            if board[tmp_row][tmp_col] == " " and tmp_row + tmp_size - 1 < board_size and \
                tmp_col + tmp_size - 1 < board_size and not search_ship(tmp_row, tmp_col, tmp_size + gap, board):
                empty_spot = True
    
            #place the ship
            if empty_spot:
                for x in range(tmp_size + gap * 2):     # layer out ship spot include gaps
                    for y in range(tmp_size + gap * 2):
                        if tmp_row - gap + x >= 0 and tmp_row - gap + x < board_size and \
                            tmp_col - gap + y >= 0 and tmp_col - gap + y < board_size and \
                            board[tmp_row - gap + x][tmp_col - gap + y] == " ":
                            board[tmp_row - gap + x][tmp_col - gap + y] = "-"
                tmp_ship = []   # for ships' coordinate
                for x in range(tmp_size):               # place ship in the middle of layer out
                    for y in range(tmp_size):
                        board[tmp_row + x][tmp_col + y] = "S"
                        tmp_ship.append(str(tmp_row + x + 1) + col_alpha[tmp_col + y])
                if player == 0:
                    ship1.append(tmp_ship)
                    ship_size1.append(tmp_size)
                else:
                    ship2.append(tmp_ship)
                    ship_size2.append(tmp_size)
                ship_cnt += 1
            if ship_cnt == ships:
                break

        # replace all spots with "O"
        board = []
        for x in range(board_size):
            board.append([toggle] * board_size)
        if player == 0:             # can't assign board to both game board at the same time
            game_board1 = board
        else:
            game_board2 = board

    print_boards()

    # Everything from here on should go in your for loop!
    # Be sure to indent four spaces!
    for round in range(1000):    # assume we haven't learned while loop yet
        act = True
        cf = False
        print "%s  Round: %d  Score: %s" % (gamemode, round_cnt, score)
        print "commands: (Q): Quit game  (T): Toggle game board (S): Shock wave"
        if player == 1:
            if recharge1:
                print "Sys: Player1, recharge for one round!"
            elif shockwave1:
                print "P1:  Shock wave, launch!!!"
            else:
                guess = raw_input("Sys: Player1, Type in firing coordinate (ex. 3A): ")
        elif selection == 2:
            if recharge2:
                print "Sys: Player2, recharge for one round!"
            elif shockwave2:
                print "P2:  Shock wave, launch!!!"
            else:
                guess = raw_input("Sys: Player2, Type in firing coordinate (ex. 3A): ")
        else:
            if recharge2:
                print "Sys: Computer is recharging ......"
            elif shockwave2:
                print "Com: Shock wave, launch!!!"
            else:
                guess = str(random_row(game_board1) + 1) + col_alpha[random_col(game_board1)]
                print "Sys: Computer is firing at ...... " + guess

        if not ((player == 1 and recharge1) or (player == 2 and recharge2) or \
            (player == 1 and shockwave1) or (player == 2 and shockwave2)):
            if guess.lower() == "q":
                print "Sys: That's too bad. Hope to see you soon!"
                exit = True
                break
            elif guess.lower() == "s":              # shock wave: charge for one round and
                if player == 1:                     # fire a shock wave, opponent will stun 
                    shockwave1 = True               # for one round and have chance to get
                    recharge1 = True                # opponent's nearby coordinate
                else:
                    shockwave2 = True
                    recharge2 = True
            elif guess.lower() == "t":
                if toggle == " ":
                    toggle = "O"
                else:
                    toggle = " "
                for i in range(len(game_board1)):
                    for j in range(len(game_board1[i])):
                        if game_board1[i][j] != "X":
                            game_board1[i][j] = toggle
                        if game_board2[i][j] != "X":
                            game_board2[i][j] = toggle
                act = False
                print_boards()
            else:
                try:
                    guess_row = int(guess[:-1]) - 1
                    guess_col = col_alpha.index(guess.upper()[-1:])
                    if guess_row < 0 or guess_row >= board_size or guess_col < 0 or guess_col >= board_size:
                        print "Sys: Out of range, please try again!"
                        act = False
                except ValueError:
                    print "Sys: Please type in a correct coordinate!"
                    act = False

        # show "X" in display board and check if it hits, then print conversation for each conditions
        if act:
            # firing cross-shape beams for revenge, that means firing at 5 spots
            if revenge and not (shockwave1 or shockwave2):
                if recharge1 or recharge2:
                    if recharge1:
                        recharge1 = False
                        ch2 = ch2[:5] + "Fire! Quick!!"
                        player = 2
                    if recharge2:
                        recharge2 = False
                        ch1 = ch1[:5] + "Fire! Quick!!"
                        player = 1
                        round_cnt += 1
                else:
                    revenge = False
                    if guess_row == 0:
                        guess_row = 1
                    elif guess_row == board_size - 1:
                        guess_row = board_size - 2
                    if guess_col == 0:
                        guess_col = 1
                    elif guess_col == board_size - 1:
                        guess_col = board_size - 2
                    tmp_x = [guess_row - 1, guess_row, guess_row, guess_row, guess_row + 1]
                    tmp_y = [guess_col, guess_col - 1, guess_col, guess_col + 1, guess_col]
                    if gamemode == "Hell Mode":         # keep only 20 shots on display board
                        if player == 1:
                            shoot_x2.append(tmp_x)
                            shoot_y2.append(tmp_y)
                            if len(shoot_x2) > 20:
                                if type(shoot_x2[0]) == list:
                                    for tmp_xy in range(len(shoot_x2[0])):
                                        game_board2[shoot_x2[0][tmp_xy]][shoot_y2[0][tmp_xy]] = " "
                                else:
                                    game_board2[shoot_x2[0]][shoot_y2[0]] = " "
                                del(shoot_x2[0])
                                del(shoot_y2[0])
                        else:
                            shoot_x1.append(tmp_x)
                            shoot_y1.append(tmp_y)
                            if len(shoot_x1) > 20:
                                if type(shoot_x1[0]) == list:
                                    for tmp_xy in range(len(shoot_x1[0])):
                                        game_board1[shoot_x1[0][tmp_xy]][shoot_y1[0][tmp_xy]] = " "
                                else:
                                    game_board1[shoot_x1[0]][shoot_y1[0]] = " "
                                del(shoot_x1[0])
                                del(shoot_y1[0])
                    txt = ""
                    for f in range(5):
                        if player == 1:
                            game_board2[tmp_x[f]][tmp_y[f]] = "X"
                            if search_coor(tmp_x[f], tmp_y[f], ship2):
                                tmp_xy = search_coor(tmp_x[f], tmp_y[f], ship2)
                                tmp_x = int(tmp_xy[:tmp_xy.index("_")])
                                tmp_y = int(tmp_xy[-tmp_xy.index("_"):])
            
                                if ship_size2[tmp_x] == 1:
                                    if ship_left2 > 1:
                                        txt += "Oh! No! You sunk one of my battleship!\n"
                                    else:
                                        txt = ""
                                        ch2 = ch2[:5] + "Nooooooo~~~~~!!!"
                                    ship_left2 -= 1
                                elif ship_size2[tmp_x] == 2:
                                    if len(ship2[tmp_x]) > 1:
                                        txt += "Ouch! You damaged my battlecruiser!\n"
                                    else:
                                        if ship_left2 > 1:
                                            txt += "Damn! You sunk one of my battlecruiser!\n"
                                        else:
                                            txt = ""
                                            ch2 = ch2[:5] + "Nooooooo~~~~~!!!"
                                        ship_left2 -= 1
                                else:
                                    if len(ship2[tmp_x]) > 1:
                                        txt += "How dare you! That's my mathership!\n"
                                    else:
                                        if ship_left2 > 1:
                                            txt += "WTF! You sunk one of my mathership! Beware of my revenge!!\n"
                                            revenge = True
                                        else:
                                            txt = ""
                                            ch2 = ch2[:5] + "Nooooooo~~~~~!!!"
                                        ship_left2 -= 1
                                del(ship2[tmp_x][tmp_y])
                        else:
                            game_board1[tmp_x[f]][tmp_y[f]] = "X"
                            if search_coor(tmp_x[f], tmp_y[f], ship1):
                                tmp_xy = search_coor(tmp_x[f], tmp_y[f], ship1)
                                tmp_x = int(tmp_xy[:tmp_xy.index("_")])
                                tmp_y = int(tmp_xy[-tmp_xy.index("_"):])
            
                                if ship_size1[tmp_x] == 1:
                                    if ship_left1 > 1:
                                        txt += "Oh! No! You sunk one of my battleship!\n"
                                    else:
                                        txt = ""
                                        ch1 = ch1[:5] + "Nooooooo~~~~~!!!"
                                    ship_left1 -= 1
                                elif ship_size1[tmp_x] == 2:
                                    if len(ship1[tmp_x]) > 1:
                                        txt += "Ouch! You damaged my battlecruiser!\n"
                                    else:
                                        if ship_left1 > 1:
                                            txt += "Damn! You sunk one of my battlecruiser!\n"
                                        else:
                                            txt = ""
                                            ch1 = ch1[:5] + "Nooooooo~~~~~!!!"
                                        ship_left1 -= 1
                                else:
                                    if len(ship1[tmp_x]) > 1:
                                        txt += "How dare you! That's my mathership!\n"
                                    else:
                                        if ship_left1 > 1:
                                            txt += "WTF! You sunk one of my mathership! Beware of my revenge!!\n"
                                            revenge = True
                                        else:
                                            txt = ""
                                            ch1 = ch1[:5] + "Nooooooo~~~~~!!!"
                                        ship_left1 -= 1
                                del(ship1[tmp_x][tmp_y])
                    if player == 1:
                        if txt == "" and ch2[5:10] != "Noooo":
                            ch2 = ch2[:5] + "Phew~! That was close!"
                        recharge1 = True         # when fired cross-shape beam for revenge, must recharge for one round
                        player = 2
                    else:
                        if txt == "" and ch1[5:10] != "Noooo":
                            ch1 = ch1[:5] + "Phew~! That was close!"
                        recharge2 = True         # when fired cross-shape beam for revenge, must recharge for one round
                        player = 1
                        round_cnt += 1
            else:
                if player == 1:
                    if recharge1:
                        recharge1 = False
                        if shockwave2:
                            shockwave2 = False
                            tmp_coor = get_random_coor(ship1)
                            if tmp_coor:
                                ch2 = ch2[:5] + "Sir, we've got something on radar!! Near " + tmp_coor
                            else:
                                ch2 = ch2[:5] + "Sir, we've got nothing on radar!!"
                        else:
                            ch2 = ch2[:5] + "Fire! Quick!!"
                    elif shockwave1:
                        ch2 = ch2[:5] + "Damn~~!!"
                        recharge2 = True
                    else:
                        if game_board2[guess_row][guess_col] == "X":
                            ch2 = ch2[:5] + "Hey! Are you wasting your ammo? Shoot more of that!!"
                        elif not search_coor(guess_row, guess_col, ship2):
                            ch2 = ch2[:5] + "You missed!"
                        else:
                            tmp_xy = search_coor(guess_row, guess_col, ship2)
                            tmp_x = int(tmp_xy[:tmp_xy.index("_")])
                            tmp_y = int(tmp_xy[-tmp_xy.index("_"):])
            
                            if ship_size2[tmp_x] == 1:
                                if ship_left2 > 1:
                                    ch2 = ch2[:5] + "Oh! No! You sunk one of my battleship!"
                                else:
                                    ch2 = ch2[:5] + "Nooooooo~~~~~!!!"
                                ship_left2 -= 1
                            elif ship_size2[tmp_x] == 2:
                                if len(ship2[tmp_x]) > 1:
                                    ch2 = ch2[:5] + "Ouch! You damaged my battlecruiser!"
                                else:
                                    if ship_left2 > 1:
                                        ch2 = ch2[:5] + "Damn! You sunk one of my battlecruiser!"
                                    else:
                                        ch2 = ch2[:5] + "Nooooooo~~~~~!!!"
                                    ship_left2 -= 1
                            else:
                                if len(ship2[tmp_x]) > 1:
                                    ch2 = ch2[:5] + "How dare you! That's my mathership!"
                                    cf = True           # change formation when damaged
                                else:
                                    if ship_left2 > 1:
                                        ch2 = ch2[:5] + "WTF! You sunk one of my mathership! Beware of my revenge!!"
                                        revenge = True
                                    else:
                                        ch2 = ch2[:5] + "Nooooooo~~~~~!!!"
                                    ship_left2 -= 1
                            del(ship2[tmp_x][tmp_y])
                            if cf:
                                ship2 = change_formation(ship2, ship_size2)
                                cf = False
                        if gamemode == "Hell Mode":         # keep only 20 shots on display board
                            shoot_x2.append(guess_row)
                            shoot_y2.append(guess_col)
                            if len(shoot_x2) > 20:
                                if type(shoot_x2[0]) == list:
                                    for tmp_xy in range(len(shoot_x2[0])):
                                        game_board2[shoot_x2[0][tmp_xy]][shoot_y2[0][tmp_xy]] = " "
                                else:
                                    game_board2[shoot_x2[0]][shoot_y2[0]] = " "
                                del(shoot_x2[0])
                                del(shoot_y2[0])
                        game_board2[guess_row][guess_col] = "X"
                    player = 2
                else:
                    if recharge2:
                        recharge2 = False
                        if shockwave1:
                            shockwave1 = False
                            tmp_coor = get_random_coor(ship2)
                            if tmp_coor:
                                ch1 = ch1[:5] + "Sir, we've got something on radar!! Near " + tmp_coor
                            else:
                                ch1 = ch1[:5] + "Sir, we've got nothing on radar!!"
                        else:
                            ch1 = ch1[:5] + "Fire! Quick!!"
                    elif shockwave2:
                        ch1 = ch1[:5] + "Damn~~!!"
                        recharge1 = True
                    else:
                        if game_board1[guess_row][guess_col] == "X":
                            ch1 = ch1[:5] + "Hey! Are you wasting your ammo? Shoot more of that!!"
                        elif not search_coor(guess_row, guess_col, ship1):
                            ch1 = ch1[:5] + "You missed!"
                        else:
                            tmp_xy = search_coor(guess_row, guess_col, ship1)
                            tmp_x = int(tmp_xy[:tmp_xy.index("_")])
                            tmp_y = int(tmp_xy[-tmp_xy.index("_"):])
                
                            if ship_size1[tmp_x] == 1:
                                if ship_left1 > 1:
                                    ch1 = ch1[:5] + "Oh! No! You sunk one of my battleship!"
                                else:
                                    ch1 = ch1[:5] + "Nooooooo~~~~~!!!"
                                ship_left1 -= 1
                            elif ship_size1[tmp_x] == 2:
                                if len(ship1[tmp_x]) > 1:
                                    ch1 = ch1[:5] + "Ouch! You damaged my battlecruiser!"
                                else:
                                    if ship_left1 > 1:
                                        ch1 = ch1[:5] + "Damn! You sunk one of my battlecruiser!"
                                    else:
                                        ch1 = ch1[:5] + "Nooooooo~~~~~!!!"
                                    ship_left1 -= 1
                            else:
                                if len(ship1[tmp_x]) > 1:
                                    ch1 = ch1[:5] + "How dare you! That's my mathership!"
                                    cf = True           # change formation when damaged
                                else:
                                    if ship_left1 > 1:
                                        ch1 = ch1[:5] + "WTF! You sunk one of my mathership! Beware of my revenge!!"
                                        revenge = True
                                    else:
                                        ch1 = ch1[:5] + "Nooooooo~~~~~!!!"
                                    ship_left1 -= 1
                            del(ship1[tmp_x][tmp_y])
                            if cf:
                                ship1 = change_formation(ship1, ship_size1)
                                cf = False
                        if gamemode == "Hell Mode":         # keep only 20 shots on display board
                            shoot_x1.append(guess_row)
                            shoot_y1.append(guess_col)
                            if len(shoot_x1) > 20:
                                if type(shoot_x1[0]) == list:
                                    for tmp_xy in range(len(shoot_x1[0])):
                                        game_board1[shoot_x1[0][tmp_xy]][shoot_y1[0][tmp_xy]] = " "
                                else:
                                    game_board1[shoot_x1[0]][shoot_y1[0]] = " "
                                del(shoot_x1[0])
                                del(shoot_y1[0])
                        game_board1[guess_row][guess_col] = "X"
                    player = 1
                    round_cnt += 1
    
            # print boards again
            print_boards()
    
        # check if no ship left
        if player == 2 and ship_left2 == 0:
            score = str(int(score[:score.index(":")]) + 1) + score[score.index(":"):]
            if selection == 1:
                print_txt = "Sys: You win!"
            else:
                print_txt = "Sys: Player 1 wins!"
            break
        elif player == 1 and ship_left1 == 0:
            score = score[:score.index(":") + 1] + str(int(score[score.index(":") + 1:]) + 1)
            if selection == 1:
                print_txt = "Sys: You lose!"
            else:
                print_txt = "Sys: Player 2 wins!"
            break

    if exit:
        break

    # ask for rematch
    print print_txt + "  Matches: %d  Score: %s" % (matches + 1, score)
    for ask_rematch in range(100):
        rematch = raw_input("Sys: That was fun, right? Wanna play again? (Y/N): ")
        if rematch.lower() == "n":
            print "Sys: That's too bad. Hope to see you soon!"
            exit = True
            break
        elif rematch.lower() == "y":
            break
        else:
            print "Sys: I don't understand you. Please enter again!"
    
    if exit:
        break
