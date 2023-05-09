import pygame
import sys
import sudokum
import solver

pygame.init()

arr = [[" " for _ in range(9)] for _ in range(9)]


class Button:
    def __init__(self, screen, position, width, height, text,
                 active_color=(170, 180, 185),
                 inactive_color=(130, 140, 150)):
        self.screen = screen
        self.text = text
        self.x ,self.y = position
        self.position = position
        self.width = width
        self.height = height
        self.active_clr = active_color
        self.inactive_clr = inactive_color
        self.font = pygame.font.SysFont("Arial", 42)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        mouse = pygame.mouse.get_pos()

        if (self.x < mouse[0] < self.x + self.width) and (self.y < mouse[1] < self.y + self.height):
            pygame.draw.rect(screen, self.active_clr, (self.x, self.y, self.width, self.height))

            # if pygame.event.get(pygame.MOUSEBUTTONUP):
            #     if action is not None:
            #         action()

        else:
            pygame.draw.rect(screen, self.inactive_clr, (self.x, self.y, self.width, self.height))


        text_render = self.font.render(self.text, True, (255, 255, 255))
        return screen.blit(text_render, (self.x + 5, self.y - 5))

    def change_color(self, active_color, inactive_color):
        self.active_clr = active_color
        self.inactive_clr = inactive_color


WIDTH, HEIGHT = 500, 560
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("sudoku")
font1 = pygame.font.SysFont("Arial", 19)
font2 = pygame.font.SysFont("Arial", 48)
font3 = pygame.font.SysFont("Arial", 42)


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

    # offset = 35
    # for row in range(9):
    #     for col in range(9):
    #         output = arr[row][col]
    #         n_text = font2.render(str(output), True, pygame.Color('black'))
    #         screen.blit(n_text, pygame.Vector2((col * 50) + offset + 4, (row * 50) + offset - 11))


def generator():
    global arr
    arr = sudokum.generate(mask_rate=0.7)
    for i in range(9):
        for j in range(9):
            if arr[i][j] == 0:
                arr[i][j] = " "


def generate_button_action():
    generator()
    offset = 35
    for row in range(9):
        for col in range(9):
            output = arr[row][col]
            n_text = font2.render(str(output), True, pygame.Color('black'))
            screen.blit(n_text, pygame.Vector2((col * 50) + offset + 4, (row * 50) + offset - 11))
    pygame.display.flip()

def exit_button_action():
    pygame.quit()
    sys.exit()


def solve_button_action():
    solver.Sudoku(arr, 0, 0)
    pygame.display.flip()


def check_button_action():
    if not(solver.Check(arr)):
        check_button.change_color((200, 25, 25), (140, 30, 30))
    else:
        check_button.change_color((25, 200, 25), (30, 140, 30))


# Button(width, height, active_color, inactive_color)
# Creating buttons for exit, generate sudoku, solve sudoku
exit_button = Button(screen, (410, 495), 65, 45, 'exit',(200, 25, 25), (140, 30, 30))
generate_button = Button(screen, (25, 495), 145, 45, 'generate')
solve_button = Button(screen, (190, 495), 90, 45, 'solve')
check_button = Button(screen, (300, 495), 100, 45, 'check')


def main():
    draw_background()
    exit_button.draw()
    generate_button.draw()
    solve_button.draw()
    check_button.draw()
    pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if exit_button.rect.collidepoint(pygame.mouse.get_pos()):
                exit_button_action()
            elif generate_button.rect.collidepoint(pygame.mouse.get_pos()):
                generate_button_action()
            elif solve_button.rect.collidepoint(pygame.mouse.get_pos()):
                solve_button_action()
        pygame.display.update()
    main()
