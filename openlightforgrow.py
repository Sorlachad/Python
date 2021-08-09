import serial
import time
from datetime import datetime
from serial.serialutil import Timeout
now = datetime.now()
today = now.today
while True :
    try:
        pass
        #relay = serial.Serial("COM3",9600,timeout=1)
    except:
        pass

    now = datetime.now()
    start_hour=16
    start_minute=10
    #################
    end_hour =16
    end_minute=45
    hournow=now.hour
    
    """"
    23 10
 23 0 1 2 3 4 5 6 7 8 9 10 11 12 13
    >
     23>
    """ 
    if now.minute==start_minute:
        check=0
    if start_hour > end_hour :
        today=now.day #28 28
        if ( now.hour >= start_hour and check==0 and now.hour!=end_hour)  : #23 23
            print('on')
            print(now)
            time.sleep(5)
            #relay.write('onlightfortree\n'.encode()) #12v
            #relay.flush()
        elif (now.hour == end_hour and now.minute<=end_minute ):
            print('on')
            print(now)
            time.sleep(5)
            #relay.write('onlightfortree\n'.encode()) #12v
            #relay.flush()
        else  :
            today=now.day
            print('off')
            print(now)
            time.sleep(5)
            check=1
            #relay.write('offlightfortree\n'.encode()) #12v
            #relay.flush()
    if end_hour > start_hour :
        if today==now.day:
            if ( now.hour >= start_hour and check==0 and now.hour!=end_hour)  : #23 23
                print('on')
                print(now)
                time.sleep(5)
                #relay.write('onlightfortree\n'.encode()) #12v
                #relay.flush()
            elif (now.hour == end_hour and now.minute<=end_minute ):
                print('on')
                print(now)
                time.sleep(5)
                #relay.write('onlightfortree\n'.encode()) #12v
                #relay.flush()
            else  :
                today=now.day
                print('off')
                print(now)
                time.sleep(5)
                check=1
                #relay.write('offlightfortree\n'.encode()) #12v
                #relay.flush()
        else :#    0          23                                                 0           2
            if ( now.hour <= start_hour  ) and ( now.hour!=end_hour )  : #and now.minute>= start_minute
                print('on')
                print(now)
                time.sleep(5)
                #relay.write('onlightfortree\n'.encode()) #12v
                #relay.flush()
            elif (now.hour == end_hour and now.minute<end_minute ):
                print('on')
                print(now)
                time.sleep(5)
                #relay.write('onlightfortree\n'.encode()) #12v
                #relay.flush()
            else  :
                print('off')
                print(now)
                time.sleep(5)
                today=now.day
                check=1
                #relay.write('offlightfortree\n'.encode()) #12v
            #   relay.flush()
    
    