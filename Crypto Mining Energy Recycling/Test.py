rate = 1
num = 0
increasing = True
def up_down():
    global num
    if go_up: num += rate
    else: num -= rate
    if num == 10: increasing = False
    if num == 0: increasing = True
    print(num)