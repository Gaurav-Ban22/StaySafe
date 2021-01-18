import pygame
import random


pygame.init()

win = pygame.display.set_mode((512, 512))


pygame.display.set_caption("Stay Safe") 


width = 32
height = 32
vel = 5 
sprite_list = []

yesmask = pygame.image.load("person-yes-mask.png")
nomask = pygame.image.load("person-no-mask.png")
nowashyesmask = pygame.image.load("no-wash-person-yes-mask.png")
nowashnomask = pygame.image.load("no-wash-person-no-mask.png")



sprites = [yesmask, nomask, nowashyesmask, nowashnomask]

def render_board():

    print("rendering")

    win.fill((0,0,0))

    for item in sprite_list:
        win.blit(sprites[item['sprite']], (item['xpos'], item['ypos']))   
    pygame.display.update()    
    



for y in range(0, 544, 32):
    for x in range(544, 0, -32):
        j = random.randint(0,3)

        masktype = sprites[j]
        masko = ""


        # if j == 0:
        #     masktype = yesmask
        #     masko = "yesmask"
        #     # win.blit(yesmask, (x,y))
        # if j == 1:
        #     masktype = nomask
        #     masko = "nomask"
        #     # win.blit(nomask, (x,y))
        # if j == 2:
        #     masktype = nowashyesmask
        #     masko = "nowashyesmask"
        #     # win.blit(nowashyesmask, (x,y))
        # if j == 3:
        #     masktype = nowashnomask
        #     masko = "nowashnomask"
        #     # win.blit(nowashnomask, (x,y))

        sprite_list.append({"sprite": j, "xpos": x, "ypos": y})  


        render_board()  

        #win.blit(masktype, (x,y))
        




print(sprite_list)

# class clickdetect:

#     def __init__(self, hi):
#         self.hi = hi



#     def createlist(self):
#         for y in range(0, 544, 32):
#             for x in range(544, 0, -32):
#                 j = random.randint(0,3)




#                 global masktype 

#                 if j == 0:
#                     masktype = yesmask
#                     # win.blit(yesmask, (x,y))
#                 if j == 1:
#                     masktype = nomask
#                     # win.blit(nomask, (x,y))
#                 if j == 2:
#                     masktype = nowashyesmask
#                     # win.blit(nowashyesmask, (x,y))
#                 if j == 3:
#                     masktype = nowashnomask
#                     # win.blit(nowashnomask, (x,y))

#                 win.blit(masktype, (x,y))


#     def detectclick(self):
#         for event in pygame.event.get():
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 a, b = event.pos
#                 if masktype.get_rect(topleft=(x, y)).collidepoint(a, b) == True:
#                     print("yee haw")


# cl = clickdetect("hi")
# cl.createlist()



        


        
    





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
            
                # os = sprite_list[i]['sprite'].replace('"',"")
                # os_real = os.replace("'","")
                if sprites[val["sprite"]].get_rect(topleft=(val['xpos'], val['ypos'])).collidepoint(a,b) == True:
                    print(val["sprite"])
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

                    print('**************************')
                    print(sprite_list)

                    
                        




    

    win.fill((0,0,0))





pygame.quit()