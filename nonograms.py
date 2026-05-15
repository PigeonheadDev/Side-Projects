import random
import sys

x_size = 3
y_size = 3
full_percentile = 60

empty = "-"
full = "X"
blank = "O"

user_nonogram = []

generated_nonogram = []

def generate_block():
    returned_block = blank
    if random.randint(1,100) >= full_percentile:
        returned_block = full
    return returned_block

def create_computer_nonogram():
    y = 0
    x = 0
    x_line = []
    compiled_lines = []
    while y < y_size:
        while x < x_size:
            block = generate_block()
            x_line.append(block)
            x += 1
        x = 0
        y += 1
        compiled_lines.append(x_line)
        x_line = []
    return compiled_lines

def print_nonogram(provided_nonogram):
    y = 0
    while y < y_size:
        hold = "|".join(provided_nonogram[y])
        print(hold)
        y += 1

def create_blank_user_nonogram():
    y = 0
    x = 0
    x_line = []
    compiled_lines = []
    while y < y_size:
        while x < x_size:
            x_line.append(empty)
            x += 1
        x = 0
        y += 1
        compiled_lines.append(x_line)
        x_line = []
    return compiled_lines

def get_row_or_column_info(provided_nonogram, rc, position):
    y = 0
    x = 0
    h = 0
    compiled_hints = []
    if rc == "r":
        y = position
        while x < x_size:
            if provided_nonogram[y][x] == full:
                h += 1
            elif provided_nonogram[y][x] == blank and h > 0:
                compiled_hints.append(str(h))
                h = 0
            else:
                pass
            x += 1
    if rc == "c":
        x = position
        while y < y_size:
            if provided_nonogram[y][x] == full:
                h += 1
            elif provided_nonogram[y][x] == blank and h > 0:
                compiled_hints.append(str(h))
                h = 0
            else:
                pass
            y += 1
    if h > 0:
        compiled_hints.append(str(h))
        h = 0
    returned_hint = "-".join(compiled_hints)
    return returned_hint

def print_hints(provided_nonogram):
    j = 0
    while j < y_size:
        print("Row " + str(j+1) + ": " + get_row_or_column_info(provided_nonogram,"r",j))
        j += 1
    j = 0
    while j < x_size:
        print("Column " + str(j+1) + ": " + get_row_or_column_info(provided_nonogram,"c",j))
        j += 1

def gameplay(generated_nonogram):
    gen_nng = generated_nonogram
    user_nng = create_blank_user_nonogram()
    while check_nonograms(gen_nng, user_nng) == False:
        #print_nonogram(gen_nng)
        print_hints(gen_nng)
        print_nonogram(user_nng)
        print("")
        print("Syntax: x y X/O || enter q to quit or r to reset")
        response = input("Please enter your command >>")
        if response == "q":
            double_check = input("Are you SURE you want to quit? y/n >>")
            if double_check == "y":
                sys.exit()
            else:
                pass
        elif response == "r":
            double_check = input("Are you SURE you want to reset your progress? y/n >>")
            if double_check == "y":
                user_nng = create_blank_user_nonogram()
            else:
                pass
        else:
            try:
                received_input = response.split(" ")
                # print(received_input)
                x = int(received_input[0]) - 1
                y = int(received_input[1]) - 1
                mark = received_input[2]
                mark = mark.upper()
                if mark == "X":
                    user_nng[y][x] = full
                elif mark == "O":
                    user_nng[y][x] = blank
                else:
                    print("Invalid command. Try again.")
            except:
                print("Invalid command. Try again.")
        print("")
    print("!!!!!!!!!!!!! Successful combination achieved! !!!!!!!!!!!!!")
    print("")
    print("Creating new nonogram...")
    print("")

def check_nonograms(generated_nonogram, user_nonogram):
    # needs to specifically check for "full" status instead of total 1:1 match
    if generated_nonogram == user_nonogram:
        return True
    else:
        return False

def initialize():
    #print("Generating nonogram...")
    print("")
    q = 0
    while True:
        generated_nonogram = create_computer_nonogram()
        #user_nonogram = create_blank_user_nonogram()
        gameplay(generated_nonogram)

initialize()

# syntax :: x y x/o // r to reset or q to quit
# Enter your command :