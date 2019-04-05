import arcade
import random

WIDTH = 1280
HEIGHT = 720


def update(delta_time):
    pass


def on_draw():
    arcade.start_render()
    # Draw in here...
    for i in range(40):
        arcade.draw_circle_filled(random.randint(0, WIDTH), random.randint(0, HEIGHT), random.randint(1, 40), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        arcade.set_background_color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        arcade.draw_rectangle_filled(WIDTH / 2, HEIGHT - 50, 10, 200, arcade.color.BLACK)
        arcade.draw_circle_filled(WIDTH / 2, HEIGHT - 200, 80, arcade.color.SILVER)
    for i in range(5):
        arcade.draw_text('UUNCE', random.randint(0, WIDTH,), random.randint(0, HEIGHT), arcade.color.RED, font_size = 18, font_name = 'Arial')

def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "UUUUNNNNCEEEEE")
    arcade.set_background_color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    arcade.schedule(update, 1/240)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release

    arcade.run()


if __name__ == '__main__':
    setup()