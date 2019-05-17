import arcade

WIDTH = 1280
HEIGHT = 720

# Index Positions

BTN_X = 0
BTN_Y = 1
BTN_W = 2
BTN_H = 3
BTN_PRESSED = 4
BTN_DEFAULT_COLOUR = 5
BTN_DEFAULT_PRESSED_COLOUR = 6

#           0    1    2    3   4                   5                         6
#           x    y    w    h   bool          color_default              color_clicked
button1 = [500, 350, 250, 100, False, arcade.color.BLIZZARD_BLUE, arcade.color.ORIOLES_ORANGE]

def setup():
    arcade.open_window(WIDTH, HEIGHT, "Button")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press
    window.on_mouse_release = on_mouse_release
    arcade.run()


def update(delta_time):
    pass


def on_draw():
    if button1[BTN_PRESSED]:
        color = button1[BTN_DEFAULT_PRESSED_COLOUR]
    else:
        color = button1[BTN_DEFAULT_COLOUR]
    arcade.draw_xywh_rectangle_filled(button1[BTN_X],
                                      button1[BTN_Y],
                                      button1[BTN_W],
                                      button1[BTN_H],
                                      color
                                      )


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    print(f'clicked at {x}, {y}')

    if (button1[BTN_X] + button1[BTN_W] >
            x > button1[BTN_X] and
            button1[BTN_Y] <
            y < button1[BTN_Y] + button1[BTN_H]):
        print('Button clicked')
        button1[BTN_PRESSED] = True
    else:
        button1[BTN_PRESSED] = False


def on_mouse_release(x, y, button, modifiers):
    if (button1[BTN_X] + button1[BTN_W] >
            x > button1[BTN_X] and
            button1[BTN_Y] <
            y < button1[BTN_Y] + button1[BTN_H]):
        print('Button released at button')
        button1[BTN_PRESSED] = False


if __name__ == '__main__':
    setup()