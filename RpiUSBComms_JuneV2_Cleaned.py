import serial
import time
'''
USB Serial Communications between Raspberry Pi and Arduino
'''
if __name__ == "__main__":
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.flush()
    status  = 0
    while status < 2:
        if status == 0:
            ser.write(b"Wash\n")
            line = ser.readline().decode('utf-8').rstrip()
			print(line)
            while True:
                line = ser.readline().decode('utf-8').rstrip()
                print(line)
                if line == "Completed":
                    ser.flush()
                    break
                time.sleep(2)
        elif status == 1:
            ser.write(b"StartSter\n")
            line = ser.readline().decode('utf-8').rstrip()
            while line != "JCompleted":
                line = ser.readline().decode('utf-8').rstrip()
                print(line)
                time.sleep(2)  
        ser.flush()
        status += 1