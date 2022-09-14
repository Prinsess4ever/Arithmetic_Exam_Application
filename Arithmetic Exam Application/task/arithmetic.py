# write your code here

while True:
    answer = input("With the first message, the program should ask for a difficulty level:\n1 - simple operations with numbers 2-9\n2 - integral squares 11-29\n")
    if answer != "1" and answer != "2":
        print("Incorrect format.")
    else:
        break

import random


def een():
    def equation():
        choice1 = random.choice([2, 3, 4, 5, 6, 7, 8, 9])
        choice2 = random.choice(["+", "-", "*"])
        choice3 = random.choice([2, 3, 4, 5, 6, 7, 8, 9])

        return [choice1, choice2, choice3]

    def is_int(int_of_str):
        try:
            int(int_of_str)
            return True
        except:
            return False



    def opplosen(oefening):
        if oefening[1] == "+":
            return oefening[0] + oefening[-1]
        if oefening[1] == "-":
            return oefening[0] - oefening[-1]
        if oefening[1] == "*":
            return oefening[0] * oefening[-1]

    oefening = equation()

    print(oefening[0], oefening[1], oefening[2])

    while True:
        oplossing_of_niet = input()
        if not is_int(oplossing_of_niet) or oplossing_of_niet == "":
            print("Wrong format.")
        else:
            break

    if oplossing_of_niet == str(opplosen(oefening)):
        return "Right!"
    else:
        return "Wrong!"


def twee():
    def equation():
        choice1 = random.choice([11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29])

        return choice1

    def is_int(int_of_str):
        try:
            int(int_of_str)
            return True
        except:
            return False



    def opplosen(oefening):
        return oefening * oefening


    oefening = equation()

    print(oefening)

    while True:
        oplossing_of_niet = input()
        if not is_int(oplossing_of_niet) or oplossing_of_niet == "":
            print("Wrong format! Try again.")
        else:
            break

    if oplossing_of_niet == str(opplosen(oefening)):
        return "Right!"
    else:
        return "Wrong!"



def loop1():
    mark = 0

    for i in range(0, 5):
        two = een()
        print(two)
        if two == "Right!":
            mark += 1
    return mark


def loop2():
    mark = 0

    for i in range(0, 5):
        two = twee()
        print(two)
        if two == "Right!":
            mark += 1

    return mark

if answer == "1":
    loop_een = loop1()
    print(f"Your mark is {loop_een}/5.")
else:
    loop_twee = loop2()
    print(f"Your mark is {loop_twee}/5.")

yes_no = input("Would you like to save your result to the file? Enter yes or no.\n")

if yes_no.lower() in ("yes", "y"):
    name = input("What is your name?\n")
    if answer == "1":
        with open("results.txt", "a") as f:
            f.write(f"{name}: {loop_een}/5 in level {answer} (simple operations with numbers 2-9).")
    else:
        with open("results.txt", "a") as f:
            f.write(f"{name}: {loop_twee}/5 in level {answer} (integral squares 11-29).")

    print('The results are saved in "results.txt".')
