from pyjoycon import GyroTrackingJoyCon, get_R_id
import time

joycon_id = get_R_id()
joycon = GyroTrackingJoyCon(*joycon_id)

print(joycon.get_button_a)

while True:
    # print("joycon pointer:  ", joycon.pointer)
    # print("joycon rotation: ", joycon.rotation)
    # print("joycon direction:", joycon.direction)
    print(joycon.pointer, end="\r")
    time.sleep(0.05)