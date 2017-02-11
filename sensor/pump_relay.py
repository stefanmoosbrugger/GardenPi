# This file implements the pump actor class.
import sensor_base
if not testmode:
    import grovepi
import logging, sys

class PumpRelay(sensor_base.SensorBase):
    def __init__(self,port_number):
        self.port_num = port_number
        if not testmode:
            grovepi.pinMode(self.port_num, "OUTPUT")
        self.name = "PumpRelay " + str(self.port_num)
        self.state = 0

    def get_state(self):
        return self.state

    def get_states(self):
        return self.state

    def set_state(self, val):
        assert val == 1 or val == 0
        if not testmode:
            if val:
                grovepi.digitalWrite(self.port_num, 1); 
                self.state = 1
            else:
                grovepi.digitalWrite(self.port_num, 0); 
                self.state = 0
        logging.debug('Set val to actor (%s, port %s): %s', self.name, self.port_num, self.state)
