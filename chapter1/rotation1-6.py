# 1-6
# given a image represented by at nxn matrix
# were each pixel in the images is 4bytes
# write a method to rotate the image by 90 degrees (in place)

#Notes: if you can swap the columns with rows because of how nesting working but that swaps the y,x (column, row) to x,y (row, column) coordinates
# x,y to rotate => x1 =n-1-y and y1=x

def rotateGrid(pic):
    n = len(pic)
    grid = [[None]*n]*n

    for x in range(n):
        for y in range(n):
            # x,y to rotate => x1 =n-1-y and y1=x
            print(str(x) +","+str(y))
            print(pic[n-1-y][x])
            grid[x][y] = pic[n-1-y][x]

    return grid

print(rotateGrid([[1,2,3,4],[5,6,7,8],[9,10,11,12], [13,14,15,16]]))
