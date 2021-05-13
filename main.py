"""
Fighting_Game
Description:
"""
import tsapp
import random
import pygame
player_hp = 100
e1_hp = 60

window = tsapp.GraphicsWindow()
bg1 =  tsapp.Sprite("FantasyPlains.jpg",0,0)
player = tsapp.Sprite("Boulder.png",50,200)

player_hb = tsapp.Sprite("DialogueBoxBlue.png",-400,-100)
player_h = tsapp.TextLabel("Acme-Regular.ttf",25,25,25,150,player_hp,tsapp.BLACK)
e1 = tsapp.Sprite("SlimeGreenIdleSheet.png",700,200)
e_hb = tsapp.Sprite("DialogueBoxBlue.png",e1.x,e1.y-25)
e_h = tsapp.TextLabel("Acme-Regular.ttf",15,e_hb.x+20,e_hb.y - 10,150,e1_hp,tsapp.BLACK)
e_hb.scale = 0.1
player_hb.scale = 0.2
e1.scale = 0.5
e1.image_animation_rate = 20

window.add_object(bg1)
window.add_object(e1)
window.add_object(e_hb)
window.add_object(e_h)
window.add_object(player)
window.add_object(player_hb)
window.add_object(player_h)


hit = tsapp.get_program_duration()
kicked = tsapp.get_program_duration()
while window.is_running:
    clock = pygame.time.Clock()
    clock.tick(20)
    now = tsapp.get_program_duration()
    player_h.text = player_hp
    player_jump = 11
    e_h.text = e1_hp
    e_h.x = e1.x+20
    e_h.y = e1.y - 10
    e_hb.x = e1.x
    e_hb.y = e1.y -25
    if tsapp.is_key_down(tsapp.K_UP) and now - kicked >= 300 and player.y == 200:
        player_jump = 0
        print(player_jump)
    if player_jump <= 10:
        player.y_speed -= 400
        player_jump += 1
    if player_jump > 10 and player.y < 200:
        player.y_speed += 100
    if player.y > 200:
        player.y_speed = 0
        player.y = 200
    if player.y == 200 and player_jump > 10:
        player.y_speed = 0
        
    if tsapp.is_key_down(tsapp.K_RIGHT) and now - kicked >= 300:
        player.image = "BoulderRunSheet.png"
        player.image_animation_rate = 20
        player.x_speed = 200
        player.scale = 0.8
        player.flip_x = False
        window.finish_frame()
    elif tsapp.is_key_down(tsapp.K_LEFT) and now - kicked >= 300:
        player.image = "BoulderRunSheet.png"
        player.image_animation_rate = 20
        player.x_speed = -200
        player.scale = 0.8
        player.flip_x = True
        window.finish_frame()
    elif now - kicked >= 300:
        player.image = "Boulder.png"
        player.image_animation_rate = 0
        player.x_speed = 0
        player.scale = 1
        
    if tsapp.was_key_pressed(tsapp.K_SPACE):
        player.image = "BoulderKick.png"
        kicked = tsapp.get_program_duration()
        player.x_speed = 0
        player.image_animation_rate = 0
        player.scale = 1
        if player.is_colliding_rect(e1):
            e1_hp -= 10
    elif now - kicked >= 300 and now - kicked <= 320:
        player.image = "Boulder.png"
        
    if e1.center_x > player.center_x and not player.center_x - e1.center_x > 100:
        e1.flip_x = True
        e1.image = "SlimeGreenHopSheet.png"
        e1.image_animation_rate = 20
        e1.x_speed = -70
        window.finish_frame()
    elif e1.center_x < player.center_x and not player.center_x - e1.center_x < 100:
        e1.flip_x = False
        e1.image = "SlimeGreenHopSheet.png"
        e1.image_animation_rate = 20
        e1.x_speed = 70
        window.finish_frame()
    elif player.center_x - e1.center_x < 100:
        e1.image = "SlimeGreenIdleSheet.png"
        e1.image_animation_rate = 20
        e1.x_speed = 0
    if player.is_colliding_rect(e1) and now - hit >= 1000 and e1_hp > 0:
        hit = tsapp.get_program_duration()
        player_hp -= 10
    if e1_hp <= 0:
        window.move_to_back(e1)
        window.move_to_back(e_hb)
        window.move_to_back(e_h)
    

    window.finish_frame()
