import random

def numbers_generator():
    random_small = random.randint(1,10)

    big_numbers = [25, 50, 75, 100]

    random_big = random.sample(big_numbers, 1)

    #0 nolla number
    number_choice_nolla = input('Hello, what would you like to choose, "s" - small number, "b" - big number ? \n')

    if number_choice_nolla == "s":
        print(random_small)

    elif number_choice_nolla == "b":
        print(random_big)

    #1 yksi number
    number_choice_yksi = input('and then ? \n')

    if number_choice_yksi == "s":
        print(random_small)

    elif number_choice_yksi == "b":
        print(random_big)

    #2 kaksi number
    number_choice_kaksi = input('and then ? \n')

    if number_choice_kaksi == "s":
        print(random_small)

    elif number_choice_kaksi == "b":
        print(random_big)

    #3 kolme number
    number_choice_kolme = input('and then ? \n')

    if number_choice_kolme == "s":
        print(random_small)

    elif number_choice_kolme == "b":
        print(random_big)

    #4 nelja vow
    number_choice_nelya = input('and then ? \n')

    if number_choice_nelya == "s":
        print(random_small)

    elif number_choice_nelya == "b":
        print(random_big)

    #5 viisi vow
    number_choice_viisi = input('and then ? \n')

    if number_choice_viisi == "s":
        print(random_small)

    elif number_choice_viisi == "b":
        print(random_big)

    target_number = random.randint(101,999)

    print('The target number is', target_number)