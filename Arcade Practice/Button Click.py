"""
Button Click

1. Draw the button with a function called `draw_button`.
2. Check if the mouse if over the button with a function called `mouse_is_over`.

Exercies
1. Add a couple more buttons.
2. Create a list of buttons. Use a for loop to draw and check hover.
3. Use a for loop to generate buttons.
"""

import arcade


WIDTH = 640
HEIGHT = 480

# Key for button index values
# This makes dealing with buttons as lists slightly easier.
BTN_X = 0
BTN_Y = 1
BTN_WIDTH = 2
BTN_HEIGHT = 3
BTN_IS_CLICKED = 4
BTN_COLOR = 5
BTN_CLICKED_COLOR = 6

# You might want to Google:
# - python namedtuple
# - python classes
# Those would be better ways to store objects like our button.
button1 = [200, 200, 300, 50, False, arcade.color.BLUE, arcade.color.GREEN]
button2 = [200, 140, 100, 30, False, arcade.color.BLUE, arcade.color.GREEN]

buttons = [button1, button2]


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
    window.on_mouse_release = on_mouse_release

    arcade.run()


def update(delta_time):
    pass


def on_draw():
    arcade.start_render()
    # Draw in here...
    for i in range(2):
        draw_button(buttons[i])


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    print(f"Click at ({x}, {y})")

    # Check if click happened on button1
    if mouse_hover(x, y, button1):
        button1[BTN_IS_CLICKED] = True

    if mouse_hover(x, y, button2):
        button2[BTN_IS_CLICKED] = True


def on_mouse_release(x, y, button, modifiers):
    # When you let go of the mouse, all buttons should be set to False.
    for i in range(2):
        buttons[i][BTN_IS_CLICKED] = False



def mouse_hover(x, y, button) -> bool:
    if (x > button[BTN_X] and x < button[BTN_X] + button[BTN_WIDTH] and
            y > button[BTN_Y] and y < button[BTN_Y] + button[BTN_HEIGHT]):
        return True
    else:
        return False


def draw_button(button):
    # Select the appropriate color to draw with
    if button[BTN_IS_CLICKED]:
        color = button[BTN_CLICKED_COLOR]
    else:
        color = button[BTN_COLOR]

    # Draw button1
    arcade.draw_xywh_rectangle_filled(button[BTN_X],
                                      button[BTN_Y],
                                      button[BTN_WIDTH],
                                      button[BTN_HEIGHT],
                                      color)



if __name__ == '__main__':
    setup()