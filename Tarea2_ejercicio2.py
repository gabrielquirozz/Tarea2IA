#codigo extraido de https://www.geeksforgeeks.org/sudoku-backtracking-7/
solutions = []

def createMatrix(n):
  return [[0 for col in range(n)] for row in range(n)]

def readData():
  with open('info.txt') as file:
    info = file.readlines()
    infoArray = []
    for line in info:
        infoArray.append(line[:-1])

    matrix = createMatrix(int(infoArray[0]))
    
    for i in range(2, int(infoArray[1]) + 2):
        coordsAndValue = [int(x) for x in infoArray[i].split()]
        matrix[coordsAndValue[0] - 1][coordsAndValue[1] - 1] = coordsAndValue[2]
    
    return (int(infoArray[0]), matrix)

def write(arr, N):
    f = open('out.txt', 'w')
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end = " ")
            f.write(str(arr[i][j])+" ")
        f.write("\n")
        print()
    f.close()

def find_empty_location(arr, l, N):
    for row in range(N):
        for col in range(N):
            if(arr[row][col]== 0):
                l[0]= row
                l[1]= col
                return True
    return False
 
def used_in_row(arr, row, num, N):
    for i in range(N):
        if(arr[row][i] == num):
            return True
    return False
  
def used_in_col(arr, col, num, N):
    for i in range(N):
        if(arr[i][col] == num):
            return True
    return False
 
def used_in_box(arr, row, col, num, mn):
    for i in range(mn):
        for j in range(mn):
            if(arr[i + row][j + col] == num):
                return True
    return False
 
def check_location_is_safe(arr, row, col, num, mn):
    return not used_in_row(arr, row, num, N) and not used_in_col(arr, col, num, N) and not used_in_box(arr, row - row % mn, col - col % mn, num, mn)
 
def solveSudoku(arr, N):
    mn = 3 if N==9 else 2 
    l =[0, 0]
    if(not find_empty_location(arr, l, N)):
        return True
    row = l[0]
    col = l[1]
    for num in range(1, N+1):
        if(check_location_is_safe(arr,
                          row, col, num, mn)):
            arr[row][col]= num
            if(solveSudoku(arr, N)):
                return True
            arr[row][col] = 0  
    return False

N, grid = readData()
print("")
if (solveSudoku(grid, N)):
  write(grid, N)
else:
    print("no solution  exists ")