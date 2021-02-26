

# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():
    usershape = input('Shape?: ')
    while usershape.lower().strip() not in ('pyramid','triangle','square','rectangle','parallelogram','oval'):
        usershape = input('Shape?: ')
    return usershape.lower().strip()


# TODO: Step 1 - get height (it must be int!)
def get_height():
    height = input('Height?: ')
    if height.isdigit() and 0 < int(height) <= 80:
        return int(height)
    else:
        return get_height()
        
# TODO: Step 2
def draw_pyramid(height, outline):
        if outline == True:
            row = 0
            while row < height:
                
                column = 0  
                while column < height*2 - 1:
                    if column + row == height - 1:
                        print("*", end="")
                    elif column - row == height - 1:
                        print("*", end="")
                    elif row == height - 1:
                        print("*",end="")
                    elif column - row < height -1:
                        print(" ",end="")
                    column = column + 1
                row = row + 1
                print("")    
                        
        else:
            row = 0
            while row < height:
                row = row + 1
                spaces = height - row
                spacecount = 0
                while spacecount < spaces:
                    print(" ", end="")
                    spacecount = spacecount + 1
                
                stars = 2 * row - 1
                while stars > 0:
                    print("*", end="")
                    stars = stars - 1
                print("")        

# TODO: Step 3
def draw_square(height, outline):
    if outline == True:
        for row in range(height):
            for col in range(height):
                if row == 0 or row == height-1 or col == 0 or col == height-1:
                    print("*", end="")
                else:
                    print(" ",end="")
            print("")
    else:
        for row in range(height):
            for col in range(height):
                print("*", end="")
            print("")

# TODO: Step 4
def draw_triangle(height, outline):
    if outline == True:
        for row in range(height):
            for col in range(height):
                if col == 0 or row == (height-1) or row == col:
                    print("*",end="")

                elif col<row:
                    print(" ",end="")
            print("")
    else:
        for row in range(0, height):
            print("*"*(row+1))
        #for y in range(0, row+1): 
         # print("*",end="") 
        #print("")


# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
        if shape == "square":
            draw_square(height, outline)
        elif shape == "triangle":
            draw_triangle(height, outline)
        elif shape == "pyramid":
            draw_pyramid(height, outline)
        elif shape == "rectangle":
            draw_rectangle(height, outline)
        elif shape == "parallelogram":
            draw_parallelogram(height, outline)
        elif shape == "oval":
            draw_oval(height, outline)


# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():
    outline = input("Outline only? (y/N): ")
    if outline.strip().lower() == "y":
        return True
    elif outline.strip().lower == "n" or outline.strip() == "":
        return False

def draw_rectangle(height, outline):
    if outline == True:
        for row in range(height):
            for col in range(height+2):
                if row == 0 or row == height-1 or col == 0 or col == height+1:
                    print("*", end="")
                else:
                    print(" ",end="")
            print("")
    else:
        for row in range(height):
            for col in range(height+2):
                print("*", end="")
            print("")

def draw_parallelogram(height, outline): #come back
        if outline == True:
                for row in range(1, height+1):
                    for col in range(1, height-row +1): #no of spaces before
                            print(" ", end="")
                    if row == 1 or row == height:
                        for col in range(1, height +1):
                            print("*",end="")
                    else:
                        for col in range (1, height+1):
                            if col == 1 or col == height:
                                print("*",end="")
                            else:
                                print(" ",end="")
                    print("")

        else:
            row = 0
            while row < height:
                row = row + 1
                spaces = height - row
                spacecount = 0
                while spacecount < spaces:
                    print(" ", end="")
                    spacecount = spacecount + 1
                
                stars = height
                while stars > 0:
                    print("*", end="")
                    stars = stars - 1
                print("")

def draw_oval(height, outline):
    if outline == True:
        for row in range(height):
            for col in range(height):
                if (col == 0 or col == height - 1) and (row != 0 and row != height - 1) or (row == 0 or row == height - 1) and (col > 0 and col < height -1):
                    print("*",end="")
                else:
                    print(" ",end="")
            print("")
    else:
        for row in range(height):
            for col in range(height):
                if (col == 0 or col == height - 1) and (row != 0 and row != height - 1) or (col > 0 and col < height -1):
                    print("*",end="")
                else:
                    print(" ",end="")
            print("")

if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)

