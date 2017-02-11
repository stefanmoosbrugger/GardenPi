import __builtin__
__builtin__.testmode = True
import logging, sys
import threading
import collections
import time
if __builtin__.testmode == True:
    import grovepi

sys.path.append("./sensor")
sys.path.append("./processor")
import ventilation_relay
import water_atomizer
import temp_sensor
import pump_relay
import light_relay
import light_sensor
import soil_moisture_sensor

import rule_processor
import web_interface

import lambdas
import rule

def rule_processor_thread(rp):
    while 1:
        rp.process()
        time.sleep(3)

def main():
    if not testmode:
        logging.warn('!!!!!!TESTMODE ACTIVATED!!!!!!')        
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

    # instantiate the sensors
    vra = ventilation_relay.VentilationRelay(2) # digital port 2
    waa = water_atomizer.WaterAtomizer(3)       # digital port 3
    ths = temp_sensor.TempHumiditySensor(4)    	# digital port 4
    pra = pump_relay.PumpRelay(5)             	# digital port 5
    lra = light_relay.LightRelay(6)            	# digital port 6   

    sms = soil_moisture_sensor.SoilMoistureSensor(0)    	# analog port 0
    sls = light_sensor.LightSensor(1)           		# analog port 1

    # create the rules
    pump_rule = rule.Rule(lambdas.pump_lambda, [sms, pra])             # activate water pump if sensor value 
    light_rule = rule.Rule(lambdas.light_lambda, [4,23])             # activate light between 4:00 and 23:00
    ventilation_rule = rule.Rule(lambdas.ventilation_lambda, [0,2])  # activate ventilation from minute 0 to minute 2
    atomizer_rule = rule.Rule(lambdas.atomizer_lambda, [ths])          # humidify the air if needed      

    # create processors
    rp = rule_processor.RuleProcessor([pump_rule, pra], [light_rule, lra], [ventilation_rule, vra], [atomizer_rule, waa])
    wi = web_interface.fill_sensor_list([vra, waa, ths, pra, lra, sms, sls])

    # run the GardenPi threads
    rpt = threading.Thread(target=rule_processor_thread, args=(rp,))
    rpt.start()
    threads = [rpt]
    for t in threads:
        t.join()
    time.sleep(1)

if __name__ == "__main__":
    main()
