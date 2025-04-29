import serial
import time
import os

COM_PORT = 'COM9' 
BAUD_RATE = 115200
SAVE_PATH = r"D:\University of Limerick\Mini Proj\log.txt"
def main():
    if not os.path.exists(os.path.dirname(SAVE_PATH)):
        os.makedirs(os.path.dirname(SAVE_PATH))

    ser = serial.Serial(COM_PORT, BAUD_RATE, timeout=1)
    print("Listening on", COM_PORT, "... Saving to", SAVE_PATH)

    with open(SAVE_PATH, "w", encoding="utf-8") as f:
        while True:
            try:
                line = ser.readline()
                if line:
                    decoded_line = line.decode('utf-8', errors='ignore').strip()
                    print(decoded_line)
                    f.write(decoded_line + '\n')
                    f.flush()
            except KeyboardInterrupt:
                print("Stopped by user.")
                break
            except Exception as e:
                print("Error:", e)
                break

    ser.close()
    print("Serial port closed.")

if __name__ == "__main__":
    main()
