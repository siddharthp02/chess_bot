#BOARD AND DISPLAY
white_pieces = {'king':'♔','queen':'♕','bishop':'♗','rook':'♖','knight':'♘','pawn':'♙'}
black_pieces = {'king':'♚','queen':'♛','bishop':'♝','rook':'♜','knight':'♞','pawn':'♟︎'}

class ChessBoard:
    def __init__(self):
        self.board = [] 
        for n in range(8):
            row = []
            for i in range(8):
                row.append(' ')
            self.board.append(row)
b = ChessBoard()

def display_board(board):
    
    
    print('   A   B   C   D   E   F   G   H')
    for i in range(8):
        print(f' ---------------------------------\n{8-i}| {b.board[i][0]} | {b.board[i][1]} | {b.board[i][2]} | {b.board[i][3]} | {b.board[i][4]} | {b.board[i][5]} | {b.board[i][6]} | {b.board[i][7]} |{8-i}')
    print(' ---------------------------------')
    print('   A   B   C   D   E   F   G   H')

#display_board(b.board) - to display board

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
