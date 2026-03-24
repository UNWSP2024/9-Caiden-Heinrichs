#Week 9, Program 2 - Random Number File Writer
#Caiden Heinrichs
#03/27/26

import random


def main():
    while True:
        try:
            #Collect count of numbers to be stored
            count = int(input("How many random numbers would you like to store? "))

            #Check for an invalid value or end loop
            if count > 1000 or count < 0:
                raise ValueError
            else:
                break

        except:
            print("Please enter a valid number between 1 and 1000 (0 to exit).")

    #Check if user ended loop
    if count != 0:
            with open("random_numbers.txt", "w") as numbers:
                #Write random numbers to random_numbers.txt
                for i in range(count - 1):
                    randomNumber = random.randint(1, 500)
                    numbers.write(f"{randomNumber}\n")

                #Iterate a final time without a new line
                randomNumber = random.randint(1, 500)
                numbers.write(f"{randomNumber}")

                #Notify user of random numbers added
                print(f"{count} random numbers from 1 to 500 have been added to random_numbers.txt")

    else:
        print("Program ended by user.")


if __name__ == "__main__":
    main()
