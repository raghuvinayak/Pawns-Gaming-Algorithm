def solution(B):
    pos_x, pos_y = 0, 0
    # find "O" character from B
    for i in range(len(B)):
        for j in range(len(B[i])):
            if B[i][j] == "O":
                pos_x = i
                pos_y = j

    # if O is located in end line
    if pos_x == len(B) - 1:
        # if O is located in up-left and up-right, return 2
        if B[pos_x-1][pos_y-1]=="X" and B[pos_x-1][pos_y+1] == "X":
            return 2
        # else if O is located in up-left or O is located in up-right, return 1
        elif B[pos_x-1][pos_y-1] == "X" or B[pos_x-1][pos_y+1] == "X":
            return 1

    # in all other cases, return 0
    return 0



B = ['X....', '.X...', '..O..', '...X.', '.....'] 
print(solution(B)) # 0
B = ['..X...', '......', '....X.', '.X....', '..X.X.', '...O..']
print(solution(B)) # 2
