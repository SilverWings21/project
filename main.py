"""
Fighting_Game

Description:
"""
import tsapp
import random

window = tsapp.GraphicsWindow()
bg1 =  tsapp.Sprite("FantasyPlains.jpg",0,0)
player = tsapp.Sprite("Boulder.png",50,200)
e1 = tsapp.Sprite("SlimeGreen.png",700,200)
e1.scale = 0.5

window.add_object(bg1)
window.add_object(e1)
window.add_object(player)



kicked = tsapp.get_program_duration()
while window.is_running:
    now = tsapp.get_program_duration()
    
    if tsapp.is_key_down(tsapp.K_RIGHT) and now - kicked >= 300:
        player.image = "BoulderRunSheet.png"
        player.image_animation_rate = 20
        player.x_speed = 150
        player.scale = 0.8
        player.flip_x = False
        window.finish_frame()
    elif tsapp.is_key_down(tsapp.K_LEFT) and now - kicked >= 300:
        player.image = "BoulderRunSheet.png"
        player.image_animation_rate = 20
        player.x_speed = -150
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
    elif now - kicked >= 300 and now - kicked <= 320:
        player.image = "Boulder.png"
        
    window.finish_frame()
