import pygame
import time
import random
from playsound import playsound

pygame.init()

display_width = 800
display_height = 600

gamedisplays = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('car game')
clock=pygame.time.Clock()
carimg= pygame.image.load('car1.jpg')
backgroundpic=pygame.image.load('download12.jpg')
yellow_strip=pygame.image.load('yellow strip.jpg')
strip=pygame.image.load('strip.jpg')
car_width=56
intro_background=pygame.image.load('background.jpg')
instruction_background=pygame.image.load('background2.jpg')
pause=False
pygame.mixer.music.load('carsound.mp3')


def obstacle(obs_startx,obs_starty,obs):
    if obs==0:
        obs_pic=pygame.image.load('car.jpg')
    elif obs==1:
        obs_pic=pygame.image.load('car2.jpg')    
    elif obs==2:
        obs_pic=pygame.image.load('car1.jpg')
    elif obs==3:
        obs_pic=pygame.image.load('car4.jpg')
    elif obs==4:
        obs_pic=pygame.image.load('car5.jpg')
    elif obs==5:
        obs_pic=pygame.image.load('car6.jpg')
    elif obs==6:
        obs_pic=pygame.image.load('car7.jpg')
    gamedisplays.blit(obs_pic,(obs_startx,obs_starty))

def button(msg,x,y,width, height, inactivecolor,activecolor,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+width>mouse[0]>x and y+height>mouse[1]>y:
        pygame.draw.rect(gamedisplays,activecolor,(x,y,width,height))
        if click[0]==1 and action!=None:
            if action=="play":
                game_loop()
            elif action=="quit":
                pygame.quit()
                quit()
                sys.exit()
            elif action=="intro":
                introduction()
            elif action=="menu":
                intro_loop()
            elif action=="pause":
                paused()
            elif action=="unpause":
                unpaused()


    else:
        pygame.draw.rect(gamedisplays,inactivecolor,(x,y,width,height))
    smalltext=pygame.font.Font("freesansbold.ttf",20)
    textsurf,textrect=text_objects(msg,smalltext)
    textrect.center=((x+(width/2)),(y+(height/2)))
    gamedisplays.blit(textsurf,textrect)


def getHighestScore():
    with open('highest score.txt','r') as f:
        return f.read()

   
def intro_loop():
    pygame.mixer.music.stop()
    intro = True
    while intro:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()
            gamedisplays.blit(intro_background,(0,0))
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects('CAR GAME',largetext)
            TextRect.center=(400,100)
            gamedisplays.blit(TextSurf,TextRect)
            button('START',150,520,100,50,(0,205,0),(0,255,0),'play')
            button('QUIT',550,520,100,50,(205,0,0),(255,0,0),'quit')
            button('INSTRUCTION',300,520,200,50,(0,0,205),(0,0,255),'intro')
            pygame.display.update()
            clock.tick(50)

def paused():
    pygame.mixer.music.stop()
    global pause

    while pause:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
            gamedisplays.blit(instruction_background,(0,0))
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf, TextRect=text_objects('PAUSED',largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            button('CONTINUE',150,520,120,50,(0,205,0),(0,255,0),'unpause')
            button('RESTART',550,520,100,50,(205,0,0),(255,0,0),'play')
            button('MAIN MENU',300,520,200,50,(0,0,205),(0,0,255),'menu')
            pygame.display.update()
            clock.tick(30)

def unpaused():
    pygame.mixer.music.play()
    global pause
    pause=False
    
def introduction():
    pygame.mixer.music.stop()
    introduction=True
    while introduction:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.blit(instruction_background,(0,0))
        largetext=pygame.font.Font('freesansbold.ttf',80)
        smalltext=pygame.font.Font('freesansbold.ttf',20)
        mediumtext=pygame.font.Font('freesansbold.ttf',40)
        textSurf,textRect=text_objects("This is a car game in which you need to dodge the coming cars",smalltext)
        textRect.center=((350),(200))
        TextSurf,TextRect=text_objects("INSTRUCTION",largetext)
        TextRect.center=((400),(100))
        gamedisplays.blit(TextSurf,TextRect)
        gamedisplays.blit(textSurf,textRect)
        stextSurf,stextRect=text_objects("ARROW LEFT : LEFT TURN",smalltext)
        stextRect.center=((150),(400))
        hTextSurf,hTextRect=text_objects("ARROW RIGHT : RIGHT TURN" ,smalltext)
        hTextRect.center=((150),(450))
        sTextSurf,sTextRect=text_objects("CONTROLS",mediumtext)
        sTextRect.center=((350),(300))
        gamedisplays.blit(sTextSurf,sTextRect)
        gamedisplays.blit(stextSurf,stextRect)
        gamedisplays.blit(hTextSurf,hTextRect)
        button("BACK",600,450,100,50,(0,0,205),(0,0,255),"menu")
        pygame.display.update()
        clock.tick(30)



def background():
    gamedisplays.blit(backgroundpic,(0,0))
    gamedisplays.blit(backgroundpic,(0,200))
    gamedisplays.blit(backgroundpic,(0,400))
    gamedisplays.blit(backgroundpic,(700,0))
    gamedisplays.blit(backgroundpic,(700,200))
    gamedisplays.blit(backgroundpic,(700,400))
    gamedisplays.blit(yellow_strip,(400,0))
    gamedisplays.blit(yellow_strip,(400,100))
    gamedisplays.blit(yellow_strip,(400,200))
    gamedisplays.blit(yellow_strip,(400,300))
    gamedisplays.blit(yellow_strip,(400,400))
    gamedisplays.blit(yellow_strip,(400,500))
    gamedisplays.blit(strip,(120,0))
    gamedisplays.blit(strip,(120,100))
    gamedisplays.blit(strip,(120,200))
    gamedisplays.blit(strip,(680,0))
    gamedisplays.blit(strip,(680,100))
    gamedisplays.blit(strip,(680,200))

def score_system(passed,score,highscore):
    font=pygame.font.SysFont(None ,25)
    text=font.render('Passed'+str(passed),True,(0,0,0))
    score=font.render('Score'+str(score),True,(255,0,0))
    highestScore = font.render('Highscore'+str(highscore),True,(255,255,255))
    gamedisplays.blit(text,(10,50))
    gamedisplays.blit(score,(10,30))
    gamedisplays.blit(highestScore,(10,10))
def text_objects(text,font):
    textsurface=font.render(text,True,(0,0,0))
    return textsurface,textsurface.get_rect()

def message_display(text):
    largetext=pygame.font.Font('freesansbold.ttf',80)
    textsurf,textrect=text_objects(text,largetext)
    textrect.center=((display_width/2),(display_height/2))
    gamedisplays.blit(textsurf,textrect)
    pygame.display.update()
    time.sleep(3)
    game_loop()

def crash():
    pygame.mixer.music.stop()
    playsound('crash.mp3')
    message_display('YOU CRASHED')
    
   
    
    


def car(x,y):
    gamedisplays.blit(carimg,(x,y))

def game_loop():
    global pause
    pause=True
    x=(display_width*0.45)
    y=(display_height*0.8)
    x_change=0
    obstacle_speed=9
    obs=0
    obs_startx=random.randrange(200,(display_width-200))
    obs_starty=-750
    obs_width=56
    obs_height=125
    passed=0
    level=0
    score=0
    y2=7
    pygame.mixer.music.play(-1)
    try:
        highscore=int(getHighestScore())
    except:
        highscore=0
    
    bumped=False
    while not bumped:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                bumped = True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change=-5
                if event.key==pygame.K_RIGHT:
                    x_change=5
 
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change=0
        x+=x_change
            
        gamedisplays.fill((119,118,110))
        
        rel_y = y2%backgroundpic.get_rect().width
        gamedisplays.blit(backgroundpic,(0,rel_y-backgroundpic.get_rect().width))
        gamedisplays.blit(backgroundpic,(700,rel_y-backgroundpic.get_rect().width))
        if rel_y<800:
            gamedisplays.blit(backgroundpic,(0,rel_y))
            gamedisplays.blit(backgroundpic,(700,rel_y))
            gamedisplays.blit(yellow_strip,(400,rel_y))
            gamedisplays.blit(yellow_strip,(400,rel_y+100))
            gamedisplays.blit(yellow_strip,(400,rel_y+200))
            gamedisplays.blit(yellow_strip,(400,rel_y+300))
            gamedisplays.blit(yellow_strip,(400,rel_y+400))
            gamedisplays.blit(yellow_strip,(400,rel_y+500))
            gamedisplays.blit(yellow_strip,(400,rel_y-100))
            gamedisplays.blit(strip,(120,rel_y-200))
            gamedisplays.blit(strip,(120,rel_y+20))
            gamedisplays.blit(strip,(120,rel_y+30))
            gamedisplays.blit(strip,(680,rel_y-100))
            gamedisplays.blit(strip,(680,rel_y+20))
            gamedisplays.blit(strip,(680,rel_y+30))
        
        y2+= obstacle_speed

        
        obs_starty-=(obstacle_speed/4)
        obstacle(obs_startx,obs_starty,obs)
        obs_starty+=obstacle_speed
        car(x,y)
        score_system(passed,score,highscore)
        
        
        if obs_starty>display_height:
            obs_starty=0-obs_height
            obs_startx=random.randrange(170,(display_width-170))
            obs=random.randrange(0,7)
            passed+=1
            score+=10
            
            if int(passed)%10==0:
                level+=1
                obstacle_speed+=2
                largetext = pygame.font.Font('freesansbold.ttf',80)
                textsurf,textrect=text_objects('Level'+str(level),largetext)
                textrect.center=((display_width/2),(display_height/2))
                gamedisplays.blit(textsurf,textrect)
                pygame.display.update()
                time.sleep(3) 

        
        if level >= 5:
            obstacle_speed = 19
        
        if x>690-car_width or x<110:
            crash()
            
        if x>display_width-(car_width+110) or x<110:
            crash()
            

        if y<obs_starty+obs_height:
            if x> obs_startx and x< obs_startx+obs_width or x+car_width>obs_startx and x+car_width< obs_startx+obs_width:
                    crash()
                
        if highscore<score:
            highscore=score
        with open('highest score.txt','w') as f:
                f.write(str(highscore))
        
        button('Pause', 650,0,150,50, (0,0,205),(0,0,255),'pause')
        
        pygame.display.update()
        clock.tick(60)

intro_loop()
game_loop()
pygame.quit()
quit()
