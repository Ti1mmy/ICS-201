import arcade


WIDTH = 1280
HEIGHT = 720

# make variables for x, y, radius
circle_x = int(input('what is the x location? '))
circle_y = int(input('what is the y location? '))
circle_radius = int(input('what is the circle radius? '))

arcade.open_window(WIDTH, HEIGHT, "My Drawing")
arcade.set_background_color(arcade.color.WHITE)

arcade.start_render() # this is when you sandwich draw commands for anything you want shown on the window.
# Begin drawing

arcade.draw_circle_filled(circle_x, circle_y, circle_radius, arcade.color.BLUE_GREEN) # x, y, radius

# End drawing
arcade.finish_render()
arcade.run()