def print_star_pyramid(hieght):
    noOfStars = 1
    for level in range(1,hieght+1):
        noOfSpace = hieght - level
        print(noOfSpace * " ",noOfStars * "*")
        noOfStars += 2

def invert_pyramid(hieght):
    for level in range(1,hieght+1):
        noOfSpace = level - 1
        noOfStars = (hieght - level) * 2 + 1
        print(noOfSpace * " ",noOfStars * "*")

invert_pyramid(5)
print_star_pyramid(5)
