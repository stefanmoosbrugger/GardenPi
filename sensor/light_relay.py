# This file implements the light actor class.
import sensor_base
import __builtin__
if not __builtin__.testmode:
    import grovepi
import logging, sys

class LightRelay(sensor_base.SensorBase):
    def __init__(self,port_number):
        self.port_num = port_number
        if not __builtin__.testmode:
            grovepi.pinMode(self.port_num, "OUTPUT")
        self.name = "LightRelay " + str(self.port_num)
        self.state = 0

    def get_state(self):
        return self.state

    def get_states(self):
        return self.state

    def set_state(self, val):
        assert val == 1 or val == 0
        if not __builtin__.testmode:
            if val:
                grovepi.digitalWrite(self.port_num, 1); 
                self.state = 1
            else:
                grovepi.digitalWrite(self.port_num, 0); 
                self.state = 0
        logging.debug('Set val to actor (%si, port %s): %s', self.name, self.port_num, self.state)
