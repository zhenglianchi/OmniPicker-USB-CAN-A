from OmniPicker import OmniPicker_Interface
import time

print('''The converter is equipped with two built - in conversion protocols, \n
      one is a fixed 20 byte protocol and the other is a variable length protocol. \n
      Please ensure that the variable length protocol is selected in the supporting software \n
      and click the Set and Start button to issue a configuration command to the converter''')

test = OmniPicker_Interface()
test.connect()
time.sleep(3)
test.gripper_half_open()
time.sleep(3)
test.gripper_close()
time.sleep(3)
test.gripper_open()
time.sleep(3)
test.disconnect()
