# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 12:16:45 2021

@author: DELL
"""

import pygame

pygame.font.init()
pygame.mixer.init()
GAME_END = pygame.USEREVENT


WINNER_SOUND = pygame.mixer.Sound("E:/PROJECTS/PYTHON PROJECTS/GAMES/TURTLE RACE/winner.mp3")
TURTLE = pygame.image.load("E:/PROJECTS/PYTHON PROJECTS/GAMES/TURTLE RACE/turtle.png")

WIDTH, HEIGHT = 620, 750
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TURTLE RACE GAME")
FINISH_LINE = pygame.Rect(0, 50, WIDTH, 5)


START_TITLE_FONT = pygame.font.Font("freesansbold.ttf", 80)
START_FONT = pygame.font.Font("freesansbold.ttf", 55)
WINNER_FONT = pygame.font.Font("freesansbold.ttf", 40)


WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
LIME = (200,230,0)
YELLOW = (255,255,0)
PURPLE = (128,0,128)
PINK = (255, 192, 203)
BLUE = (0,0,128)
BROWN = (150, 75, 0)
GOLD = (255, 215, 0)
CREAM = (255, 253, 208)
NEON = (245, 71, 195)
GREEN = (105,255,0)


TURTLE_1 = pygame.Rect(20, 720, 20, 20)
TURTLE_2 = pygame.Rect(105, 720, 20, 20)
TURTLE_3 = pygame.Rect(190, 720, 20, 20)
TURTLE_4 = pygame.Rect(270, 720, 20, 20)
TURTLE_5 = pygame.Rect(350, 720, 20, 20)
TURTLE_6 = pygame.Rect(430, 720, 20, 20)
TURTLE_7 = pygame.Rect(510, 720, 20, 20)
TURTLE_8 = pygame.Rect(580, 720, 20, 20)

def new_game():
    TURTLE_1.y = 720
    TURTLE_2.y = 720
    TURTLE_3.y = 720
    TURTLE_4.y = 720
    TURTLE_5.y = 720
    TURTLE_6.y = 720
    TURTLE_7.y = 720
    TURTLE_8.y = 720
    pygame.display.update()
    
def board():
    WINDOW.fill(BLACK)
    pygame.draw.rect(WINDOW, RED, FINISH_LINE)
    pygame.draw.rect(WINDOW, NEON, TURTLE_1)
    pygame.draw.rect(WINDOW, GOLD, TURTLE_2)
    pygame.draw.rect(WINDOW, CREAM, TURTLE_3)
    pygame.draw.rect(WINDOW, PURPLE, TURTLE_4)
    pygame.draw.rect(WINDOW, PINK, TURTLE_5)
    pygame.draw.rect(WINDOW, BLUE, TURTLE_6)
    pygame.draw.rect(WINDOW, BROWN, TURTLE_7)
    pygame.draw.rect(WINDOW, LIME, TURTLE_8)
    pygame.display.update()
    
def waiting_board():
    WINDOW.fill(WHITE)
    start_text = START_TITLE_FONT.render("TURTLE RACE", 1, GREEN)
    WINDOW.blit(start_text, (WIDTH/2 - start_text.get_width()/2, 100))
    
    WINDOW.blit(TURTLE, (WIDTH/2 - start_text.get_width()/2 , 70))
    
    start_text_1 = START_FONT.render("PRESS SPACEBAR", 1, BLACK)
    WINDOW.blit(start_text_1, (WIDTH/2 - start_text.get_width()/2 + 30, 500))
    
    start_text_2 = START_FONT.render("TO START", 1, BLACK)
    WINDOW.blit(start_text_2, (WIDTH/2 - start_text.get_width()/2 + 120, 557))
    pygame.display.update()

def winner():
    if TURTLE_1.y < 52:
        pygame.event.post(pygame.event.Event(GAME_END))
    if TURTLE_2.y < 52:
        pygame.event.post(pygame.event.Event(GAME_END))
    if TURTLE_3.y < 52:
        pygame.event.post(pygame.event.Event(GAME_END))
    if TURTLE_4.y < 52:
        pygame.event.post(pygame.event.Event(GAME_END))
    if TURTLE_5.y < 52:
        pygame.event.post(pygame.event.Event(GAME_END))
    if TURTLE_6.y < 52:
        pygame.event.post(pygame.event.Event(GAME_END))
    if TURTLE_7.y < 52:
        pygame.event.post(pygame.event.Event(GAME_END))
    if TURTLE_8.y < 52:
        pygame.event.post(pygame.event.Event(GAME_END))


def winner_turtle_name(text, text_1):
    winner_text = WINNER_FONT.render(text, 1, GOLD)
    winner_text_1 = WINNER_FONT.render(text_1, 1, GOLD)
    WINDOW.blit(winner_text, (WIDTH/2 - winner_text.get_width()/2, HEIGHT/2 - winner_text.get_height()/2))
    WINDOW.blit(winner_text_1, (WIDTH/2 - winner_text_1.get_width()/2, HEIGHT/2 + winner_text.get_width()/4 - winner_text_1.get_height()/2))
    
    pygame.display.update()
    WINNER_SOUND.play()
    pygame.time.delay(5000)
    new_game()


waiting = True
while waiting:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                waiting = False
    waiting_board()



def main():
    
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_1:
                    TURTLE_1.y -= 8
                if event.key == pygame.K_2:
                    TURTLE_2.y -= 8
                if event.key == pygame.K_3:
                    TURTLE_3.y -= 8
                if event.key == pygame.K_4:
                    TURTLE_4.y -= 8
                if event.key == pygame.K_5:
                    TURTLE_5.y -= 8
                if event.key == pygame.K_6:
                    TURTLE_6.y -= 8
                if event.key == pygame.K_7:
                    TURTLE_7.y -= 8
                if event.key == pygame.K_8:
                    TURTLE_8.y -= 8
                    
            if event.type == GAME_END:
                main()


        
        TURTLES = [TURTLE_1, TURTLE_2, TURTLE_3, TURTLE_4, TURTLE_5, TURTLE_6, TURTLE_7, TURTLE_8]
        for a in TURTLES:       
            if a.y < 52 and a.x > 10 and a.x < 80:   
                winner_text = "TURTLE 1"
                winner_text_1 = "WON!"
                winner_turtle_name(winner_text,winner_text_1)
            if a.y < 52 and a.x > 80 and a.x < 170:   
                winner_text = "TURTLE 2"
                winner_text_1 = "WON!"
                winner_turtle_name(winner_text,winner_text_1)
            if a.y < 52 and a.x > 170 and a.x < 250:   
                winner_text = "TURTLE 3"
                winner_text_1 = "WON!"
                winner_turtle_name(winner_text,winner_text_1)
            if a.y < 52 and a.x > 250 and a.x < 330:   
                winner_text = "TURTLE 4"
                winner_text_1 = "WON!"
                winner_turtle_name(winner_text,winner_text_1) 
            if a.y < 52 and a.x > 330 and a.x < 410:   
                winner_text = "TURTLE 5"
                winner_text_1 = "WON!"
                winner_turtle_name(winner_text,winner_text_1)
            if a.y < 52 and a.x > 410 and a.x < 490:   
                winner_text = "TURTLE 6"
                winner_text_1 = "WON!"
                winner_turtle_name(winner_text,winner_text_1)
            if a.y < 52 and a.x > 490 and a.x < 560:   
                winner_text = "TURTLE 7"
                winner_text_1 = "WON!"
                winner_turtle_name(winner_text,winner_text_1)
            if a.y < 52 and a.x > 560 and a.x < 620:   
                winner_text = "TURTLE 8"
                winner_text_1 = "WON!"
                winner_turtle_name(winner_text,winner_text_1)
                   

        board()
    main()
    
if __name__ == "__main__":
    main()
    
