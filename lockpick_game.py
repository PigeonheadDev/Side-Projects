import random
import sys
import time
import math

try:
    import bext
except ImportError:
    print('This program requires the bext module.')
    sys.exit()

empty = ' '
ext = '*'
wall = '-'
pin = '|'
key = '='
bar = '_'
cursor = '/'

difficulty = "Easy"
tumblers = 4
attempts = 5
lockpicking_bonus = 0

def main_program():
    bext.clear()
    intc = 0
    print("This is a small game about picking a lock.")
    print("This was designed with the idea of possibly being used in a")
    print("game of Dungeons & Dragons. As such, you will be asked to")
    print("enter your 'Sleight of Hand' skill. The higher your bonus,")
    print("the more attempts you will have to pick the lock. In")
    print("addition, you will know the first correct tumblers for every")
    print("4 points you have in this skill.")
    print("")
    print("~~~~~~~~~~~~ HOW TO PLAY: ~~~~~~~~~~~~")
    print("Locks have a certain amount of tumblers, which must be moved")
    print("upwards to allow your key to move through. If you select the")
    print("right tumbler, it will stay upwards. If you select the wrong")
    print("tumbler, it will not stay up as well as cause the tumblers")
    print("you've already moved upwards to fall as well. Choosing a wrong")
    print("tumbler will cause you to lose an attempt. Finally, if you pick")
    print("the leftmost tumbler and it is the correct one, your key will")
    print("move inwards and force the tumbler to stay upwards, even if")
    print("you later select the wrong tumbler.")
    print("")
    print("Created by Lyon [thepigeonmanlyon on Discord]")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("")
    while True:
        game_setup()
    #    game_loop()
    #    game_complete()
    game_setup()
    

def game_setup():
    lockpicking_bonus = 0
    selected_difficulty = 0
    intc1 = 0
    intc2 = 0
    while intc1 == 0:
        try:
            lockpicking_bonus = input("Please enter your Sleight of Hand Bonus >>")
            lockpicking_bonus = int(lockpicking_bonus)
            intc1 += 1
        except ValueError:
            print("That is not a valid input. Try again.")
            print("")
    print("")
    while intc2 == 0:
        try:
            print("Enter the difficulty of the Lock you would like to attempt.")
            print("1. Easy [4 tumblers, 5 attempts]")
            print("2. Normal [5 tumblers, 4 attempts]")
            print("3. Hard [6 tumblers, 3 attempts]")
            print("4. Very Hard [7 tumblers, 2 attempts]")
            print("5. Impossible [8 tumblers, 1 attempts]")
            print("0. Random Difficulty")
            selected_difficulty = input(">> ")
            selected_difficulty = int(selected_difficulty)
            if 0 <= selected_difficulty <= 5:
                pass
            else:
                raise ValueError
            intc2 += 1
        except ValueError:
            print("That is not a valid input. Try again.")
            print("")
    bext.clear()
    # game_start(selected_difficulty)
    lock_param = lock_randomization(selected_difficulty)
    lock_order = determine_order(lock_param["tumblers"])
    key_position = 4
    cursor_position = 4
    game_loop(lock_param, lock_order, key_position, cursor_position, lockpicking_bonus)

