# This file implements the pump actor class.
import sensor

class PumpRelay(sensor.Sensor):
    def __init__(self,port_number):
        self.port_num = port_number
        self.name = "PumpRelay " + self.port_num
        pinMode(self.port_num, OUTPUT)
        self.state = LOW

    def get_state(self):
        return self.state

    def get_states(self):
        return self.state

    def set_state(self, val):
        assert val == HIGH or val == LOW
        if val:
            grovepi.digitalWrite(self.port_num, HIGH); 
            self.state = HIGH
        else:
            grovepi.digitalWrite(self.port_num, LOW); 
            self.state = LOW
        logging.debug('Set val to actor (%s): %s', self.name, self.state)
