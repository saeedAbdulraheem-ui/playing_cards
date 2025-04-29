import sensor, time, ml, uos, gc 

sensor.reset()   

sensor.set_pixformat(sensor.RGB565)     

sensor.set_framesize(sensor.QVGA)  

sensor.set_windowing((240, 240))  

sensor.skip_frames(time=2000) 

net = None 

labels = None 

try: 

    net = ml.Model("trained.tflite", load_to_fb=uos.stat('trained.tflite')[6] > (gc.mem_free() - (64*1024))) 

except Exception as e: 

    print(e) 

    raise Exception('Failed to load "trained.tflite", did you copy the .tflite and labels.txt file onto the mass-storage device? (' + str(e) + ')') 

try: 

    labels = [line.rstrip('\n') for line in open("labels.txt")] 

except Exception as e: 

    raise Exception('Failed to load "labels.txt", did you copy the .tflite and labels.txt file onto the mass-storage device? (' + str(e) + ')') 

try: 

    log_file = open("logfile.txt", "w")   

except Exception as e: 

    raise Exception('Failed to open "logfile.txt" for writing (' + str(e) + ')') 

clock = time.clock() 

while(True): 

    clock.tick() 

    img = sensor.snapshot() 

    predictions_list = list(zip(labels, net.predict([img])[0].flatten().tolist())) 

    for label, score in predictions_list: 

        line = "%s = %f\n" % (label, score) 

        print(line.strip()) 

        log_file.write(line) 

    fps_info = "%d fps\n" % clock.fps() 

    print(fps_info.strip()) 

    log_file.write(fps_info) 

log_file.flush()  

But after trying it, I found that the camera can't save the logfile without an SD card, so I tried to listen to the OpenMV port to realize logging, the code is as follows， 

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