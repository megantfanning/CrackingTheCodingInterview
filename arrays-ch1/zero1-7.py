# 1-7 write a algo where in a mxn grid if there is a 0 set both the row and the column to become 0

def zeroedgrid(Arr):
    toZeroOut = []
    #iterate over columns
    rowCounter=0
    for row in Arr:
        rowCounter=+1
        #iterate down column
        zero=False
        for cell in range(len(row)):
            if row[cell] == 0:
                #save the cell position so we can come back to zero out row
                toZeroOut.append(cell)
                zero=True
        #handlecolumns
        if zero:
            toZeroOut.append(rowCounter)
          
    for r in range(len(Arr)):
        # zero out column
        for c in range(len(Arr)):
            if c in toZeroOut:
                Arr[r][c]=0
            if r in toZeroOut:
                Arr[r][c]=0

    return Arr

print(zeroedgrid([[1,2,3],[1,0,3],[1,1,1]]))
