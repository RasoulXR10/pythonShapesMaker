# num = int(input("Enter the number of row: "))
num = 6


def heart_maker(num):
    for row in range(num):
        for col in range(num + 1):
            if (row == 0 and col % 3 != 0) or (row == 1 and col % 3 == 0) or (row - col == 2) or (row + col == 8):
                print("*", end="")
            else:
                print(" ", end="")
        print()


heart_maker(num)