def game_loop(lock_param, lock_order, key_position, cursor_position, lockpicking_bonus):
    tumbler_positions = lock_param["positions"]
    initial_lock_order = lock_order.copy()
    player_order = []
    player_order_count = 0
    lockable_tumbler = 1
    reset_flag = 0
    total_attempts = max(lock_param["attempts"] + lockpicking_bonus, 1)
    revealed_numbers = math.floor(lockpicking_bonus / 4)
    #while 0 in tumbler_positions and total_attempts > 0:
    success_state = 0
    while total_attempts > 0:
        bext.clear()
        draw_lock(lock_param["tumblers"], key_position, cursor_position, tumbler_positions)
        print("")
        if success_state == 1:
            time.sleep(0.05)
            key_position += 1
            if key_position >= 17:
                break
            else:
                pass
        else:
            if lock_param["difficulty"] == "Impossible" or lock_param["difficulty"] == "Easy":
                print("This is an " + lock_param["difficulty"] + " lock.")
            else:
                print("This is a " + lock_param["difficulty"] + " lock.")
            print("")
            # print("There are " + str(lock_param["tumblers"]) + " tumblers in this lock.")
            # print("You have " + str(lock_param["attempts"]) + " attempts to pick this lock.")
            # print("You would normally have " + str(lock_param["attempts"]) + " attempts to pick this lock.")
            if reset_flag == 1:
                print("!! - You selected an incorrect tumbler.")
                print("!! - Tumblers have been reset, -1 attempt.")
                # print("DEV LINE :: Recorded tumbler positions are: " + str(tumbler_positions))
            print("You currently have " + str(total_attempts) + " attempts to open this lock.")
            if lockpicking_bonus >= 4:
                print("Due to your high Sleight of Hand skill, you know")
                print("that the first tumbler(s) are: " + str(initial_lock_order[0:revealed_numbers]))
            #print("DEV LINE :: CURRENT PLAYER ORDER IS " + str(player_order))
            #print("DEV LINE :: THE CORRECT ORDER IS " + str(lock_order)) #################### COMMENT THIS OUT WHEN NOT TESTING
            #print("DEV LINE :: TUMBLER POSITIONS ARE: " + str(tumbler_positions))
            print("")
            intc3 = 0
            selection = 1
            reset_flag = 0
            while intc3 == 0:
                try:
                    #print(player_order_count)
                    selection = input("Select tumbler, q to quit >>")
                    if selection == "q":
                        sys.exit()
                    selection = int(selection)
                    if 1 <= selection <= lock_param["tumblers"]:
                       pass
                    else:
                        raise ValueError
                    intc3 += 1
                    print("")
                except ValueError:
                    print("That is not a valid input. Try again.")
                    print("")
        player_order.append(selection)
        if player_order == lock_order:
            success_state = 1
        if success_state == 1:
                player_order_count == None
                tumbler_positions[selection-1] = 1
                player_order_count += 1
                while lockable_tumbler in player_order:
                    tumbler_positions[lockable_tumbler-1] = 2
                    player_order.remove(lockable_tumbler)
                    lock_order.remove(lockable_tumbler)
                    lockable_tumbler += 1
                    key_position += 1
        else:
            if player_order[player_order_count] == lock_order[player_order_count]: # and success_state != 1:
                tumbler_positions[selection-1] = 1
                player_order_count += 1
                while lockable_tumbler in player_order:
                    tumbler_positions[lockable_tumbler-1] = 2
                    player_order.remove(lockable_tumbler)
                    lock_order.remove(lockable_tumbler)
                    lockable_tumbler += 1
                    player_order_count -= 1
                    key_position += 1
            else:
                tumbler_positions = [0 if x == 1 else x for x in tumbler_positions]
                reset_flag = 1
                total_attempts -= 1
                player_order = []
                player_order_count = 0
        cursor_position = selection + 3
    if success_state == 1:
        print("You have successfully picked this lock!")
    else:
        print("XXX   FAILURE   XXX")
        print("You have failed to open this lock.")
    print("")
    print("Would you like to play this game again? y/n")
    ync = 0
    while ync == 0:
        play_again = input(">>")
        play_again = play_again.upper()
        if play_again == "Y" or play_again == "N":
            ync += 1
        else:
            print("That is not a valid input. Try again.")
            print("")
    if play_again == "N":
        sys.exit()
    else:
        bext.clear()

