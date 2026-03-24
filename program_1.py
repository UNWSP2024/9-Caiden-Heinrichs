#Week 9, Program 1 - Item Counter
#Caiden Heinrichs
#03/27/26


def count_file_lines():
    with open("names.txt", "r") as names:
        numberOfNames = len(names.readlines())

    print(f"There are {numberOfNames} names.")

if __name__ == '__main__':
    count_file_lines()
