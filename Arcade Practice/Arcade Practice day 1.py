import arcade


WIDTH = 1280
HEIGHT = 720

tree_x_positions = [100, 200, 300, 450, 530]
tree_y_positions = [100, 150, 500, 400, 200]
tree_positions = [
    (100, 100),
    (200, 150),
    (300, 500),
    (450, 400),
    (530, 200)
]


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
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
    for x_pos, y_pos in tree_positions:
        arcade.draw_circle_filled(x_pos, y_pos, 25, arcade.color.GO_GREEN)


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


if __name__ == '__main__':
    setup()