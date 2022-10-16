from pyjoycon import GyroTrackingJoyCon, get_R_id
import time

joycon_id = get_R_id()
joycon = GyroTrackingJoyCon(*joycon_id)

while True:
    # print("joycon pointer:  ", joycon.pointer)
    # print("joycon rotation: ", joycon.rotation)
    # print("joycon direction:", joycon.direction)
    print(f"Pointer = {joycon.pointer} A button pressed = {joycon.get_button_a()}", end="\r")
    time.sleep(0.1)