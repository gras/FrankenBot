'''
Created on Mar 21, 2015

@author: CDR Gras
'''

import os
import sys

import kovan as link

import constants as c 
import servo
import time


def init() :
    # set print to unbuffered
    sys.stdout = os.fdopen(sys.stdout.fileno(),'w',0)
    print "starting FrankenBot"
    link.enable_servos()
    link.camera_open()
    time.sleep(1.0)
    servo.moveShutter( c.shutterOpen )
    print "Initialized"
    servo.moveShutter( c.shutterClosed )

def testCamera():
    servo.moveShutter( c.shutterOpen )
    for i in range(10):
        link.camera_update()
        area = link.get_object_area(c.chanRed,0)
        print i, area
        


def shutdown():
    print "finished"
    link.camera_close()
    link.ao()
    time.sleep(1.0)


    

    
def DEBUG() :
    print "DEBUG"
    link.camera_close()
    link.ao()
    exit()