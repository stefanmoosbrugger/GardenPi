# This file implements the light sensor class.
import sensor
import grovepi
import collections
import logging, sys
import time

class LightSensor(sensor.Sensor):
    def __init__(self,port_number):
        self.port_num = port_number
	grovepi.pinMode(self.port_num, "INPUT")
	self.name = "LightSensor " + str(self.port_num)
        self.data = collections.deque(maxlen=50)

    def get_state(self):
        try:
	    time.sleep(0.5)
            val = grovepi.analogRead(self.port_num)
            self.data.append(val)
            logging.debug('Read sensor (%s, port %s) value: %s', self.name, int(self.port_num), val)
            return val
        except IOError:
            logging.error('Error while reading sensor (%s) value', self.name)

    def get_states(self):
        return collections.list(self.data)

    def set_state(self, val):
        logging.error('Called set_state to unidirectional sensor (%s)', self.name)
        raise Error( "Called set_state to unidirectional sensor" )
