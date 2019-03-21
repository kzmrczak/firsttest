
theboard = {'1': ' ','2': ' ','3': ' ',
            '4': ' ','5': ' ','6': ' ',
            '7': ' ','8': ' ','9': ' ',}


def makeBoard(board):
    print(board['1'] + "|" + board['2'] + "|" + board['3'])
    print('-+-+-')
    print(board['4'] + "|" + board['5'] + "|" + board['6'])
    print('-+-+-')
    print(board['7'] + "|" + board['8'] + "|" + board['9'])


def rules():
   if theboard['1'] == 'X' and theboard['2'] == 'X' and theboard['3'] == 'X' or \
      theboard['1'] == 'O' and theboard['2'] == 'O' and theboard['3'] == 'O':
       return True
   elif theboard['2'] == 'X' and theboard['5'] == 'X' and theboard['8'] == 'X' or \
        theboard['2'] == 'O' and theboard['5'] == 'O' and theboard['8'] == 'O':
       return True
   elif theboard['3'] == 'X' and theboard['6'] == 'X' and theboard['9'] == 'X' or \
        theboard['3'] == 'O' and theboard['6'] == 'O' and theboard['9'] == 'O':
       return True
   elif theboard['1'] == 'X' and theboard['4'] == 'X' and theboard['7'] == 'X' or \
        theboard['1'] == 'O' and theboard['4'] == 'O' and theboard['7'] == 'O':
       return True
   elif theboard['4'] == 'X' and theboard['5'] == 'X' and theboard['6'] == 'X' or \
        theboard['4'] == 'O' and theboard['5'] == 'O' and theboard['6'] == 'O':
       return True
   elif theboard['1'] == 'X' and theboard['5'] == 'X' and theboard['9'] == 'X' or \
        theboard['1'] == 'O' and theboard['5'] == 'O' and theboard['9'] == 'O':
       return True
   elif theboard['3'] == 'X' and theboard['5'] == 'X' and theboard['7'] == 'X' or \
        theboard['3'] == 'O' and theboard['5'] == 'O' and theboard['7'] == 'O':
       return True
   else:
       return False

won = False
turn = 'X'
player = 1
for i in range(0,9):
    makeBoard(theboard)

    print("Gracz nr {} Ktore pole wybierasz?".format(player))
    while True:
        move = input()

        if theboard[move] == ' ':
            theboard[move] = turn
            break
        else:
            print("Pole zajęte!, wybierz jeszcze raz.")
            continue
    if rules() == True:
        makeBoard(theboard)
        print('')
        print("Wygrywa gracz {}, gratulacje!".format(player))
        break
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    if player == 1:
        player = 2
    else:
        player = 1





#makeBoard(theboard)
