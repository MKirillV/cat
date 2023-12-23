import pygame


pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

font = pygame.font.SysFont("Kristen ITC", 50)
font2 = pygame.font.SysFont("Kristen ITC", 50)

x,y = 140, 40
x1,y1 = 140, 80
x2,y2 = 140, 120
apple = pygame.image.load("img/яблоко.jpg")
apple = pygame.transform.scale(apple, (100,100))
Shailushai = pygame.image.load("img/шайлушай!.jpg")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.blit(Shailushai, (10, 50)) #это для картинок
    text = font.render("banana cat ", True, (0, 0, 100)
    screen.blit(text, (x, y))
    text2 = font2.render("VS", True, (0, 100, 100))
    screen.blit(text2, (x1, y1))
    textadsf = font.render("apple cat", True, (0, 110, 100))
    screen.blit(textadsf, (x2, y2))
    screen.blit(apple, (10,50))


    pygame.display.update()