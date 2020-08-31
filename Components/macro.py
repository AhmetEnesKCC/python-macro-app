



import pythoncom
import keyboard

from PyHook3 import cpyHook,HookConstants



def mouse_macro(selected_button, press_time, key):
    XBUTTON1 = 0x0001
    XBUTTON2 = 0x0002

    wm = {0x020B: "WM_XBUTTONDOWN", 0x020C: "WM_XBUTTONUP", 0x0201: "WM_LBUTTONDOWN", }

    def mouse_handler(msg, x, y, data, flags, time, hwnd, window_name):

        name = wm.get(msg, None)
        if name:

            xb = data >> 16  # high word indicates which xbutton
            print(name, xb & XBUTTON1, xb & XBUTTON2)
            if name == 'WM_XBUTTONDOWN':
                if xb == selected_button:
                    for _i in range(0, press_time):
                        keyboard.press_and_release(f'{key}')
                # cpyHook.cUnhook(HookConstants.WH_MOUSE_LL)

        return True

    try:
        cpyHook.cSetHook(HookConstants.WH_MOUSE_LL, mouse_handler)
        pythoncom.PumpMessages()
    finally:
        cpyHook.cUnhook(HookConstants.WH_MOUSE_LL)
#
#
# def mouse_endless_macro():
#     user32 = ctypes.windll.user32
#
#     XBUTTON1 = 0x0001
#     XBUTTON2 = 0x0002
#
#     wm = {0x020B: "WM_XBUTTONDOWN", 0x020C: "WM_XBUTTONUP", 0x0201: "WM_LBUTTONDOWN", }
#
#     def mouse_handler(msg, x, y, data, flags, time, hwnd, window_name):
#         name = wm.get(msg, None)
#         if name:
#             xb = data >> 16  # high word indicates which xbutton
#             print(name, xb & XBUTTON1, xb & XBUTTON2)
#             if name == 'WM_XBUTTONDOWN':
#                 keyboard.press('`')
#                 time.sleep(1)
#                 cpyHook.cUnhook(HookConstants.WH_MOUSE_LL)
#
#         return True
#
#     try:
#         cpyHook.cSetHook(HookConstants.WH_MOUSE_LL, mouse_handler)
#         pythoncom.PumpMessages()
#     finally:
#         cpyHook.cUnhook(HookConstants.WH_MOUSE_LL)
