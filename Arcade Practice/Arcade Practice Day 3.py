import arcade
import random

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

startgame = False

star_x_positions = []
star_y_positions = []
y_plane = HEIGHT / 2
keydown = False
keyup = False
boom = False
frametime = 0
SPEED = 4
for i in range(10):
    x = random.randrange(WIDTH / 2, WIDTH * 2)
    y = random.randrange(HEIGHT)
    star_x_positions.append(x)
    star_y_positions.append(y)


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
    if startgame:
        global y_plane
        global boom
        global frametime, SPEED
        frametime += 1
        for x_range in range(len(star_x_positions)):
            star_x_positions[x_range] -= SPEED
            if star_x_positions[x_range] <= 0:
                star_y_positions[x_range] = random.randrange(0, HEIGHT)
                star_x_positions[x_range] = random.randrange(WIDTH, WIDTH * 2)
        if y_plane >= 50:
            if keydown:
                y_plane -= 8
        if y_plane <= HEIGHT - 50:
            if keyup:
                y_plane += 8
        for detect in range(len(star_x_positions)):
            if (star_x_positions[detect] - 50 <= 250 <= star_x_positions[detect] + 50) and (
                    star_y_positions[detect] - 50 <= y_plane <= star_y_positions[detect] + 50):
                arcade.close_window()

        if frametime % 120 == 0:
            SPEED += 0.35

def on_draw():
    if button1[BTN_PRESSED]:
        color = button1[BTN_DEFAULT_PRESSED_COLOUR]
    elif not button1[BTN_PRESSED] and not startgame:
        color = button1[BTN_DEFAULT_COLOUR]
    arcade.draw_xywh_rectangle_filled(button1[BTN_X],
                                      button1[BTN_Y],
                                      button1[BTN_W],
                                      button1[BTN_H],
                                      color
                                      )
    else:
        for x_star, y_star in zip(star_x_positions, star_y_positions):
            arcade.draw_circle_filled(x_star, y_star, 2, arcade.color.WHITE)
        plane = arcade.load_texture('plane.png', 0, 0, 420, 420)
        arcade.draw_texture_rectangle(250, y_plane, 100, 100, plane)
        arcade.draw_text(str(frametime), 1200, 700, arcade.color.WHITE)



def on_key_press(key, modifiers):
    if startgame:
        global keydown
        global keyup
        if key == arcade.key.DOWN:
            keydown = True
        if key == arcade.key.UP:
            keyup = True


def on_key_release(key, modifiers):
    if startgame:
        global keyup
        global keydown
        if key == arcade.key.DOWN:
            keydown = False
        if key == arcade.key.UP:
            keyup = False


def on_mouse_press(x, y, button, modifiers):
    print(f'clicked at {x}, {y}')

    if (button1[BTN_X] + button1[BTN_W] >
            x > button1[BTN_X] and
            button1[BTN_Y] <
            y < button1[BTN_Y] + button1[BTN_H]):
        print('Button clicked')
        button1[BTN_PRESSED] = True



def on_mouse_release(x, y, button, modifiers):
    global startgame
    if (button1[BTN_X] + button1[BTN_W] >
            x > button1[BTN_X] and
            button1[BTN_Y] <
            y < button1[BTN_Y] + button1[BTN_H]):
        print('Button released at button')
        startgame = True


if __name__ == '__main__':
    setup()