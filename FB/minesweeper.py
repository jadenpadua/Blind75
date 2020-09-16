import random
def minesweeper(n,mines):
    arr = [[0 for row in range(n)] for column in range(n)]

    count = 0
    
    while count < mines:
        x = random.randint(0,n-1)
        y = random.randint(0,n-1)

        if arr[y][x] == 'X':
            continue
        else:
            arr[y][x] = 'X'
            count += 1

    for i in range(len(arr)):
       for j in range(len(arr[i])):

            if arr[i][j] == 'X':
               continue
            
            if i > 0 and j > 0 and arr[i-1][j-1] == 'X':
                arr[i][j] += 1

            if i > 0 and arr[i-1][j] == 'X':
                arr[i][j] += 1
            
            if i > 0 and j < n-1 and arr[i-1][j+1] == 'X':
                arr[i][j] += 1

            if j < n-1 and arr[i][j+1] == 'X':
                arr[i][j] += 1

            if i < n-1 and j< n-1 and arr[i+1][j+1]== 'X':
                arr[i][j] += 1

            if i < n-1  and arr[i+1][j]== 'X':
                arr[i][j] += 1

            if i < n-1 and arr[i+1][j-1] == 'X':
                arr[i][j] += 1

            if i > 0 and arr[i][j-1] == 'X':
                arr[i][j] += 1
            

            

    for row in arr:
        print(" ".join(str(cell) for cell in row))
        print("")

if __name__ == "__main__":
    minesweeper(5,3)
