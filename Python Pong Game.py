#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame,sys
import time
import random

#general setup
pygame.init()
clock = pygame.time.Clock()

#set up main display surface
screen_width = 1300
screen_height = 1000
screen = pygame.display.set_mode((screen_width,screen_height))
#name of window
pygame.display.set_caption("Safwan's Pong Game")


#set up game objects
#place game objects in a rectangle (easy to locate in this manner)
#game ball
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15,30,30)
#player
player = pygame.Rect(screen_width-20,screen_height/2 - 70,10,140)
#opponent
opponent = pygame.Rect(10, screen_height/2 - 70,10,140)

#set up colours
background_colour = pygame.Color("grey12")
#store light_grey colour as tuple
light_grey = (200,200,200)


#set up ball velocity vectors + randomize it
ball_velocity_x = 7 *random.choice([1,-1])
ball_velocity_y = 7 *random.choice([1,-1])

#set up player movement velocity vector
player_velocity = 0

#set up opponent velocity vector
opponent_velocity = 15


def player_animation():
    #movement of player
    player.y += player_velocity
    #dealing with condition of when player hits ends of screen
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def ball_animation():
    #globally define variables so can use inside the function, locally
    global ball_velocity_x, ball_velocity_y
    global player_score, opponent_score

    #moving the ball incrementally
    ball.x = ball.x + ball_velocity_x
    ball.y = ball.y + ball_velocity_y
    #dealing with wall collisions
    if ball.top <= 0 or ball.bottom >= screen_height:
        #reverse component
        ball_velocity_y *= -1    
    if ball.left <= 0:
        #player score increments by 1 
        player_score += 1
        #restart ball
        ball_restart()
    if ball.right >= screen_width:
        #opponent score increments by 1
        opponent_score += 1
        #call restart_ball function within ball_animation function
        ball_restart()
    #dealing with pad, ball collision
    #object.colliderect(other object) boolean method
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_velocity_x *= -1

def opponent_animation():
    
    if opponent.top < ball.y:
        #increment opponent's movement to go downward
        opponent.top += opponent_velocity
    
    if opponent.bottom > ball.y:
        #increment opponent's movement to go upward
        opponent.top -= opponent_velocity 
    
    #dealing with condition of when opponent hits ends of screen
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height
        
def ball_restart():
    global ball_velocity_x , ball_velocity_y
    #move centre of ball to middle of screen
    #let random library vary the ball's movement via random.choice method
    time.sleep(1)
    ball.center = (screen_width/2,screen_height/2)
    ball_velocity_y *= random.choice([1,-1])
    ball_velocity_x *= random.choice([1,-1])
        
#creating a score keeper
player_score = 0
opponent_score = 0
#font syntax
#name of font + size
game_font= pygame.font.Font("freesansbold.ttf",32)

        
#event loop 
while True:
    for event in pygame.event.get():
        # conditional statement
        if event.type == pygame.QUIT:
            #best way to close the tab + entire application
            pygame.quit()
            sys.exit()
            
        #look for a pressed down key
        if event.type == pygame.KEYDOWN:
            #sub condition, specifically for the down key button
            if event.key == pygame.K_DOWN:
                #player's velocity increments by 7 each time down button is presssed
                player_velocity += 7
            if event.key == pygame.K_UP:
                player_velocity -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_velocity -= 7
            if event.key == pygame.K_UP:
                player_velocity += 7
                
                
    # Game Logic
    ball_animation()
    player_animation()
    opponent_animation()
    
    #visuals
    #out of the for loop
    #draw the rectangles(notice the order here)
    screen.fill(background_colour)
    pygame.draw.rect(screen,light_grey,player)
    pygame.draw.rect(screen,light_grey,opponent)
    pygame.draw.ellipse(screen,light_grey,ball)
    pygame.draw.aaline(screen,light_grey,(screen_width/2,0),(screen_width/2,screen_height))
    
    #player + opponent tag
    player_tag_image = game_font.render("PLAYER",True,light_grey)
    screen.blit(player_tag_image,(950,20))
    
    opponent_tag_image = game_font.render("OPPONENT",True,light_grey)
    screen.blit(opponent_tag_image,(250,20))
    
   
    #opponent + score text
    player_score_image = game_font.render(f"{player_score}",False,light_grey)
    #display image surface on main screen
    screen.blit(player_score_image,(1000,65))
    
    opponent_score_image = game_font.render(f"{opponent_score}",False,light_grey)
    screen.blit(opponent_score_image,(325,65))
    
            
    #update the window
    pygame.display.flip()
    clock.tick(60)


# In[ ]:




