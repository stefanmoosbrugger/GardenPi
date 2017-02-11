# This file implements the light sensor class.
import sensor_base
if not testmode:
    import grovepi
import collections
import logging, sys
import time

class LightSensor(sensor_base.SensorBase):
    def __init__(self,port_number):
        self.port_num = port_number
        if not testmode:
            grovepi.pinMode(self.port_num, "INPUT")
        self.name = "LightSensor " + str(self.port_num)
        self.data = collections.deque(maxlen=50)

    def get_state(self):
        try:
            time.sleep(0.5)
            val = -1.0
            if not testmode:
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
