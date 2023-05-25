M = 9


def solve(grid, row: int, col, num: int) -> bool:
    for x in range(9):
        if grid[row][x] == num:
            return False

    for x in range(9):
        if grid[x][col] == num:
            return False

    startRow = row - row % 3
    startCol = col - col % 3

    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True


def Sudoku(grid, row: int, col) -> bool:
    if row == M - 1 and col == M:
        return True
    if col == M:
        row += 1
        col = 0
    if grid[row][col] != ' ':
        return Sudoku(grid, row, col + 1)
    for num in range(1, M + 1):

        if solve(grid, row, col, num):

            grid[row][col] = num
            if Sudoku(grid, row, col + 1):
                return True
        grid[row][col] = ' '
    return False


def Check(arr) -> bool:
    for i in range(9):
        if ' ' in arr[i]:
            return False
        elif sum(arr[i]) != sum(set((arr[i]))):
            return False

    temp_arr = list(map(list, arr))    # transpose matrix of sudoku

    for i in range(9):
        if sum(temp_arr[i]) != sum(set(temp_arr[i])):
            return False

    return True
