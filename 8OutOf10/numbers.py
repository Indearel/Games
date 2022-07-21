import random


def numbers_generator():
    # 0 nolla number
    number_choice_nolla = input('What would you like to choose, "s" - small number, "b" - big number ? \n')

    random_small_nolla = random.randrange(1, 10)

    big_numbers_nolla = [25, 50, 75, 100]

    random_big_nolla = random.sample(big_numbers_nolla, 1)

    if number_choice_nolla == "s":
        print(random_small_nolla)

    elif number_choice_nolla == "b":
        print(random_big_nolla)

    # 1 yksi number
    number_choice_yksi = input('and then ? \n')

    random_small_yksi = random.randrange(1, 10)

    big_numbers_yksi = [25, 50, 75, 100]

    random_big_yksi = random.sample(big_numbers_yksi, 1)

    if number_choice_yksi == "s":
        print(random_small_yksi)

    elif number_choice_yksi == "b":
        print(random_big_yksi)

    # 2 kaksi number
    number_choice_kaksi = input('and then ? \n')

    random_small_kaksi = random.randrange(1, 10)

    big_numbers_kaksi = [25, 50, 75, 100]

    random_big_kaksi = random.sample(big_numbers_kaksi, 1)

    if number_choice_kaksi == "s":
        print(random_small_kaksi)

    elif number_choice_kaksi == "b":
        print(random_big_kaksi)

    # 3 kolme number
    number_choice_kolme = input('and then ? \n')

    random_small_kolme = random.randrange(1, 10)

    big_numbers_kolme = [25, 50, 75, 100]

    random_big_kolme = random.sample(big_numbers_kolme, 1)

    if number_choice_kolme == "s":
        print(random_small_kolme)

    elif number_choice_kolme == "b":
        print(random_big_kolme)

    # 4 nelja number
    number_choice_nelya = input('and then ? \n')

    random_small_nelya = random.randrange(1, 10)

    big_numbers_nelya = [25, 50, 75, 100]

    random_big_nelya = random.sample(big_numbers_nelya, 1)

    if number_choice_nelya == "s":
        print(random_small_nelya)

    elif number_choice_nelya == "b":
        print(random_big_nelya)

    # 5 viisi number
    number_choice_viisi = input('and then ? \n')

    random_small_viisi = random.randrange(1, 10)

    big_numbers_viisi = [25, 50, 75, 100]

    random_big_viisi = random.sample(big_numbers_viisi, 1)

    if number_choice_viisi == "s":
        print(random_small_viisi)

    elif number_choice_viisi == "b":
        print(random_big_viisi)

    target_number = random.randint(101, 999)

    print('The target number is', target_number)
