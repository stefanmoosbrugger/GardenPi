import logging, sys
import time
import __builtin__

if __builtin__.testmode == True:
    HIGH = 1
    LOW = 0

def pump_lambda(sensor):
    logging.debug('Call to pump_lambda')
    val = sensor[0].get_state()
    pump_state = -1
    if sensor[1].get_state() == HIGH:
        pump_state = 1
    if sensor[1].get_state() == LOW:
        pump_state = 0

    logging.debug('Received val: %s', val)
    logging.debug('Current pump state: %s', pump_state)
    
    if pump_state == 0 and val < 500:
        logging.debug('New pump state: 1')
        return 1
    if pump_state == 0 and val >= 500:
        logging.debug('New pump state: 0')
        return 0
    if pump_state == 1 and val < 700:
        logging.debug('New pump state: 1')
        return 1
    if pump_state == 1 and val >= 700:
        logging.debug('New pump state: 0')        
        return 0

def light_lambda(t):
    logging.debug('Call to light lambda')    
    start = t[0]
    end = t[1]
    logging.debug('From: %s', t[0])
    logging.debug('To: %s', t[1])    
    if  time.localtime().tm_hour >= start and time.localtime().tm_hour <= end:
        logging.debug('New light state: 1')
        return 1
    else:
        logging.debug('New light state: 0')
        return 0

def ventilation_lambda(t):
    logging.debug('Call to ventilation lambda')
    start = t[0]
    end = t[1]
    logging.debug('From: %s', t[0])
    logging.debug('To: %s', t[1])        
    if  time.localtime().tm_min >= start and time.localtime().tm_min <= end:
        logging.debug('New ventilation state: 1')
        return 1
    else:
        logging.debug('New ventilation state: 0')
        return 0

def atomizer_lambda(sensor):
    logging.debug('Call to atomizer lambda')
    [temp, humidity] = sensor[0].get_state()

    logging.debug('Temperature: %s', temp)
    logging.debug('Humidity: %s', humidity)    

    if humidity <= 50.0:
        logging.debug('New atomizer state: 1')
        return 1
    else:
        logging.debug('New atomizer state: 0')
        return 0
