#!/usr/bin/python3
import sys

def solvequeens(N):
    board = []
    solutions = []
    startpoint = 0
    while (startpoint < N):
        donerows = []
        donecols = []
        diagonal = []
        queens = []
        for row in range(N):
            if row == 0:
                col = startpoint
            else:
                col = 0
            while col < N:
                board.append([row, col])
                if row not in donerows and col not in donecols and [row, col] not in diagonal:
                    queens.append([row, col])
                    donecols.append(col)
                    donerows.append(row)
                    for dr in range(N):
                        if row + dr == N or col + dr == N:
                            break
                        else:
                            diagonal.append([row + dr, col + dr])
                    for dr in range(N):
                        if row + dr == N or col - dr == -1:
                            break
                        else:
                            diagonal.append([row + dr, col - dr])
                    break
                col += 1
        # print("queens:",queens)
        if len(queens) == N:
            solutions.append(queens)
        startpoint += 1

    # print("bord:",board)
    # print("diagonals:",diagonal)
    # print("queens:",queens)
    for quns in solutions:
        print(quns)

if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv)

    if argc != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not isinstance(eval(argv[-1]), int):
        print("N must be a number")
        sys.exit(1)
    if eval(argv[-1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    N = eval(argv[-1])

    # solving a row
    solvequeens(N)
