import arcade


WIDTH = 1280
HEIGHT = 720


def setup():
    arcade.open_window(WIDTH, HEIGHT, "21 May 2019")
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
    pass


def on_draw():
    arcade.start_render()
    # Draw in here...
    draw_face(WIDTH / 2, HEIGHT / 2)


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


def draw_face(x, y):

    # Face
    arcade.draw_ellipse_filled(x, y, 150, 200, arcade.color.PEACH)

    # Right Eye
    arcade.draw_ellipse_filled(x + 35, y + 50, 25, 40, arcade.color.WHITE)
    arcade.draw_circle_filled(x + 35, y + 50, 12, arcade.color.BROWN_NOSE)
    arcade.draw_circle_filled(x + 35, y + 50, 5, arcade.color.BLACK)

    # Left Eye
    arcade.draw_ellipse_filled(x - 35, y + 50, 25, 40, arcade.color.WHITE)
    arcade.draw_circle_filled(x - 35, y + 50, 12, arcade.color.BROWN_NOSE)
    arcade.draw_circle_filled(x - 35, y + 50, 5, arcade.color.BLACK)

    # Mouth
    arcade.draw_circle_filled(x, y - 75, 50, arcade.color.BLACK)


if __name__ == '__main__':
    setup()