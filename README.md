ESP32 CAM virtual mouse program tutorial

how to run the program:

1. prepare the tools & materials needed, namely ESP32 CAM, CP2102 FTDI Module, 5 female to female jumper cables, and micro-USB cables.
2. assemble the microcontroller using the above tools and materials as in the repository file circuit image.
3. enter the arduino software, open the web_camera_esp32.ino file, then connect the microcontroller that has been assembled using a micro-USB cable to the PC / laptop.
4. compile the code in the arduino software until it is complete, after that open the serial monitor, then unplug the jumper cable that connects pin 100 with GND on the ESP32 CAM, then click the reset button on the ESP32 CAM, the camera ip will appear along with the resolution.
5. copy the camera ip and one of the resolutions, then create a folder that contains the detection file. py and virtualmouse.py, after that open the folder using vscode or the editor code that you use.
6. in the deteksitangan.py and virtualmouse.py files, enter the camera ip code that has been copied on the arduino serial monitor.
7. then run the python code and the program will run.
