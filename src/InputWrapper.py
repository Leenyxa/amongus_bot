import ctypes
import time
import autoit

time.sleep(2)
#"left" stand for left click, 1243 and 1035 is x and y coordinates and 1 is number of clicks.
autoit.mouse_click("left", 1243, 1035, 1)

# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)


class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]


class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]


class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]


# directx scan codes
# http://www.gamespp.com/directx/directInputKeyboardScanCodes.html

class InputWrapper:
    def __init__(self):
        SendInput = ctypes.windll.user32.SendInput

        self.W = 0x11
        self.A = 0x1E
        self.S = 0x1F
        self.D = 0x20
        self.UP = 0xC8
        self.LEFT = 0xCB
        self.RIGHT = 0xCD
        self.DOWN = 0xD0
        self.ENTER = 0x1C
        self.ESC = 0x01
        self.TWO = 0x03
        self.Q = 0x10
        self.R = 0x13
        self.E = 0x12



    def move_left(self):
        self._press_key(self.LEFT)
        time.sleep(0.1)
        self._release_key(self.LEFT)

    def move_up(self):
        self._press_key(self.UP)
        time.sleep(1)
        self._release_key(self.UP)

    def move_right(self):
        self._press_key(self.RIGHT)
        time.sleep(0.1)
        self._release_key(self.RIGHT)

    def move_down(self):
        self._press_key(self.DOWN)
        time.sleep(1)
        self._release_key(self.DOWN)

    def enter(self):
        self._press_key(self.ENTER)
        time.sleep(0.2)
        self._release_key(self.ENTER)

    def e_key(self):
        self._press_key(self.E)
        time.sleep(0.1)
        self._release_key(self.E)

    def _press_key(self, hexKeyCode):
        extra = ctypes.c_ulong(0)
        ii_ = Input_I()
        ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra))
        x = Input(ctypes.c_ulong(1), ii_)
        ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

    def _release_key(self, hexKeyCode):
        extra = ctypes.c_ulong(0)
        ii_ = Input_I()
        ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008 | 0x0002, 0,
                            ctypes.pointer(extra))
        x = Input(ctypes.c_ulong(1), ii_)
        ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

if __name__ == '__main__':
    #while (True):
    #    PressKey(0x11)
    #    time.sleep(1)
    #    ReleaseKey(0x11)
    #    time.sleep(1)
    time.sleep(2)
    wrapper = InputWrapper()

    wrapper.move_left()