def draw_lock(tumbler_count, key_position, cursor_position, tumbler_positions):
    x = 0
    y = 0
    tumbler_positions = tumbler_positions
    ############### MAYBE ADD 2 SPACES TO X TO EMPHASIZE KEY BEING PUT IN??
    x_width = 26
    y_width = 7
    numbers_printed = 1
    tumblers_printed = 0
    while y < y_width:
        while x < x_width:
            bext.goto(x, y)
            bext.fg('black')
            bext.bg('white')
            tumbler_check = x - 4
            if x > 15:
                pass
                #if y == 3 and key_position == 15:
                #    bext.bg('yellow')
                #    for letter in "UNLOCKED!!":
                #        print(letter)
                #        time.sleep(0.2)
                #else:
                #    pass
            elif (x == 0 or x == 15) and (y < 2 or y > 4):
                bext.bg('blue')
                print(ext)
            elif (y == 0 or y == 6):
                bext.bg('blue')
                print(ext)
            elif (y == 1 or y == 5) and (x == 1 or x == 14):
                bext.bg('blue')
                print(ext)
            elif y == 3:
                #tumbler_check = x - 4
                if x < key_position:
                    bext.fg('black')
                    bext.bg('yellow')
                    print(key)
                elif tumbler_check < tumbler_count:
                    if tumbler_positions[tumbler_check] == 0:
                        bext.bg('red')
                        print(pin)
                    else:
                        print(empty)
                else:
                    print(empty)
            elif y == 1 and 3 < x < 12:
                if numbers_printed < tumbler_count + 1:
                    print(numbers_printed)
                    numbers_printed += 1
                else:
                    print(empty)
            elif y == 2:
                if 3 < x < 12:
                    #tumbler_check = x - 4
                    #print("DEV LINE :: TUMBLER POSITIONS IS " + str(tumbler_positions))
                    #print("DEV LINE :: TUMBLER CHECK IS " + str(tumbler_check))
                    if len(tumbler_positions) <= tumbler_check:
                        print(wall)
                    elif tumbler_positions[tumbler_check] == 0:
                        print(empty)
                    elif 1 <= tumbler_positions[tumbler_check] <= 2:
                        bext.bg('red')
                        print(pin)
                    elif tumbler_positions[tumbler_check] == 3:
                        print(wall)
                else:
                    print(wall)
            elif y == 4:
                if x < cursor_position:
                    print(bar)
                elif x == cursor_position:
                    print(cursor)
                else:
                    print(empty)
            else:
                print(empty)
            x += 1
        x = 0
        bext.fg('white')
        bext.bg('black')
        y += 1

def lock_randomization(selected_difficulty):
    # PERCENTILES OF DIFFICULTIES - 4: 35%/5: 25%/6:20%/7: 15%/8: 5%
    # print("Difficulty percentile is " + str(difficulty_percentile))
    if selected_difficulty != 0:
        if selected_difficulty == 1:
            difficulty_percentile = 7
        elif selected_difficulty == 2:
            difficulty_percentile = 12
        elif selected_difficulty == 3:
            difficulty_percentile = 16
        elif selected_difficulty == 4:
            difficulty_percentile = 19
        elif selected_difficulty == 5:
            difficulty_percentile = 20
        else:
            difficulty_percentile = 7
    else:
        difficulty_percentile = random.randint(1,20)
    if difficulty_percentile <= 7:
        return {
            "difficulty": "Easy",
            "tumblers": 4,
            "attempts": 5,
            "positions": [0, 0, 0, 0]
            }
    elif difficulty_percentile <= 12:
        return {
            "difficulty": "Normal",
            "tumblers": 5,
            "attempts": 4,
            "positions": [0, 0, 0, 0, 0]
            }
    elif difficulty_percentile <= 16:
        return {
            "difficulty": "Hard",
            "tumblers": 6,
            "attempts": 3,
            "positions": [0, 0, 0, 0, 0, 0]
            }
    elif difficulty_percentile <= 19:
        return {
            "difficulty": "Very Hard",
            "tumblers": 7,
            "attempts": 2,
            "positions": [0, 0, 0, 0, 0, 0, 0]
            }
    elif difficulty_percentile <= 20:
        return {
            "difficulty": "Impossible",
            "tumblers": 8,
            "attempts": 1,
            "positions": [0, 0, 0, 0, 0, 0, 0, 0]
            }
    else:
        return {
            "difficulty": "Easy",
            "tumblers": 4,
            "attempts": 5
            }

def determine_order(no_of_tumblers):
    order = []
    dummy_no = 1
    while len(order) < no_of_tumblers:
        order.append(dummy_no)
        dummy_no += 1
    random.shuffle(order)
    return order

main_program()
