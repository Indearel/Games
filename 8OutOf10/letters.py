import random

def letters_generator():
    #0 nolla vow
    vowels_nolla = ["A", "Ą", "E", "Ę", "I", "O", "Ó", "U", "Y"]

    random_vowel_nolla = random.choice(vowels_nolla)

    #1 yksi vow
    vowels_yksi = ["A", "Ą", "E", "Ę", "I", "O", "Ó", "U", "Y"]

    random_vowel_yksi = random.choice(vowels_yksi)

    #2 kaksi vow
    vowels_kaksi = ["A", "Ą", "E", "Ę", "I", "O", "Ó", "U", "Y"]

    random_vowel_kaksi = random.choice(vowels_kaksi)

    #3 kolme vow
    vowels_kolme = ["A", "Ą", "E", "Ę", "I", "O", "Ó", "U", "Y"]

    random_vowel_kolme = random.choice(vowels_kolme)

    #4 nelja vow
    vowels_nelja = ["A", "Ą", "E", "Ę", "I", "O", "Ó", "U", "Y"]

    random_vowel_nelja = random.choice(vowels_nelja)

    #5 viisi vow
    vowels_viisi = ["A", "Ą", "E", "Ę", "I", "O", "Ó", "U", "Y"]

    random_vowel_viisi = random.choice(vowels_viisi)

    #6 kuusi vow
    vowels_kuusi = ["A", "Ą", "E", "Ę", "I", "O", "Ó", "U", "Y"]

    random_vowel_kuusi = random.choice(vowels_kuusi)

    #7 seitseman vow
    vowels_seitseman = ["A", "Ą", "E", "Ę", "I", "O", "Ó", "U", "Y"]

    random_vowel_seitseman = random.choice(vowels_seitseman)

    #8 kahdeksan vow
    vowels_kahdeksan = ["A", "Ą", "E", "Ę", "I", "O", "Ó", "U", "Y"]

    random_vowel_kahdeksan = random.choice(vowels_kahdeksan)

    #0 nolla con
    consonants_nolla = ["B", "C", "Ć", "D", "F", "G", "H", "J", "K", "L", "Ł", "M", "N", "Ń", "P", "R", "S", "Ś", "T", "W", "Z", "Ź", "Ż"]

    random_consonants_nolla = random.choice(consonants_nolla)

    #1 yksi con
    consonants_yksi = ["B", "C", "Ć", "D", "F", "G", "H", "J", "K", "L", "Ł", "M", "N", "Ń", "P", "R", "S", "Ś", "T", "W", "Z", "Ź", "Ż"]

    random_consonants_yksi = random.choice(consonants_yksi)

    #2 kaksi con
    consonants_kaksi = ["B", "C", "Ć", "D", "F", "G", "H", "J", "K", "L", "Ł", "M", "N", "Ń", "P", "R", "S", "Ś", "T", "W", "Z", "Ź", "Ż"]

    random_consonants_kaksi = random.choice(consonants_kaksi)

    #3 kolme con
    consonants_kolme = ["B", "C", "Ć", "D", "F", "G", "H", "J", "K", "L", "Ł", "M", "N", "Ń", "P", "R", "S", "Ś", "T", "W", "Z", "Ź", "Ż"]

    random_consonants_kolme = random.choice(consonants_kolme)

    #4 nelja con
    consonants_nelja = ["B", "C", "Ć", "D", "F", "G", "H", "J", "K", "L", "Ł", "M", "N", "Ń", "P", "R", "S", "Ś", "T", "W", "Z", "Ź", "Ż"]

    random_consonants_nelja = random.choice(consonants_nelja)

    #5 viisi con
    consonants_viisi = ["B", "C", "Ć", "D", "F", "G", "H", "J", "K", "L", "Ł", "M", "N", "Ń", "P", "R", "S", "Ś", "T", "W", "Z", "Ź", "Ż"]

    random_consonants_viisi = random.choice(consonants_viisi)

    #6 kuusi con
    consonants_kuusi = ["B", "C", "Ć", "D", "F", "G", "H", "J", "K", "L", "Ł", "M", "N", "Ń", "P", "R", "S", "Ś", "T", "W", "Z", "Ź", "Ż"]

    random_consonants_kuusi = random.choice(consonants_kuusi)

    #7 seitseman con
    consonants_seitseman = ["B", "C", "Ć", "D", "F", "G", "H", "J", "K", "L", "Ł", "M", "N", "Ń", "P", "R", "S", "Ś", "T", "W", "Z", "Ź", "Ż"]

    random_consonants_seitseman = random.choice(consonants_seitseman)

    #8 kahdeksan con
    consonants_kahdeksan = ["B", "C", "Ć", "D", "F", "G", "H", "J", "K", "L", "Ł", "M", "N", "Ń", "P", "R", "S", "Ś", "T", "W", "Z", "Ź", "Ż"]

    random_consonants_kahdeksan = random.choice(consonants_kahdeksan)

    #0 nolla
    letter_choice_nolla = input('Hello, what would you like to choose, "v" - vowel, "c" - consonants ? \n')

    if letter_choice_nolla == "v":
        print(random_vowel_nolla)

    elif letter_choice_nolla == "c":
        print(random_consonants_nolla)

    #1 yksi
    letter_choice_yksi = input('and then ? \n')

    if letter_choice_yksi == "v":
        print(random_vowel_yksi)

    elif letter_choice_yksi == "c":
        print(random_consonants_yksi)

    #2 kaksi
    letter_choice_kaksi = input('and then ? \n')

    if letter_choice_kaksi == "v":
        print(random_vowel_kaksi)

    elif letter_choice_kaksi == "c":
        print(random_consonants_kaksi)

    #3 kolme
    letter_choice_kolme = input('and then ? \n')

    if letter_choice_kolme == "v":
        print(random_vowel_kolme)

    elif letter_choice_kolme == "c":
        print(random_consonants_kolme)

    #4 nelja
    letter_choice_nelja = input('and then ? \n')

    if letter_choice_nelja == "v":
        print(random_vowel_nelja)

    elif letter_choice_nelja == "c":
        print(random_consonants_nelja)

    #5 viisi
    letter_choice_viisi = input('and then ? \n')

    if letter_choice_viisi == "v":
        print(random_vowel_viisi)

    elif letter_choice_viisi == "c":
        print(random_consonants_viisi)

    #6 kuusi
    letter_choice_kuusi = input('and then ? \n')

    if letter_choice_kuusi == "v":
        print(random_vowel_kuusi)

    elif letter_choice_kuusi == "c":
        print(random_consonants_kuusi)

    #7 seitseman
    letter_choice_seitseman = input('and then ? \n')

    if letter_choice_seitseman == "v":
        print(random_vowel_seitseman)

    elif letter_choice_seitseman == "c":
        print(random_consonants_seitseman)

    #8 kahdeksan
    letter_choice_kahdeksan = input('and then ? \n')

    if letter_choice_kahdeksan == "v":
        print(random_vowel_kahdeksan)

    elif letter_choice_kahdeksan == "c":
        print(random_consonants_kahdeksan)
