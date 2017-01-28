# This file implements the soil moisture sensor class.
import sensor

class SoilMoistureSensor(sensor.Sensor):
    def __init__(self,port_number):
        self.port_num = port_number
        self.name = "SoilMoistureSensor " + self.port_num
        grovepi.pinMode(self.port_num, "INPUT")
        self.data = collections.deque(maxlen=50)

    def get_state(self):
        try:
            val = grovepi.analogRead(self.port_num)
            self.data.append(val)
            logging.debug('Read sensor (%s) value: %s', self.name, val)
            return val
        except IOError:
            logging.error('Error while reading sensor (%s) value', self.name)

    def get_states(self):
        return collections.list(self.data)

    def set_state(self, val):
        logging.error('Called set_state to unidirectional sensor (%s)', self.name)
        raise Error( "Called set_state to unidirectional sensor" )
