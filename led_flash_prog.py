import sensor, time, ml, uos, gc
import random
from machine import Pin


sensor.reset()                         # Reset and initialize the sensor.
sensor.set_pixformat(sensor.RGB565)    # Set pixel format to RGB565 (or GRAYSCALE)
sensor.set_framesize(sensor.QVGA)      # Set frame size to QVGA (320x240)
sensor.set_windowing((240, 240))       # Set 240x240 window.
sensor.skip_frames(time=2000)          # Let the camera adjust.

net = None
labels = None
start_time = None #track time when card is shown
my_label = None #store card label shown
waiting_for_card = True #track if card is shown to system
label_buffer = []
p0 = Pin('P0', Pin.OUT, Pin.PULL_UP)
p1 = Pin('P1', Pin.OUT, Pin.PULL_UP)
p2 = Pin('P2', Pin.OUT, Pin.PULL_UP)
p3 = Pin('P3', Pin.OUT, Pin.PULL_UP)

try:
    # load the model, alloc the model file on the heap if we have at least 64K free after loading
    net = ml.Model("trained.tflite", load_to_fb=uos.stat('trained.tflite')[6] > (gc.mem_free() - (64*1024)))
except Exception as e:
    print(e)
    raise Exception('Failed to load "trained.tflite", did you copy the .tflite and labels.txt file onto the mass-storage device? (' + str(e) + ')')

try:
    labels = [line.rstrip('\n') for line in open("labels.txt")]
except Exception as e:
    raise Exception('Failed to load "labels.txt", did you copy the .tflite and labels.txt file onto the mass-storage device? (' + str(e) + ')')

clock = time.clock()

while True:
    clock.tick()
    img = sensor.snapshot()
    predictions_list = list(zip(labels, net.predict([img])[0].flatten().tolist()))
    top_label, top_score = max(predictions_list, key=lambda x: x[1]) #get top label and confidence interval from list

    img.draw_rectangle((70, 70, 100, 100), color=(255, 0, 0))
    display_text = "{} ({:.2f})".format(top_label, top_score)

    img.draw_string(75, 75, display_text, color=(255, 255, 255), mono_space=False)

    #if a card is shown to the system
    if waiting_for_card:
        if top_score > 0.2 and start_time is None: #if start time is none and confidence iterval is above 50%
            start_time = time.time() #start the timer
        elif start_time is not None: #if start time is not none
            if top_score > 0.2: #prediction over 50%
                label_buffer.append(top_label)  #store label for prediction

            if time.time() - start_time > 7: # if 3 secs have based
                if len(label_buffer) > 0: #buffer list is not empty
                    my_label = max(set(label_buffer), key=label_buffer.count)  #set the label for the highest value in the buffer list
                    print(label_buffer)
                    print("Card registered:", my_label)
                else:
                    print("same card not detected")
                    my_label = None #no card registered no label assigned

                label_buffer.clear() #clear buffer list
                waiting_for_card = False #system confirms card

    else:
        if my_label is not None:
            print("Detected card label:", my_label)
            if my_label == "clubs":
                p0.high()
                p1.low()
                p2.low()
                p3.low()
            elif my_label == "diamonds":
                p0.low()
                p1.high()
                p2.low()
                p3.low()
            elif my_label == "hearts":
                p0.low()
                p1.low()
                p2.high()
                p3.low()
            elif my_label == "spades":
                p0.low()
                p1.low()
                p2.low()
                p3.high()
        else:
            print('no card registered')
            waiting_for_card = True
        time.sleep(1)

        #reset for next round
        start_time = None
        my_label = None



