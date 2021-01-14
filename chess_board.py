#BOARD AND DISPLAY
white_pieces = {'king':'♔','queen':'♕','bishop':'♗','rook':'♖','knight':'♘','pawn':'♙'}
black_pieces = {'king':'♚','queen':'♛','bishop':'♝','rook':'♜','knight':'♞','pawn':'♟︎'}
columns = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
class ChessBoard:
    def __init__(self):
        self.board = ['#'] 
        for n in range(8):
            row = ['#']
            for i in range(8):
                row.append(' ')
            self.board.append(row)
b = ChessBoard()
def display_board(board):
    
    
    print('   A   B   C   D   E   F   G   H')
    for i in range(8):
        print(f' ---------------------------------\n{8-i}| {b.board[8-i][1]} | {b.board[8-i][2]} | {b.board[8-i][3]} | {b.board[8-i][4]} | {b.board[8-i][5]} | {b.board[8-i][6]} | {b.board[8-i][7]} | {b.board[8-i][8]} |{8-i}')
    print(' ---------------------------------')
    print('   A   B   C   D   E   F   G   H')

display_board(b.board) #- to display board

class Pieces:
    def __init__(self):
        self.white_pieces = []
        self.white_pawns = [white_pieces['pawn'] for n in range(8)]
        self.white_rooks = [white_pieces['rook'] for n in range(2)]
        self.white_bishops = [white_pieces['bishop'] for n in range(2)]
        self.white_knights = [white_pieces['knight'] for n in range(2)]
        self.white_queens = [white_pieces['queen']]
        self.white_kings = [white_pieces['king']]
        self.white_pieces.append(self.white_rooks)
        self.white_pieces.append(self.white_bishops)
        self.white_pieces.append(self.white_queens)
        self.white_pieces.append(self.white_knights)
        self.white_pieces.append(self.white_pawns)
        self.white_pieces.append(self.white_kings)
        
        self.black_pieces = []
        self.black_pawns = [black_pieces['pawn'] for n in range(8)]
        self.black_rooks = [black_pieces['rook'] for n in range(2)]
        self.black_bishops = [black_pieces['bishop'] for n in range(2)]
        self.black_knights = [black_pieces['knight'] for n in range(2)]
        self.black_queens = [black_pieces['queen']]
        self.black_kings = [black_pieces['king']]
        self.black_pieces.append(self.black_pawns)
        self.black_pieces.append(self.black_rooks)
        self.black_pieces.append(self.black_queens)
        self.black_pieces.append(self.black_kings)
        self.black_pieces.append(self.black_knights)
        self.black_pieces.append(self.black_bishops)
pieces = Pieces()
#can call pieces by pieces.black_pieces etc.

def place_piece(board,piece,row,column):
    board[row][columns[column]]=piece
    
'''
place_piece(b.board,white_pieces,'pawn',2,'d')
display_board(b.board)
'''
def reset_board(board):
    for n in range(len(pieces.white_pawns)):
        place_piece(b.board,pieces.white_pawns[n],2,list(columns.keys())[n])
    for n in range(len(pieces.black_pawns)):
        place_piece(b.board,pieces.black_pawns[n],7,list(columns.keys())[n])

    place_piece(b.board,pieces.white_rooks[0],1,list(columns.keys())[0])
    place_piece(b.board,pieces.white_rooks[1],1,list(columns.keys())[7])
    place_piece(b.board,pieces.black_rooks[0],8,list(columns.keys())[0])
    place_piece(b.board,pieces.black_rooks[1],8,list(columns.keys())[7])

    place_piece(b.board,pieces.white_knights[0],1,list(columns.keys())[1])
    place_piece(b.board,pieces.white_knights[1],1,list(columns.keys())[6])
    place_piece(b.board,pieces.black_knights[0],8,list(columns.keys())[1])
    place_piece(b.board,pieces.black_knights[1],8,list(columns.keys())[6])

    place_piece(b.board,pieces.white_bishops[0],1,list(columns.keys())[2])
    place_piece(b.board,pieces.white_bishops[1],1,list(columns.keys())[5])
    place_piece(b.board,pieces.black_bishops[0],8,list(columns.keys())[2])
    place_piece(b.board,pieces.black_bishops[1],8,list(columns.keys())[5])

    place_piece(b.board,pieces.white_kings[0],1,list(columns.keys())[4])
    place_piece(b.board,pieces.white_queens[0],1,list(columns.keys())[3])
    place_piece(b.board,pieces.black_kings[0],8,list(columns.keys())[4])
    place_piece(b.board,pieces.black_queens[0],8,list(columns.keys())[3])
        

reset_board(b.board)
display_board(b.board)


