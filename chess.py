import pygame #1
pygame.init() #2
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
    pygame.display.update()
