from microbit import *
x = 2
y = 2
while True:
    tilt_x = accelerometer.get_x()
    tilt_y = accelerometer.get_y()
    
    if tilt_x < 0 and x > 0:
        x -= 1
    elif tilt_x > 0 and x < 4:
        x += 1
    if tilt_y < 0 and y > 0:
        y -= 1
    elif tilt_y > 0 and y < 4:
        y += 1
    display.set_pixel(x,y,9) 
    sleep(100)
    display.clear()
    

