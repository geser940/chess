import pygame #1
from pygame import transform
pygame.init() #2
pygame.display.set_caption('Chess ot GES')
screen = pygame.display.set_mode((800,800)) #3
cell_size = 100
light = (240,217,181)
dark = (181,136,99)
player = 0
selected_piece = None
selected_pos = None
def move(board,r,c):
    p = board[r][c]
    if p == '.':
        return []
    color = int(p[-1])
    moves = []
    if p[0] == 'p':
        if color == 0:
            d = -1
        else:
            d = 1
        if color == 0:
            s = 6
        else:
            s = 1
        if 0 <= r + d < 8 and board[r + d][c] == '.':
            moves.append((r + d, c))
            if r == s and board[r + 2*d][c] == '.':
                moves.append((r + d * 2, c))
        for dc in [-1,1]:
            nr, nc = r + d, c + dc
            if 0 <= nr < 8 and 0 <= nc < 8:
                t = board[nr][nc]
                if t != '.' and int(t[-1]) != color:
                            moves.append((nr,nc))
    elif p[0] == 'k':
        knight_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1),
                        (1, 2), (1, -2), (-1, 2), (-1, -2)]
        for dr, dc in knight_moves:
            row, col = r + dr, c + dc
            if 0 <= row < 8 and 0 <= col < 8:
                if board[row][col] == '.' or int(board[row][col][-1]) != color:
                    moves.append((row, col))
    elif p[0] == 'b':
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dr, dc in directions:
            row, col = r + dr, c + dc
            while 0 <= row < 8 and 0 <= col < 8:
                if board[row][col] == '.':
                    moves.append((row, col))
                else:
                    if int(board[row][col][-1]) != color:
                        moves.append((row, col))
                    break
                row += dr
                col += dc

        # Ладья
    elif p[0] == 'r':
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dr, dc in directions:
            row, col = r + dr, c + dc
            while 0 <= row < 8 and 0 <= col < 8:
                if board[row][col] == '.':
                    moves.append((row, col))
                else:
                    if int(board[row][col][-1]) != color:
                        moves.append((row, col))
                    break
                row += dr
                col += dc

        # Ферзь
    elif p[0] == 'q':
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                      (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dr, dc in directions:
            row, col = r + dr, c + dc
            while 0 <= row < 8 and 0 <= col < 8:
                if board[row][col] == '.':
                    moves.append((row, col))
                else:
                    if int(board[row][col][-1]) != color:
                        moves.append((row, col))
                    break
                row += dr
                col += dc
    elif p[0] == 'king':
        king_moves = [(1, 0), (-1, 0), (0, 1), (0, -1),
                      (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dr, dc in king_moves:
            row, col = r + dr, c + dc
            if 0 <= r < 8 and 0 <= c < 8:
                if board[r][c] == '.' or int(board[r][c][-1]) != color:
                    moves.append((r, c))
    return moves
board = [
    ['r1', 'k1', 'b1', 'q1', 'king1', 'b1', 'k1',
     'r1'],
    ['p1', 'p1', 'p1', 'p1', 'p1', 'p1', 'p1',
     'p1'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['p0', 'p0', 'p0', 'p0', 'p0', 'p0', 'p0',
     'p0'],
    ['r0', 'k0', 'b0', 'q0', 'king0', 'b0', 'k0',
     'r0']]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            c = x // cell_size
            r = y // cell_size
            if 0 <= r < 8 and 0 <= c < 8:
                clicked_piece = board[r][c]
                if clicked_piece != '.' and int(clicked_piece[-1]) == player:
                    selected_piece = clicked_piece
                    selected_pos = (r, c)
                    valid_moves = move(board, r, c)
                elif selected_piece and (r, c) in valid_moves:
                    board[r][c] = selected_piece
                    board[selected_pos[0]][selected_pos[1]] = '.'
                    player = 1 - player
                    selected_piece = None
                    selected_pos = None
                    valid_moves = []

    for r in range(8):
        for c in range(8):
            if (r + c) % 2 == 0:
                color = light
            else:
                color = dark
                pygame.draw.rect(screen, color, (c * cell_size, r * cell_size, cell_size, cell_size))
    y = 0
    for brd in board:
        x = 0
        for b in brd:
            if b != '.':
                screen.blit(transform.scale(pygame.image.load(board[y][x] + '.png'), (90,90)), (5 + x * 100, 5 + y * 100))
            x += 1
        y += 1

    pygame.display.update()
