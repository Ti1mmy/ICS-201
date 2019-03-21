import arcade


WIDTH = 640
HEIGHT = 480


def update(delta_time):
    pass


def on_draw():
    arcade.start_render()
    # Draw in here...
    arcade.draw_rectangle_filled(320, 340, 20, 60, arcade.color.ASPARAGUS)
    arcade.draw_ellipse_filled(320, 240, 80, 100, arcade.color.PUMPKIN)
    arcade.draw_circle_filled(320, 240, 10, arcade.color.ORANGE_PEEL)
    arcade.draw_triangle_filled(290, 280, 280, 265, 300, 265, arcade.color.ORANGE_PEEL)
    arcade.draw_triangle_filled(350, 280, 340, 265, 360, 265, arcade.color.ORANGE_PEEL)
def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "Pumpkin")
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