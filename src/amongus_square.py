from InputWrapper import InputWrapper
import time

#open sandbox before running program
time.sleep(5)
wrapper = InputWrapper()

wrapper.move_left()
wrapper.move_left()

time.sleep(1)
wrapper.move_down()
wrapper.move_down()

time.sleep(1)
wrapper.move_right()
wrapper.move_right()

time.sleep(1)
wrapper.move_up()
wrapper.move_up()

time.sleep(1)