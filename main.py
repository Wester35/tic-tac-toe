#Coded by Wester35
ls = ['1', '2', '3',
      '4', '5', '6',
      '7', '8', '9']

xo = ['x', 'o']

check_ls = [[0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]]

def printArr():
    print(" ___________")
    print("|", ls[0], "|", ls[1], "|", ls[2], "|")
    print("|===|===|===|")
    print("|", ls[3], "|", ls[4], "|", ls[5], "|")
    print("|===|===|===|")
    print("|", ls[6], "|", ls[7], "|", ls[8], "|")
    print("|___|___|___|")

def checkWinCombX(i):
    tmp = 0
    for j in range(3):
        if ls[check_ls[i][j]] == 'x':
            tmp = tmp + 1
    if tmp == 3:
        return True
    else:
        return False

def checkWinCombO(i):
    tmp = 0
    for j in range(3):
        if ls[check_ls[i][j]] == 'o':
            tmp = tmp + 1
    if tmp == 3:
        return True
    else:
        return False

def checkWinComb(i):
    if checkWinCombX(i):
        return 0
    elif checkWinCombO(i):
        return 1
    else:
        return -1

def printWinner(i):
    print(" __________")
    if i == 0:
        print("| x winner |")
    elif i == 1:
        print("| o winner |")
    else:
        print("|   draw   |")
    print("|__________|")
    input("Press any key to continue.")

def playGame():
    printArr()
    for i in range(9):
        if i % 2 == 0:
            symbol = 'x'
        else:
            symbol = 'o'

        print(f"Ход {symbol}")
        while True:
            tmp = int(input(f"Выберите куда ставить {symbol}: "))
            if ls[tmp - 1] not in xo:
                ls[tmp - 1] = symbol
                break
            else:
                print("Эта клетка уже занята. Попробуйте снова.")

        printArr()
        for k in range(8):
            if checkWinComb(k) == 0:
                printWinner(0)
                exit()
            elif checkWinComb(k) == 1:
                printWinner(1)
                exit()
            elif i == 8:
                printWinner(-1)
                exit()


if __name__ == "__main__":
    playGame()
