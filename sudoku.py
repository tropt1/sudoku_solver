import pygame
import sys
import sudokum

pygame.init()


#   test


# arr = sudokum.generate(mask_rate=0.7)
# for i in range(9):
#     for j in range(9):
#         if arr[i][j] == 0:
#             arr[i][j] = " "

WIDTH, HEIGHT = 500, 560
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font1 = pygame.font.SysFont("Arial", 19)
font2 = pygame.font.SysFont("Arial", 48)


def draw_background():
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, pygame.Color("black"), pygame.Rect(25, 25, 450, 450), 5)
    i = 1
    while (i * 50) < 450:
        line_width = 2 if i % 3 > 0 else 5
        pygame.draw.line(screen, pygame.Color("black"), pygame.Vector2((i * 50) + 25, 25),
                         pygame.Vector2((i * 50) + 25, 470), line_width)
        pygame.draw.line(screen, pygame.Color("black"), pygame.Vector2(25, (i * 50) + 25),
                         pygame.Vector2(470, (i * 50) + 25), line_width)
        i += 1


def write(text, y, color="Red"):
    text = font1.render(text, True, pygame.Color(color))
    text_rect = text.get_rect(center=(WIDTH // 2, y))
    screen.blit(text, text_rect)


def generator():
    global arr
    arr = sudokum.generate(mask_rate=0.7)
    for i in range(9):
        for j in range(9):
            if arr[i][j] == 0:
                arr[i][j] = " "


def draw_numbers():
    row = 0
    offset = 35
    while row < 9:
        col = 0
        while col < 9:
            output = arr[row][col]
            n_text = font2.render(str(output), True, pygame.Color('black'))
            screen.blit(n_text, pygame.Vector2((col * 50) + offset - 1, (row * 50) + offset - 11))
            col += 1
        row += 1


def main():
    draw_background()
    write("sudoku", 12)
    draw_numbers()
    pygame.display.flip()


generator()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    main()
