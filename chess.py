import pygame #1
from pygame import transform
pygame.init() #2
pygame.display.set_caption('Chess ot GES')
screen = pygame.display.set_mode((800,800)) #3
cell_size = 100
light = (240,217,181)
dark = (181,136,99)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    for r in range(8):
        for c in range(8):
            if (r + c) % 2 == 0:
                color = light
            else:
                color = dark
                pygame.draw.rect(screen, color, (c * cell_size, r * cell_size, cell_size, cell_size))
    board = [
        ['r1-Photoroom', 'k1-Photoroom', 'b1-Photoroom', 'q1-Photoroom', 'king1-Photoroom', 'b1-Photoroom', 'k1-Photoroom', 'r1-Photoroom'],
        ['p1-Photoroom', 'p1-Photoroom', 'p1-Photoroom', 'p1-Photoroom', 'p1-Photoroom', 'p1-Photoroom', 'p1-Photoroom', 'p1-Photoroom'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['p0-Photoroom', 'p0-Photoroom', 'p0-Photoroom', 'p0-Photoroom', 'p0-Photoroom', 'p0-Photoroom', 'p0-Photoroom', 'p0-Photoroom'],
        ['r0-Photoroom', 'k0-Photoroom', 'b0-Photoroom', 'q0-Photoroom', 'king0-Photoroom', 'b0-Photoroom', 'k0-Photoroom', 'r0-Photoroom']]
    y = 0
    for brd in board:
        x = 0
        for b in brd:
            if b != '.':
                screen.blit(transform.scale(pygame.image.load(board[y][x] + '.png'), (90,90)), (5 + x * 100, 5 + y * 100))
            x += 1
        y += 1
    pygame.display.update()
