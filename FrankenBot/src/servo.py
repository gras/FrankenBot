'''
Created on Mar 21, 2015

@author: CDR Gras
'''

import time 
import kovan as link
import constants as c

def moveShutter( endPos, speed=10 ):
    moveServo( c.shutter, endPos, speed )

def moveServo( servo, endPos, speed=10 ) :
    # speed of 1 is slow
    # speed of 2000 is fast
    # speed of 10 is the default
    now = link.get_servo_position( servo )
    if now > endPos:
        speed = -speed
    for i in range (now, endPos, speed ):
        link.set_servo_position( servo, i)
        time.sleep(0.010)
    link.set_servo_position( servo, endPos )
    time.sleep( 0.010 )