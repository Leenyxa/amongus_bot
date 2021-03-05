from InputWrapper import InputWrapper
from ImageSearchWrapper import ImageSearchWrapper
import time
import autoit
import keyboard

wrapper = InputWrapper()
imagewrapper = ImageSearchWrapper()

if __name__ == '__main__':
    # open sandbox before running program
    time.sleep(2)

    print('Searching for chat icon')
    pos = imagewrapper.chat()

    if pos[0] != -1:
        # "left" stand for left click, 1243 and 1035 is x and y coordinates and 1 is number of clicks.
        autoit.mouse_click("left", pos[0], pos[1], 1)
        time.sleep(2)
        print('Chatting!')
        keyboard.write('Hi this is Leenybot')
        wrapper.enter()
        time.sleep(1)
        autoit.mouse_click("left", pos[0], pos[1], 1)
    else:
        print('Chat icon not found')


    time.sleep(1)

    # toggle for dance party
    dance = 0
    if dance == 1:
        print('Dancing!')
        wrapper.move_left()
        wrapper.move_right()
        wrapper.move_left()
        wrapper.move_right()
        wrapper.move_left()
        wrapper.move_right()
        wrapper.move_left()
        wrapper.move_right()
        wrapper.move_left()
        wrapper.move_right()
        wrapper.move_left()
        wrapper.move_right()
        wrapper.move_left()
        wrapper.move_right()
        wrapper.move_left()
        wrapper.move_right()
        wrapper.move_left()
        wrapper.move_right()
        wrapper.move_left()
        wrapper.move_right()


    # Start task
    print('Figuring out what task to do')




    wrapper.e_key()
    time.sleep(0.5)

    # Empty garbage
    print('Searching for trash handle')
    pos = imagewrapper.garbage()
    if pos[0] != -1:
        autoit.mouse_click_drag(pos[0]+20, pos[1], pos[0]+20, pos[1]+500, "left", 40)
        time.sleep(0.5)
        print('Emptied trash')
    else:
        print('Could not find trash handle')

    # Divert power
    print('Trying to divert power')
    pos = imagewrapper.divert_power()
    if pos[0] != -1:
        autoit.mouse_click_drag(pos[0] + 10, pos[1], pos[0] + 20, pos[1] - 100, "left", 20)
        time.sleep(0.5)
        print('Diverted power')
    else:
        print('Could not divert power')

    print('Finishing diverting power')
    pos = imagewrapper.divert_power2()
    if pos[0] != -1:
        autoit.mouse_click("left", pos[0]+5, pos[1]+10, 1)
        time.sleep(0.5)
        print('Diverted power')
    else:
        print('Could not divert power')

    print('Looking for wires')
    pos = imagewrapper.wires()
    print("position : ", pos[0], pos[1])
