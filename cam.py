PROGRAM 
import os
i=0
while(i<=5):
    os.system("fswebcam -F 4 --fps 30 -r 1200*1000 /home/pi/group2/"+str(i)+".jpg")
    i=i+1
    print("pic taken")
OUTPUT
pic taken
pic taken
pic taken 
pic taken
pic taken
