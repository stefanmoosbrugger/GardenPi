import __builtin__
__builtin__.testmode = False
import logging, sys
import threading
import collections
import time
import os
if not __builtin__.testmode:
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
import thingspeak_client
#import web_interface

import lambdas
import rule
import config

def main():
	if __builtin__.testmode:
		logging.warn('!!!!!!TESTMODE ACTIVATED!!!!!!')		
	logging.basicConfig(stream=sys.stderr)
	logging.getLogger().setLevel(logging.DEBUG)

	while 1:
		try:
			# read config file
			c = config.Config(os.getcwd()+"/config.ini")
			c.readFile()
			# instantiate the sensors
			vra = ventilation_relay.VentilationRelay(c.readValue("ventilation","port")) 	# digital port 7
			waa = water_atomizer.WaterAtomizer(c.readValue("atomizer","port"))	   	# digital port 8
			ths = temp_sensor.TempHumiditySensor(c.readValue("thsensor","port"))		# digital port 4
			pra = pump_relay.PumpRelay(c.readValue("pump","port"))				# digital port 2
			lra = light_relay.LightRelay(c.readValue("light","port"))			# digital port 3   

			sms = soil_moisture_sensor.SoilMoistureSensor(c.readValue("smsensor","port"))	# analog port 0
			sls = light_sensor.LightSensor(c.readValue("lightsensor","port"))	 	# analog port 1

			# create the rules
			pump_rule = rule.Rule(lambdas.pump_lambda, [sms, pra])		 # activate water pump if sensor value 
			light_rule = rule.Rule(lambdas.light_lambda, [c.readValue("light","from"), c.readValue("light","to")])		 		# activate light between 4:00 and 23:00
			ventilation_rule = rule.Rule(lambdas.ventilation_lambda, [c.readValue("ventilation","from"), c.readValue("ventilation","to")])  # activate ventilation from minute 0 to minute 2
			atomizer_rule = rule.Rule(lambdas.atomizer_lambda, [ths])	 # humidify the air if needed	  

			# create processors
			rp = rule_processor.RuleProcessor([pump_rule, pra], [light_rule, lra], [ventilation_rule, vra], [atomizer_rule, waa])
			ts = thingspeak_client.TSClient(vra, waa, ths, pra, lra, sms, sls)
			#wi = web_interface.fill_sensor_list([vra, waa, ths, pra, lra, sms, sls])

			# run the GardenPi threads
			rp.process()
			ts.updateVals()
			time.sleep(60)
		except KeyboardInterrupt:
			raise
		except:
			print(sys.exc_info()[0])
			pass

if __name__ == "__main__":
	main()
