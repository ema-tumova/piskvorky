# PIŠKVORKY

from random import choice

# příprava hry, úvodní oznámení pro hráče:
player = input("Chceš mít 'x' nebo 'o'?").lower()
while player not in ['x', 'o', 'X', 'O']:
    print("Zadej prosím pouze x nebo o.")
    player = input("Chceš mít 'x' nebo 'o'?").lower()
if player == 'o':
    pc = 'x'
if player == 'x':
    pc = 'o'
print(f"""Hraješ s {player}, počítač má {pc}.
Herní pole je jednorozměrné, má 20 polí umístěných za sebe.""")

def player_move(board):
    # vrací board s hráčovým tahem
    # zamítá čísla mimo 1-20 a tahy na zabraná políčka
    # pokud je zadána nesprávná hodnota, hráč je vždy znovu dotazován
    dotaz = 'Na jakou pozici (1-20) chceš hrát?'
    
    while True:
        odpoved = input(dotaz)
        while not odpoved.isnumeric():
            print('Vyber si ČÍSLO pozice mezi 1 a 20.')
            odpoved = input(dotaz)
        position = int(odpoved) - 1
        if position not in range(20):
            print('Vyber si číslo pozice mezi 1 a 20.')
        elif board[position] != '-':
            print('Pozice je už zabraná, vyber si jinou.')
        else:
            break
    
    board = move(board, player, position)
    return board

def pc_move(board):
    # vrací board s tahem počítače
    while True:
        position = choice(range(20))
        if board[position] == '-':
            print('Hraje počítač:')
            board = move(board, pc, position)
            break
    
    return board

def move(board, player_or_pc, position):
    # vrací board se zaznamenaným tahem na dané pozici
    zacatek = board[:position]
    konec = board[position + 1 :]
    board = zacatek + player_or_pc + konec

    return board
    
def evaluate(board):
    # vyhodnocuje tah a oznamuje výhru, prohru, remízu, nebo pokračuje ve hře
    hra_pokracuje = False

    if 'xxx' in board:
        if player == 'x':
            print('Vyhrál jsi ty, křížek :).')
        if player == 'o':
            print('Vyhrál počítač (křížek), tak třeba příště to vyjde zase tobě ;)')
    elif 'ooo' in board:
        if player == 'o':
            print('Vyhrál jsi ty, kolečko :).')
        if player == 'x':
            print('Vyhrál počítač (kolečko), tak třeba příště to vyjde zase tobě ;)')
    elif '-' not in board:
        print('Nerozhodně, už není volné místo na plánku hry :).')
    else:
        hra_pokracuje = True
    
    return hra_pokracuje

def tictactoe():
    # celá hra piškvorky
    board = '-' * 20
    while True:
        board = player_move(board)
        print(board)
        hra_pokracuje = evaluate(board)
        if not hra_pokracuje:
            break
        board = pc_move(board)
        print(board)
        hra_pokracuje = evaluate(board)
        if not hra_pokracuje:
            break

tictactoe()
