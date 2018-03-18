# This file implements the sensor class.
# Main purpose is to provide a base class
# for the different kinds of sensors/actors
# that are used in the GardenPi project.
import logging, sys
import random

class SensorBase:
    def __init__(self,port_number):
        self.port_num = port_number
        self.name = ""

    def get_state(self):
        logging.error('Called get_name to base class')
        raise NotImplementedError( "Should have implemented this" ) 

    def get_states(self):
        logging.error('Called get_name to base class')
        raise NotImplementedError( "Should have implemented this" ) 

    def set_state(self, val):
        logging.error('Called get_name to base class')
        raise NotImplementedError( "Should have implemented this" ) 

    def get_port_num(self):
        return self.port_num
    
    def get_name(self):
        return self.name

    def get_simple_name(self):
        return self.simple_name
