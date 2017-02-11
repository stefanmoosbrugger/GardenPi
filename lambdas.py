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
    if sensor[1].get_state() == 1:
        pump_state = 1
    if sensor[1].get_state() == 0:
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

def light_lambda(time_pair):
    logging.debug('Call to light lambda')    
    start = time_pair[0]
    end = time_pair[1]
    logging.debug('From: %s', time_pair[0])
    logging.debug('To: %s', time_pair[1])    
    t = time.localtime()
    if  t.tm_hour >= start and t.tm_hour <= end:
        logging.debug('New light state: 1')
        return 1
    else:
        logging.debug('New light state: 0')
        return 0

def ventilation_lambda(time_pair):
    logging.debug('Call to ventilation lambda')
    start = time_pair[0]
    end = time_pair[1]
    logging.debug('From: %s', time_pair[0])
    logging.debug('To: %s', time_pair[1])        
    t = time.localtime()
    if  t.tm_min >= start and t.tm_min <= end:
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
