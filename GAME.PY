import pygame
import time 
import random
pygame.font.init()
WIDTH,HEIGHT=1920,875

PLAYER_WIDTH,PLAYER_HEIGHT= 20,40
PLAYER_VEL=5

STAR_HEIGHT=20
STAR_WIDTH = 10
STAR_VEL=5
  
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("War")

BG = pygame.transform.scale (pygame.image.load("542443.jpg"),(WIDTH,HEIGHT))

FONT= pygame.font.SysFont("Aerial",50)

def draw(player,elapsed_time,stars):
    WIN.blit(BG,(0,0))
    
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text,(10,10))
    pygame.draw.rect(WIN,"green",player)

    for star in stars:
         pygame.draw.rect(WIN,"white",star)

    pygame.display.update()

def main(): 
    run= True

    player = pygame.Rect(350,HEIGHT-PLAYER_HEIGHT,PLAYER_WIDTH,PLAYER_HEIGHT)

    clock=pygame.time.Clock()
    start_time=time.time()
    elapsed_time=0

    star_add_increment=2000
    star_count = 0
    stars=[]
    hit = False


    while(run==True):

        star_count += clock.tick(60)
        elapsed_time=time.time()-start_time

        if star_count> star_add_increment:
             for _ in range (7):
                  star_x = random.randint(0,WIDTH-STAR_WIDTH)
                  star = pygame.Rect(star_x,-STAR_HEIGHT,STAR_WIDTH,STAR_HEIGHT)
                  stars.append(star)
            
             star_add_increment= max(200,star_add_increment-50)
             star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    

        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >=0:
                player.x -= PLAYER_VEL
    
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width<= WIDTH:
            player.x +=PLAYER_VEL

        for star in stars[:]:
             star.y+= STAR_VEL
             if star.y > HEIGHT:
                  stars.remove(star)
             elif star.y + star.height >= player.y and star.colliderect(player):
                  stars.remove(star)
                  hit = True
                  break
             
        if hit:
            lost_text= FONT.render("GAME OVER <3",1,"WHITE")
            WIN.blit(lost_text,(WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(2000)
            break

        draw(player,elapsed_time,stars)

    pygame.quit()
if __name__ =="__main__":
    main()
