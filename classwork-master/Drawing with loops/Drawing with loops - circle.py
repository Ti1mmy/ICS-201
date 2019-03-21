import arcade


WIDTH = 640
HEIGHT = 480


def update(delta_time):
    pass


def on_draw():
    arcade.start_render()
    # Draw in here...
    for x in range(20, WIDTH - 20 + 1, 40):
        arcade.draw_circle_filled(x, 50, 20, arcade.color.ORANGE_PEEL)
def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "Arcade Test")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release

    arcade.run()


if __name__ == '__main__':
    setup()