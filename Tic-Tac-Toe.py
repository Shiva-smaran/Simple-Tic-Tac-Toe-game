import random
print("Simple tic tac toe game between Player and Computer")
print("Player->X\n2.Computer->O")
n = input("Enter your name")
l = [0,0,0,0,0,0,0,0,0]
def board():
    k = 1
    for i in range(3):
        for j in range(3):
            if(l[k-1]==0):
                print(k,"Yes","     ",end="")
                k+=1
            else:
                print(k," ",l[k-1],"     ",end="")
                k+=1
        print()
def check_win(mark, board):
    return ((board[0] == mark and board[1] == mark and board[2] == mark) or
            (board[3] == mark and board[4] == mark and board[5] == mark) or
            (board[6] == mark and board[7] == mark and board[8] == mark) or
            (board[0] == mark and board[3] == mark and board[6] == mark) or
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            (board[0] == mark and board[4] == mark and board[8] == mark) or
            (board[2] == mark and board[4] == mark and board[6] == mark))
def game():
    count = 0    
    while(count<9):
        print("Choose from the following")
        board()
        i = int(input("Enter your choice from available options"))
        if (l[i-1] != 0):
            print("This choice is not available. Please choose another one.")
            continue
        l[i-1]="X"
        print("Choice locked")
        count+=1
        if check_win("X", l):
            print("Congratulations, ",n," wins!")
            break
        print("Computer's turn.")
        m = random.choice([i for i in range(9) if l[i] == 0])
        print("Computer chose",m)
        l[m-1] = "O"
        count+=1
        if check_win("O", l):
            print("Sorry, the computer wins.")
            break
    repeat = input('do you want another game? y for yes and n for no?::')
    if(repeat == "y" or repeat == "Y"):
        game()
game()
