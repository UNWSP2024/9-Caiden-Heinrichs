#Week 9, Program 3 - Average Numbers
#Caiden Heinrichs
#03/27/26


def sum_numbers_from_file():
    #Set up variable for adding numbers
    total = 0

    try:
        with open("numbers.txt", "r") as numbers:
            #Add each number to the total
            for number in numbers.readlines():
                number = int(number)
                total += number

            print(f"Total of numbers in numbers.txt: {total}")
    
    #Print error message if an error is found
    except ValueError:
        print("Non-integer value found in numbers.txt")
    except IOError:
        print("File \"numbers.txt\" not found")


if __name__ == '__main__':
    sum_numbers_from_file()
