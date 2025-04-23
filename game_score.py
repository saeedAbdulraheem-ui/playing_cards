import sensor, time, ml, uos, gc
import random


sensor.reset()                         # Reset and initialize the sensor.
sensor.set_pixformat(sensor.RGB565)    # Set pixel format to RGB565 (or GRAYSCALE)
sensor.set_framesize(sensor.QVGA)      # Set frame size to QVGA (320x240)
sensor.set_windowing((240, 240))       # Set 240x240 window.
sensor.skip_frames(time=2000)          # Let the camera adjust.

net = None
labels = None
count = 0 #initialising counter for game
player_score = 0 #initialising counter for player score
system_score = 0 #initialising counter for system
suit_score = {'hearts':4, 'spades': 3, 'clubs':2, 'diamonds':1} #dictionary for scoring of cards
start_time = None #track time when card is shown
my_label = None #store card label shown
waiting_for_card = True #track if card is shown to system
system_suit = random.choice(list(suit_score.keys())) #randomly generate suits for player to play against
label_buffer = []

#function to give camera 3 secs to register card
def timer(start_time):
    if start_time != None:
        if time.time() - start_time > 5:
            print('card registered')
        return True

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

    #put label and confidence interval inside box
  #  label, conf = max(predictions_list, key=lambda x: x[1])
    display_text = "{} ({:.2f})".format(top_label, top_score)

    #draw label
    img.draw_string(75, 75, display_text, color=(255, 255, 255), mono_space=False)





    #if a card is shown to the system
    if waiting_for_card:
        if top_score > 0.5 and start_time is None: #if start time is none and confidence iterval is above 50%
            start_time = time.time() #start the timer
        #elif start_time is not None and time.time() - start_time > 3: #wait 3 seconds
           # my_label = top_label #label is registered for card
           # waiting_for_card = False #system confirms card
           # print("Card registered:", my_label)
        elif start_time is not None: #if start time is not none
            if top_score > 0.5: #prediction over 50%
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
        if my_label is not None: #if card registered by system
            if suit_score[my_label] > suit_score[system_suit]: #player wins if card value greater than system
                print('You win')
                player_score += 1
            elif suit_score[system_suit] > suit_score[my_label]: #system wins if card value greater than player
                print('system wins')
                system_score += 1
            else:
                print('its a draw')
        else:
            print('no card registered')

        #set up next round
        count += 1 #increment counter
        if count >= 5: #end game after 5 rounds
            if system_score > player_score:
                print('The winner is system')
            elif player_score > system_score:
                print('The winner is player')
            else:
                print('It\'s a draw')
            break

        #allow pause for five seconds so player can change card
        print('Next round starts in:')
        for i in range(10, 0, -1):
            print(i)
            time.sleep(1)

        #reset for next round
        start_time = None
        my_label = None
        waiting_for_card = True
        system_suit = random.choice(list(suit_score.keys()))



