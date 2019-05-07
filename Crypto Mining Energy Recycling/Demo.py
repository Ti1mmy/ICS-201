import arcade
import random

WIDTH = 1280
HEIGHT = 720

heat = int(input('What is the power consumption of one of your miners? (W) ')) * int(input('How many miners do you have? '))
print(f'The total amount of heat your facility generates is equivalent to {heat / 1000000} megawatts! (± {(heat / 1000000) * 0.1} megawatts)')

pressure = 0
power_output = 0
decreasing_pressure = False
decreasing_power = False
def update(delta_time):
    pass


def on_draw():
    global pressure
    global power_output
    global decreasing_pressure
    global decreasing_power
# Logic:
    # Pressure

    if pressure == 0:
        decreasing_pressure = False
    if not decreasing_pressure:
        pressure += 3
    if pressure == 165:
        decreasing_pressure = True
    if decreasing_pressure:
        pressure -= 55

    # Power
    if power_output == 0:
        decreasing_power = False
    if pressure == 18:
        decreasing_power = False
    if not decreasing_power and pressure > 21:
        power_output += 2
    if pressure == 55:
        decreasing_power = True
    if decreasing_power:
        power_output = (power_output // 3)
    print(power_output)

    arcade.start_render()
# Loading Sprites
    # General
    arrow = arcade.load_texture('arrow.png', 0, 0, 512, 512)

    # Graphs
    barometer = arcade.load_texture('barometer.png', 0, 0, 512, 512)
    power = arcade.load_texture('electricity.png', 0, 0, 2273, 2400)

    # Container
    liquid = arcade.load_texture('liquid.png', 0, 0, 1600, 450)

    # Gas
    gas = arcade.load_texture('gas.png', 0, 0, 512, 512)
# Graphs
    arcade.draw_line(950, 525, 1150, 525, arcade.color.BLACK, 1)  # x - axis
    arcade.draw_line(950, 525, 950, 690, arcade.color.BLACK, 1)  # y - axis
    arcade.draw_texture_rectangle(990, 505, 30, 30, barometer)  # Pressure
    arcade.draw_texture_rectangle(1100, 505, 30, 30, power)  # Power output
    # Bars
    arcade.draw_line(990, 525, 990, 526 + pressure, arcade.color.BLUE, 25)
    arcade.draw_line(1100, 525, 1100, 526 + power_output, arcade.color.RED, 25)
# Container
    arcade.draw_texture_rectangle(250, 235, 200, 110, liquid)  # Liquid
    arcade.draw_rectangle_filled(250, 180, 200, 35, arcade.color.WHITE)  # Covers the bit that extends too much
    arcade.draw_xywh_rectangle_outline(150, 200, 200, 120, arcade.color.BLACK, 7)
    arcade.draw_rectangle_outline(250, 251, 400, 27, arcade.color.BLACK, 7)

    # Temperature Gradient for Water
    x_gradient = 51
    red = 255
    blue = 0
    for i in range(200):
        arcade.draw_line(x_gradient, 238, x_gradient, 264, [red, 0, blue], 2)
        x_gradient += 2
        red -= 0.6375 * 2
        blue += 0.6375 * 2

    # Radiator
    x_radiator = 175
    for i in range(7):
        arcade.draw_line(x_radiator, 225, x_radiator, 280, arcade.color.BLACK, 5)
        x_radiator += 25

    # Water Direction Arrows
    arcade.draw_texture_rectangle(25, 250, 40, 40, arrow)
    arcade.draw_texture_rectangle(475, 250, 40, 40, arrow)

    # Gas
    arcade.draw_texture_rectangle(random.randint(175, 345), random.randint(290, 300), 25, 25, gas)

# Actual Power Generation Part
    arcade.draw_xywh_rectangle_outline(150, 400, 200, 120, arcade.color.BLACK, 7)  # Piston Section 1
    arcade.draw_rectangle_outline(250, 360, 50, 75, arcade.color.BLACK, 7)  # Tubing
    arcade.draw_rectangle_filled(250, 360, 43, 87, arcade.color.WHITE)  # Removing Lines



    # Piston Movement

# Pressure Bar

    arcade.draw_rectangle_outline(600, 450, 40, 370, arcade.color.BLACK, 7)
    arcade.draw_texture_rectangle(550, 598, 20, 20, arrow)  # arrow is positioned at 330 because 2x 165
    # Gradient
    red = 0
    green = 255
    blue = 0
    y_gradient = 268.5
    for i in range(pressure):
        arcade.draw_line(583.5, y_gradient, 616.5, y_gradient, [red, green, blue], 2)
        y_gradient += 2
        red += 1.54
        green -= 1.54




def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, 'Power recycling demo')
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/180)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


if __name__ == '__main__':
    setup()
