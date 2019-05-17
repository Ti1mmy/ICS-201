import arcade
import random

WIDTH = 1280
HEIGHT = 720

rain_x_positions = []
rain_y_positions = []

for i in range(90):
    x = random.randrange(0, WIDTH)
    y = random.randrange(600, 720)
    rain_y_positions.append(y)
    rain_x_positions.append(x)
def setup():
    arcade.open_window(WIDTH, HEIGHT, "Rain")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


def update(delta_time):
    for y in range(len(rain_y_positions)):
        rain_y_positions[y] -= 40
        if rain_y_positions[y] <= 0:
            rain_y_positions[y] = random.randint(700, 720)
            rain_x_positions[y] = random.randrange(WIDTH)

def on_draw():
    global rain_y_positions
    arcade.start_render()
    for x, y in zip(rain_x_positions, rain_y_positions):
        arcade.draw_circle_filled(x, y, 15, arcade.color.BLUE)

def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


if __name__ == '__main__':
    setup()