import pygame
import random


pygame.init()

win = pygame.display.set_mode((512, 512))

pygame.display.set_caption("Stay Safe") 

sprite_list = []

yesmask = pygame.image.load("person-yes-mask.png")
nomask = pygame.image.load("person-no-mask.png")
nowashyesmask = pygame.image.load("no-wash-person-yes-mask.png")
nowashnomask = pygame.image.load("no-wash-person-no-mask.png")

sprites = [yesmask, nomask, nowashyesmask, nowashnomask]


def render_board():
    """ renders the sprites in a board. """

    print("rendering")

    win.fill((0,0,0))

    for item in sprite_list:
        win.blit(sprites[item['sprite']], (item['xpos'], item['ypos']))   
    pygame.display.update()    
    


#creating a sprite list and rendering it as a board using the render_board() function.
for y in range(0, 576, 64):
    for x in range(576, 0, -64):
        j = random.randint(0,3)

        sprite_list.append({"sprite": j, "xpos": x, "ypos": y})  

        render_board()  

#Takes player input.
run = True
click=False
while run:
    pygame.time.delay(100)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        if event.type == pygame.MOUSEBUTTONDOWN:
            a, b = event.pos
            for i,val in enumerate(sprite_list):
            
                if sprites[val["sprite"]].get_rect(topleft=(val['xpos'], val['ypos'])).collidepoint(a,b) == True:
                    click = True

                    while click:

                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                    click = False
                                    
                                if val["sprite"] == 1 and event.key == pygame.K_m:
                                    val["sprite"] = 0
                                    render_board()
                                    click = False
                                    

                                if val["sprite"] == 2 and event.key == pygame.K_w:
                                    val["sprite"] = 0
                                    render_board()
                                    click = False
                                
                                if val["sprite"] == 3 and event.key == pygame.K_m:
                                    val["sprite"] = 2
                                    render_board()
                                    click = False
                                
                                if val["sprite"] == 3 and event.key == pygame.K_w:
                                    val["sprite"] = 1
                                    render_board()
                                    click = False

           

pygame.quit()