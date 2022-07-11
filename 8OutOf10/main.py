import letters
import numbers

def main():
   choice = input('What do we have today, "l" - letter, "n" - numbers\n')
   if choice == "l":
      letters.letters_generator()
   elif choice == "n":
      numbers.numbers_generator()

main()
