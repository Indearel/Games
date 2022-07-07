import random

def numbers_generator():
    random_small = random.randint(1,10)

    big_numbers = [25, 50, 75, 100]

    random_big = random.sample(big_numbers, 1)

    number_choice = input('Hello, what would you like to choose, "s" - small number, "b" - big number ? \n')

    if number_choice == "s":
        print(random.randint(1,10))

    elif number_choice == "b":
        print(random_big)

    for x in range(5):

        number_choice_later = input('and then ? \n')

        if number_choice_later == "s":
            print(random.randint(1,10))

        elif number_choice == "b":
            print(random_big)

    target_number = random.randint(101,999)

    print('The target number is', target_number)