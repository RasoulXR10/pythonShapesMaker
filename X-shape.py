num = input("Enter an odd length numbers: ")


def x_shape(num):
    length = len(num)
    for i in range(length):
        for j in range(length):
            if i == j or i + j == length - 1:
                # this is a same-row mode
                # for same-col mode
                print(num[i], end=" ")
                # print(num[j], end=" ")
            else:
                print(" ", end=" ")
        print("\r")


x_shape(num)
