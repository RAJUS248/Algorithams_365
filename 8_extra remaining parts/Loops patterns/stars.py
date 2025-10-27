def print_stars(maxcount):

    for _ in range(maxcount):
        print("*", end=" ")


def print_star_grid(gridsize):
    for count in range(gridsize):
        print(gridsize * "* ")
       


def print_star_list(arr):
    for num in arr:
        print(num * "*")






# arr = [1,2,3,4,5,6,7]

# print_star_list(arr)

# print_star_grid(5)

# print_stars(100)

def print_star_grid_concat(gridsize):

    for row in range(gridsize):

        printMsg = []

        for column in range(gridsize):
            printMsg.append("*")

        print("".join(printMsg))

print_star_grid_concat(5)
