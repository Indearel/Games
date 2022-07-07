import letters
import numbers

def main():
   choice = input('What do we have today, "l" - letter, "n" - numbers\n')
   if choice == "l":
      letters.letters_generarator()
   elif choice == "n":
      numbers.numbers_generator()

main()
