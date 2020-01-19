num = int(input("Enter a number of row:"))


def triangle_maker(num):

    # outer loop to handle number of rows
    for i in range(0, num):

        # inner loop to handle number spaces
        # values changing acc. to requirement
        for j in range(0, num - i - 1):
            print(end=" ")

        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i + 1):
            # printing the stars
            print("*", end=" ")
        # ending line after each row
        print("\r")


triangle_maker(num)
