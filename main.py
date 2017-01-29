import logging, sys
import collections
import time
import grovepi

import sensor.sensor
import sensor.light_relay
import sensor.light_sensor
import sensor.pump_relay
import sensor.temp_sensor
import sensor.water_atomizer
import sensor.soil_moisture_sensor
import sensor.ventilation_relay

import rule
import processor.rule_processor

from lambdas import *

def main():
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

    # instantiate the sensors
    vra = sensor.ventilation_relay.VentilationRelay(2)  # digital port 2
    waa = sensor.water_atomizer.WaterAtomizer(3)        # digital port 3
    ths = sensor.temp_sensor.TempHumiditySensor(4)    	# digital port 4
    pra = sensor.pump_relay.PumpRelay(5)             	# digital port 5
    lra = sensor.light_relay.LightRelay(6)            	# digital port 6   

    sms = sensor.soil_moisture_sensor.SoilMoistureSensor(0)    	# analog port 0
    sls = sensor.light_sensor.LightSensor(1)           		# analog port 1

    # create the rules
    pump_rule = rule.Rule(pump_lambda, [sms, pra])             # activate water pump if sensor value 
    light_rule = rule.Rule(light_lambda, [4,23])             # activate light between 4:00 and 23:00
    ventilation_rule = rule.Rule(ventilation_lambda, [0,2])  # activate ventilation from minute 0 to minute 2
    atomizer_rule = rule.Rule(atomizer_lambda, [ths])          # humidify the air if needed      

    # create processors
    rp = processor.rule_processor.RuleProcessor([pump_rule, pra], [light_rule, lra], [ventilation_rule, vra], [atomizer_rule, waa])

    # run the GardenPi
    while 1:
        rp.process()    # process the rules and switch the relays if needed
	time.sleep(10)       # sleep 10 seconds

if __name__ == "__main__":
    main()
