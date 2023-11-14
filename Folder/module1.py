#setup

from math import *
pieces_name=["R"]
pieces_style=["♜"]

board = [["R","N","B","Q","K","B","N","R"],
         ["P","P","P","P","P","P","P","P"],
         [".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".","."],
         ["p","p","p","p","p","p","p","p"],
         ["r","n","b","q","k","b","n","r"]
        ]


style_board=board
for i in range(8):
    for j in range(8):
        if style_board[i][j] in pieces_name:
            style_board[i][j]=piece_style[pieces_name.indec(board[i][j])

def show_board():
    for i in range(8):
        joined_line = " ".join(board[i])
        print(joined_line)

def show_style_board():
    style_board=board
    for i in range(8):
        for j in range(8):
            if style_board[i][j] in pieces_name:
                style_board[i][j]=piece_style[pieces_name.indec(board[i][j])
