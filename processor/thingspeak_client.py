import thingspeak
import collections
import logging, sys
import requests
import time
import json

class TSClient:
    w_api_key = "INSERT_THINGSPEAK_WRITE_API_KEY"
    r_api_key = "INSERT_THINGSPEAK_READ_API_KEY"
    channel_key = "INSERT CHANNEL ID"

    def __init__(self, *sens):
        self.sensors = sens
        r = requests.get('https://api.thingspeak.com/channels/'+self.channel_key+'/feeds.json?api_key='+self.r_api_key+'&results=2')
        channel = json.loads(r.content)["channel"]
        self.fieldNames = {}
        for key in channel:
            if "field" in key:
                self.fieldNames[str(channel[key])] = key
        logging.debug('Successfully initialized thingspeak client: %s fields -> %s', len(self.fieldNames), self.fieldNames)
        logging.debug('Number of sensors: %s', len(self.sensors))
        r.connection.close()


    def updateVals(self):
        req = 'https://api.thingspeak.com/update?api_key='+self.w_api_key
        for s in self.sensors:
            # get sensor state and check if it is a seq
            # if not generate a sequence
            val = s.get_state()
            if not isinstance(val, collections.Sequence):
                val = [val]
            i = 0
            for name in s.get_simple_name().split('_'):
                logging.debug('Write thingspeak value: name %s in %s with value %s', name, self.fieldNames[name], val[i])  
                req += '&'+self.fieldNames[name]+'='+str(val[i])
                i += 1
        logging.debug('HTTP GET: ' + req)
        r = requests.get(req)
        r.connection.close()
