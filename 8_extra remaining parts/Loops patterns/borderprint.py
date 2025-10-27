def print_star_grid_border_only(gridsize):

    for row in range(1, gridsize+1, 1):
        print_grid = []
        
        for column in range(1, gridsize+1, 1):
            isstar = row == 1 or column == 1 or row == gridsize or column == gridsize
            
            print_grid.append("* "if isstar else "  ")

        
        print("".join(print_grid))

print_star_grid_border_only(4)