
# Ultimate Battleships

def print_ships_to_be_placed():
    print("Ships to be placed:", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Ships to be placed: ")


# elem expected to be a single list element of a primitive type.
def print_single_element(elem):
    print(str(elem), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write(str(elem) + " ")


def print_empty_line():
    print()
    if FILE_OUTPUT_FLAG:
        f.write("\n")


# n expected to be str or int.
def print_player_turn_to_place(n):
    print("It is Player {}'s turn to place their ships.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to place their ships.\n".format(n))


def print_to_place_ships():
    print("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) : \n")
        # There is a \n because we want the board to start printing on the next line.


def print_incorrect_input_format():
    print("Input is in incorrect format, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Input is in incorrect format, please try again.\n")


def print_incorrect_coordinates():
    print("Incorrect coordinates given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect coordinates given, please try again.\n")


def print_incorrect_ship_name():
    print("Incorrect ship name given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect ship name given, please try again.\n")


def print_incorrect_orientation():
    print("Incorrect orientation given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect orientation given, please try again.\n")


# ship expected to be str.
def print_ship_is_already_placed(ship):
    print(ship, "is already placed, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " is already placed, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_outside(ship):
    print(ship, "cannot be placed outside the board, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed outside the board, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_occupied(ship):
    print(ship, "cannot be placed to an already occupied space, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed to an already occupied space, please try again.\n")


def print_confirm_placement():
    print("Confirm placement Y/N :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Confirm placement Y/N : \n")


# n expected to be str or int.
def print_player_turn_to_strike(n):
    print("It is Player {}'s turn to strike.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to strike.\n".format(n))


def print_choose_target_coordinates():
    print("Choose target coordinates :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Choose target coordinates : ")


def print_miss():
    print("Miss.")
    if FILE_OUTPUT_FLAG:
        f.write("Miss.\n")


# n expected to be str or int.
def print_type_done_to_yield(n):
    print("Type done to yield your turn to player {} :".format(n), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Type done to yield your turn to player {} : \n".format(n))


def print_tile_already_struck():
    print("That tile has already been struck. Choose another target.")
    if FILE_OUTPUT_FLAG:
        f.write("That tile has already been struck. Choose another target.\n")


def print_hit():
    print("Hit!")
    if FILE_OUTPUT_FLAG:
        f.write("Hit!\n")


# n expected to be str or int.
def print_player_won(n):
    print("Player {} has won!".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("Player {} has won!\n".format(n))


def print_thanks_for_playing():
    print("Thanks for playing.")
    if FILE_OUTPUT_FLAG:
        f.write("Thanks for playing.\n")


# my_list expected to be a 3-dimensional list, formed from two 2-dimensional lists containing the boards of each player.
def print_3d_list(my_list):
    first_d = len(my_list[0])
    for row_ind in range(first_d):
        second_d = len(my_list[0][row_ind])
        print("{:<2}".format(row_ind+1), end=' ')
        for col_ind in range(second_d):
            print(my_list[0][row_ind][col_ind], end=' ')
        print("\t\t\t", end='')
        print("{:<2}".format(row_ind+1), end=' ')
        for col_ind in range(second_d):
            print(my_list[1][row_ind][col_ind], end=' ')
        print()
    print("", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\t\t", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\nPlayer 1\t\t\t\t\t\tPlayer 2")
    print()

    if FILE_OUTPUT_FLAG:
        first_d = len(my_list[0])
        for row_ind in range(first_d):
            second_d = len(my_list[0][row_ind])
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[0][row_ind][col_ind] + " ")
            f.write("\t\t\t")
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[1][row_ind][col_ind] + " ")
            f.write("\n")
        f.write("   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\t\t   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\nPlayer 1\t\t\t\t\t\tPlayer 2\n")
        f.write("\n")


def print_rules():
    print("Welcome to Ultimate Battleships")
    print("This is a game for 2 people, to be played on two 10x10 boards.")
    print("There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).")
    print("First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.")
    print("Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.")
    print("If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.")
    print("If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.")
    print("Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.")
    print("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.")
    print("The last player to have an unsunk ship wins.")
    print("Have fun!")
    print()

    if FILE_OUTPUT_FLAG:
        f.write("Welcome to Ultimate Battleships\n")
        f.write("This is a game for 2 people, to be played on two 10x10 boards.\n")
        f.write(
            "There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).\n")
        f.write(
            "First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.\n")
        f.write(
            "Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.\n")
        f.write("If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.\n")
        f.write("If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.\n")
        f.write(
            "Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.\n")
        f.write("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.\n")
        f.write("The last player to have an unsunk ship wins.\n")
        f.write("Have fun!\n")
        f.write("\n")


# Create the game
board_size = 10
f = open('UltimateBattleships.txt', 'w')
FILE_OUTPUT_FLAG = True  # You can change this to True to also output to a file so that you can check your outputs with diff.

print_rules()

# Remember to use list comprehensions at all possible times.
# If we see you populate a list that could be done with list comprehensions using for loops, append/extend/insert etc. you will lose points.

# Make sure to put comments in your code explaining your approach and the execution.

# We defined all the functions above for your use so that you can focus only on your code and not the formatting.
# You need to call them in your code to use them of course.

# If you have questions related to this homework, direct them to utku.bozdogan@boun.edu.tr please.

# Do not wait until the last day or two to start doing this homework, it requires serious effort.

try:  # The entire code is in this try block, if there ever is an error during execution, we can safely close the file.
    # DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    
    import copy  # I used deepcopy, as we learned a few weeks ago in class, to store my playerboards.

    liste = [[["-" for i in range(10)] for j in range(10)] for k in range(2)]
# I created a 3 dimensional list for my playboard because the given function was working for 3d nested links

    ship_list = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
    ship_list_ana = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
    shiplist_kopya = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]

    ship_dic = {"Carrier": 5, "Battleship": 4, "Cruiser": 3, "Submarine": 3, "Destroyer": 2}

    player_1_board = []
    player_2_board = []
    already_placed_control = []

    trying = False

    for n in range(1, 3):  
        while len(ship_list) > 0:  # I used while loop until a player place all his/her ships

            print_3d_list(liste)
            print_ships_to_be_placed()

            for i in ship_list:
                print_single_element(i)
            print_empty_line()

            print_player_turn_to_place(n)
            print_to_place_ships()

            ship_choice = input()
            ship_choice_ilk = ship_choice[0].upper()
            ship_choice_kalan = ship_choice[1:].lower()
            ship_choice = ship_choice_ilk + ship_choice_kalan

# I converted my whole input into desired style, making first letter up and other low,
# I would use .capitalize() or .title() but we haven't learned them yet.
            input_list = ship_choice.strip().split()
# in case players input extra spaces i used strip()
            coord = []
            try:  # i used try except to be sure that players won't write any input
                coord = [int(i) for i in input_list[1:3]]  # in any unwanted way.
            except:
                print_incorrect_input_format()
                continue

            if len(input_list) < 4:  # to take at least 4 inputs
                print_incorrect_input_format()
                continue

            if coord[0] > 10 or coord[0] < 1 or coord[1] > 10 or coord[
                1] < 1:  # to make sure that coordinates for ships are convenient
                print_incorrect_coordinates()
                continue

            if input_list[0] not in ship_list_ana:  # to not accept shipnames which are invalid
                print_incorrect_ship_name()
                continue

            if input_list[3] != "h" and input_list[3] != "v":  # to only accept vertical and horizontal
                print_incorrect_orientation()
                continue

            if input_list[0] in already_placed_control:  # each player can use each ships only 1 time
                print_ship_is_already_placed(input_list[0])
                continue

            if input_list[3] == "h" and (ship_dic[input_list[0]] + coord[0] - 1) > 10:
                print_ship_cannot_be_placed_outside(
                    input_list[0])  # ships cannot be placed outside the board it's crazy
                continue

            if input_list[3] == "v" and (ship_dic[input_list[0]] + coord[1] - 1) > 10:
                print_ship_cannot_be_placed_outside(input_list[0])
                continue

            if input_list[3] == "h":
                if "#" in liste[n - 1][coord[1] - 1][(coord[0] - 1): (coord[0] + ship_dic[input_list[0]] - 1)]:
                    print_ship_cannot_be_placed_occupied(input_list[0])  # ships cannot be placed occupied its a rule
                    continue

            if input_list[3] == "v":
                for i in range(coord[1], coord[1] + ship_dic[input_list[0]]):
                    if "#" in liste[n - 1][i - 1][coord[0] - 1]:
                        print_ship_cannot_be_placed_occupied(input_list[0])
                        trying = True
            if trying == True:
                trying = False
                continue

# I used ifs for placing ships I know that I could use dictionaries but same conclusion

# Then every time when I placed a ship, I add that in a list so that I can check whether it's placed or not for already placed ships
# I removed the used ship names form my list to because code prompt possible ships that can be placed to players

# i checked input list and according to shipname and orientation a changed lists' appropriate "-" into "#"

            if input_list[0] == "Carrier":
                if input_list[3] == "h":
                    liste[n - 1][coord[1] - 1][coord[0] - 1:coord[0] + 4] = ["#" for i in range(5)]
                if input_list[3] == "v":
                    for j in range(5):
                        liste[n - 1][coord[1] - 1 + j][coord[0] - 1] = "#"
                ship_list.remove(input_list[0])
                already_placed_control.append(input_list[0])

            if input_list[0] == "Battleship":
                if input_list[3] == "h":
                    liste[n - 1][coord[1] - 1][coord[0] - 1:coord[0] + 3] = ["#" for i in range(4)]

                if input_list[3] == "v":
                    for j in liste[n - 1][coord[1] - 1: coord[1] + 3]:
                        j[coord[0] - 1] = "#"
                ship_list.remove(input_list[0])
                already_placed_control.append(input_list[0])

            if input_list[0] == "Cruiser":
                if input_list[3] == "h":
                    liste[n - 1][coord[1] - 1][coord[0] - 1:coord[0] + 2] = ["#" for i in range(3)]

                if input_list[3] == "v":
                    for j in liste[n - 1][coord[1] - 1: coord[1] + 2]:
                        j[coord[0] - 1] = "#"
                ship_list.remove(input_list[0])
                already_placed_control.append(input_list[0])

            if input_list[0] == "Submarine":
                if input_list[3] == "h":
                    liste[n - 1][coord[1] - 1][coord[0] - 1:coord[0] + 2] = ["#" for i in range(3)]

                if input_list[3] == "v":
                    for j in liste[n - 1][coord[1] - 1: coord[1] + 2]:
                        j[coord[0] - 1] = "#"
                ship_list.remove(input_list[0])
                already_placed_control.append(input_list[0])

            if input_list[0] == "Destroyer":
                if input_list[3] == "h":
                    liste[n - 1][coord[1] - 1][coord[0] - 1:coord[0] + 1] = ["#" for i in range(2)]

                if input_list[3] == "v":
                    for j in liste[n - 1][coord[1] - 1: coord[1] + 1]:
                        j[coord[0] - 1] = "#"
                ship_list.remove(input_list[0])
                already_placed_control.append(input_list[0])

# here i  copied the boards for each player for hitting rounds,
# I used deepcopy because otherwise my boards will be change when code go back to for loop
            if n == 1:
                player_1_board = copy.deepcopy(liste)

            if n == 2:
                player_2_board = copy.deepcopy(liste)

            confirming = ""
            flag2 = 0
# then, if a player placed every ship i asked if he/she is satisfied about his/her placement or not,
# if player is not satisfied i recreate the board, ship lists and boards to go back to placing phase.
# if 1st player is happy about the board it's player 2's turn to place ships.
#so in biggest for loop i made n=2 if player 2 is not satisfied about her/his placement code go back and
# makes placements again for player 2. if 2nd player satisfied, placement phase over and we go on.
            if len(ship_list) == 0:
                print_3d_list(liste)
                while confirming != 'y' and confirming != 'n':
                    print_confirm_placement()
                    confirming = input().lower()
                    if n == 1 and confirming == "y":
                        player_1_board = copy.deepcopy(liste)
                        ship_list = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
                        already_placed_control.clear()
                        liste.clear()
                        liste = [[["-" for i in range(10)] for j in range(10)] for k in range(2)]
                        flag2 = 1
                        break

                    elif n == 2 and confirming == "y":
                        already_placed_control.clear()
                        player_2_board = copy.deepcopy(liste)
                        flag2 = 1
                        break

                    elif n == 1 and confirming == "n":
                        ship_list = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
                        already_placed_control.clear()
                        liste.clear()
                        liste = [[["-" for i in range(10)] for j in range(10)] for k in range(2)]
                        player_1_board.clear()
                        player_1_board = [[["-" for i in range(10)] for j in range(10)] for k in range(2)]

                    elif n == 2 and confirming == "n":
                        ship_list = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
                        already_placed_control.clear()
                        liste.clear()
                        liste = [[["-" for i in range(10)] for j in range(10)] for k in range(2)]
                        player_2_board.clear()
                        player_2_board = [[["-" for i in range(10)] for j in range(10)] for k in range(2)]

                if flag2 == True:
                    flag2 = False
                    break

    game_over = True
    while game_over:
        flag = True
        for n in range(1, 3):
            enough = True
            if flag == False:
                break
            while enough:
                if n == 1:
                    print_3d_list(player_1_board)
                if n == 2:
                    print_3d_list(player_2_board)

# when a player shoot every ship, board will have 17 "!" ,because sum of length of all ships are 17 ,
# so when board list has 17 "!" game will be over.
# with the for loops below here i checked board lists

                if n == 1:
                    sum = 0
                    for i in range(10):
                        for j in range(10):
                            if player_1_board[1][i][j] == "!":
                                sum = sum + 1
                    if sum == 17:
                        print_player_won(1)
                        game_over = False
                        enough = False
                        flag = False
                        break

                if n == 2:
                    sum_2 = 0
                    for i in range(10):
                        for j in range(10):
                            if player_2_board[0][i][j] == "!":
                                sum_2 = sum_2 + 1
                    if sum_2 == 17:
                        print_player_won(2)
                        game_over = False
                        enough = False
                        flag = False
                        break

                print_player_turn_to_strike(n)
                print_choose_target_coordinates()
                target = input().split()

                if len(target) != 2:
                    print_incorrect_input_format()
                    continue

                try:
                    target_list = [int(i) for i in target]
                except:
                    print_incorrect_input_format()
                    continue
                if target_list[1] > 10 or target_list[0] > 10 or target_list[1] < 0 or target_list[0] < 0:
                    print_incorrect_coordinates()
                    continue

# if there is a "!" or "O" that means that "-" has shooted before so we should say it to the shooter

                if n == 1:
                    if player_2_board[1][target_list[1] - 1][target_list[0] - 1] == "!":
                        print_tile_already_struck()
                        continue
                    if player_2_board[1][target_list[1] - 1][target_list[0] - 1] == "O":
                        print_tile_already_struck()
                        continue

# these lines will check the intervals and change them into "!" if there is "#" or "O" if there is "-"

                    if player_2_board[1][target_list[1] - 1][target_list[0] - 1] == "#":
                        print_hit()
                        player_2_board[1][target_list[1] - 1][target_list[0] - 1] = "!"
                        player_1_board[1][target_list[1] - 1][target_list[0] - 1] = "!"
                        continue

                    if player_2_board[1][target_list[1] - 1][target_list[0] - 1] != "#":
                        print_miss()
                        player_2_board[1][target_list[1] - 1][target_list[0] - 1] = "O"
                        player_1_board[1][target_list[1] - 1][target_list[0] - 1] = "O"

# when a player missed the shoot until he/she write "done" we must get an input again and again

                        xyz = True
                        while xyz:
                            print_type_done_to_yield(2)
                            done_control = input().capitalize()
                            if done_control != "Done":
                                continue
                            if done_control == "Done":
                                xyz = False
                                enough = False

# if there is a "!" or "O" that means that "-" has shooted before so we should say it to the shooter

                if n == 2:
                    if player_1_board[0][target_list[1] - 1][target_list[0] - 1] == "!" or \
                            player_1_board[0][target_list[1] - 1][target_list[0] - 1] == "O":
                        print_tile_already_struck()
                        continue

# these lines will check the intervals and change them into "!" if there is "#" or "O" if there is "-"

                    if player_1_board[0][target_list[1] - 1][target_list[0] - 1] == "#":
                        print_hit()
                        player_1_board[0][target_list[1] - 1][target_list[0] - 1] = "!"
                        player_2_board[0][target_list[1] - 1][target_list[0] - 1] = "!"
                        continue

                    if player_1_board[0][target_list[1] - 1][target_list[0] - 1] != "#":
                        print_miss()

                        player_1_board[0][target_list[1] - 1][target_list[0] - 1] = "O"
                        player_2_board[0][target_list[1] - 1][target_list[0] - 1] = "O"

# when a player missed the shoot until he/she write "done" we must get an input again and again

                        abc = True
                        while abc:
                            print_type_done_to_yield(1)
                            is_it_done = input().capitalize()
                            if is_it_done != "Done":
                                continue
                            if is_it_done == "Done":
                                abc = False
                                enough = False

    print_thanks_for_playing()


    # DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
except:
    f.close()

