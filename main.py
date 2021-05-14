"""
Fighting_Game
Description:
"""
import tsapp
import random
import pygame
player_hp = 100
e1_hp = 60
score = 0
lock = False
lock2 = False
level1 = True
level2 = False
window = tsapp.GraphicsWindow()
bg1 =  tsapp.Sprite("FantasyPlains.jpg",0,0)
bg2 =  tsapp.Sprite("NightSky.jpg",0,0)
bg3 =  tsapp.Sprite("Stage.png",0,0)
player = tsapp.Sprite("Boulder.png",50,200)

player_hb = tsapp.Sprite("DialogueBoxBlue.png",-400,-100)
trophy = tsapp.Sprite("Trophy.png", 400, 275)
arrow = tsapp.Sprite("BlueChevron.png", 900, 400)
player_h = tsapp.TextLabel("Acme-Regular.ttf",25,25,25,150,player_hp,tsapp.BLACK)
e1 = tsapp.Sprite("SlimeGreenIdleSheet.png",700,200)
e_hb = tsapp.Sprite("DialogueBoxBlue.png",e1.x,e1.y-25)
e_h = tsapp.TextLabel("Acme-Regular.ttf",15,e_hb.x+20,e_hb.y - 10,150,e1_hp,tsapp.BLACK)
death_text = tsapp.TextLabel("Flavors-Regular.ttf", 350, 100, 250, window.width, "GAME OVER", tsapp.RED)
win = tsapp.TextLabel("Rye-Regular.ttf", 100, 275, 225, window.width, "YOU WIN", tsapp.YELLOW)
score1 = tsapp.TextLabel("Acme-Regular.ttf", 50, 500, 100, 150, str(score), tsapp.WHITE)
n_l = tsapp.TextLabel("Acme-Regular.ttf", 50, 900, 350, 150, "Next Level", tsapp.BLACK)
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
window.add_object(score1)

hit = tsapp.get_program_duration()
kicked = tsapp.get_program_duration()

while window.is_running:
    mouse_x, mouse_y = tsapp.get_mouse_position()
    if level1:
        score1.text = score
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
        if player_hp == 0:
            window.add_object(bg2)
            window.add_object(death_text)
    
        if tsapp.is_key_down(tsapp.K_UP) and now - kicked >= 300 and player.y == 200:
            player_jump = 0
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
            score += 20
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
            score -= 5
        if e1_hp <= 0 and not lock:
            window.move_to_back(e1)
            window.move_to_back(e_hb)
            window.move_to_back(e_h)
            window.add_object(bg3)
            window.add_object(trophy)
            window.add_object(win)
            window.add_object(arrow)
            window.add_object(n_l)
            print("Your score is for level 1 is " + str(score))
            lock = True
            continue
        if arrow.is_colliding_point(mouse_x, mouse_y) and tsapp.was_mouse_pressed():
            bg3.destroy()
            trophy.destroy()
            arrow.destroy()
            win.destroy()
            n_l.destroy()
            player_hp = 100
            bg1.image = "GrassyCliffEdge.jpg"
            e1_hp = 80
            e1.x = 800
            level1 = False
            level2 = True
    if level2:
        window.move_to_front(e1)
        window.move_to_front(e_hb)
        window.move_to_front(e_h)
        mouse_x, mouse_y = tsapp.get_mouse_position()
        score1.text = score
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
        if player_hp == 0:
            window.add_object(bg2)
            window.add_object(death_text)
    
        if tsapp.is_key_down(tsapp.K_UP) and now - kicked >= 300 and player.y == 200:
            player_jump = 0
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
            score += 20
            if player.is_colliding_rect(e1):
                e1_hp -= 10
        elif now - kicked >= 300 and now - kicked <= 320:
            player.image = "Boulder.png"
            
        if e1.center_x > player.center_x and not player.center_x - e1.center_x > 100:
            e1.flip_x = True
            e1.image = "AirChildRunSheet.png"
            e1.image_animation_rate = 20
            e1.x_speed = -70
            window.finish_frame()
        elif e1.center_x < player.center_x and not player.center_x - e1.center_x < 100:
            e1.flip_x = False
            e1.image = "AirChildRunSheet.png"
            e1.image_animation_rate = 20
            e1.x_speed = 70
            window.finish_frame()
        elif player.center_x - e1.center_x < 100:
            e1.image = "AirChild.png"
            e1.image_animation_rate = 20
            e1.x_speed = 0
        if player.is_colliding_rect(e1) and now - hit >= 1000 and e1_hp > 0:
            hit = tsapp.get_program_duration()
            player_hp -= 10
            score -= 5
        if e1_hp <= 0 and not lock2 and level2:
            window.move_to_back(e1)
            window.move_to_back(e_hb)
            window.move_to_back(e_h)
            window.add_object(bg3)
            window.add_object(trophy)
            window.add_object(win)
            print("Your score is for level 2 is " + str(score))
            lock2 = True
            level2 = False


        

    window.finish_frame()
