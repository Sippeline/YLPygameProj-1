import pygame
import sys
from button import Button

pygame.init()
SCREEN = pygame.display.set_mode((1400, 700))
pygame.display.set_caption("Menu")
BG = pygame.image.load("assets/Background.jpeg")
BG = pygame.transform.scale(BG, (1400, 700))


def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)


def play():
    while True:
        game_mouse_pos = pygame.mouse.get_pos()
        SCREEN.fill("black")
        play_text = get_font(45).render("Game is gonna be here soon.", True, "White")
        play_rect = play_text.get_rect(center=(700, 350))
        SCREEN.blit(play_text, play_rect)
        play_back = Button(image=None, pos=(700, 550),
                           text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        play_back.changeColor(game_mouse_pos)
        play_back.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_back.checkForInput(game_mouse_pos):
                    main_menu()

        pygame.display.update()


def options():
    while True:
        options_mouse_pos = pygame.mouse.get_pos()
        SCREEN.fill("white")

        options_text = get_font(45).render("Options are gonna be here soon.", True, "Black")
        options_rect = options_text.get_rect(center=(700, 350))
        SCREEN.blit(options_text, options_rect)

        options_back = Button(image=None, pos=(700, 550),
                              text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        options_back.changeColor(options_mouse_pos)
        options_back.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if options_back.checkForInput(options_mouse_pos):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        menu_mouse_pos = pygame.mouse.get_pos()

        menu_text = get_font(100).render("MAIN MENU", True, "#b68f40")
        menu_rect = menu_text.get_rect(center=(700, 100))

        play_button = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(700, 250),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        options_button = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(700, 400),
                                text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        quit_button = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(700, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(menu_text, menu_rect)

        for button in [play_button, options_button, quit_button]:
            button.changeColor(menu_mouse_pos)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(menu_mouse_pos):
                    play()
                if options_button.checkForInput(menu_mouse_pos):
                    options()
                if quit_button.checkForInput(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()
