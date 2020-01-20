n = int(input("Enter the number of row: "))


def stars_in_hollow_right():
    for row in range(n):
        for col in range(n):
            if (row == 0) or (col == (n - 1)) or (row == col):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print("\r")


stars_in_hollow_right()
