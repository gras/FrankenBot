'''
Created on Mar 21, 2015

@author: CDR Gras
'''
import kovan as link
from time import sleep
from kovan import msleep

def main() :
#    link.create_connect()

    ###############################################    

    print "Frankenbot lives!!"
    while not link.side_button_clicked():
        link.motor(0,100)
        link.motor(1,-100)
        link.motor(2,100)
        link.motor(3,-100)
        msleep(500)
        link.motor(3,100)
        link.motor(2,-100)
        link.motor(1,100)
        link.motor(0,-100)
        msleep(500)
    print "Frankenbot dies!!"

    # HHH



    ###############################################    
#    link.create_disconnect()
'''
    drive forward and stop after a given time
    default speed is 100 m/sec
    default time is 5 sec
'''
def distance(speed=100, time=5.0) :
    link.create_drive_straight(-speed)
    sleep(time)
    link.create_stop()



if __name__ == "__main__":
    import os
    import sys
    sys.stdout = os.fdopen(sys.stdout.fileno(),'w',0)
    main()