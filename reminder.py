import time 
from pygame import mixer
initiate = time.time()
prime_time = time.time()
# range for water is 3600 to 3660
#range for eye 1800 to 1860
#range for exersise 2700 to 2760
def take_log(n):
    f= open("reminder_soup.txt","a")
    loct = time.asctime(time.localtime(time.time()))
    f.write(loct , f"this is time for{n} \n")#if we do a= then no. of string store in a 
    

     
def plays(s=str()):
    # Starting the mixer
    mixer.init()

    # Loading the song
    mixer.music.load(s)

    # Setting the volume
    mixer.music.set_volume(0.7)

    # Start playing the song
    mixer.music.play()

    # infinite loop


while(True):
    current = time.time()
    if (120<=(current-initiate)<= 125):
        plays("eye.mp3")
        take_log("eyye")
        while(True):
            response = input("please enter done if you are done")
            if response == "done" :
                mixer.music.stop()
                break
        
    if (180<=(current-initiate)<= 185):
        plays("exersise.mp3")
        take_log("exerssise")
        while(True):
            response = input("please enter done if you are done")
            if response == "done" :
                mixer.music.stop()
                break
        
    if (240<=(current-initiate)<= 245):
        plays("Drink.mp3")
        take_log("drinnk")
        while(True):
            response = input("please enter done if you are done")
            if response == "done" :
                mixer.music.stop()
                break
        initiate = time.time()
    if (300<=(current - prime_time)<=305):
         break
    

        

