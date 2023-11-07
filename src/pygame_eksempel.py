# Et simpelt pygames-eksempel.

import src.pygame_eksempel as pygame_eksempel
pygame_eksempel.init()
screen = pygame_eksempel.display.set_mode([500, 500])
running = True
while running:
    for event in pygame_eksempel.event.get():
        if event.type == pygame_eksempel.QUIT:
            running = False
    screen.fill((255, 255, 255))
    pygame_eksempel.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    pygame_eksempel.display.flip()
pygame_eksempel.quit()