import ConfigParser
import logging, sys

class Config:
    def __init__(self,file):
        self.file = file
	self.conf = ConfigParser.ConfigParser()

    def readFile(self):
        logging.debug('Read config file: '+self.file)
	self.conf.read(self.file)
        logging.debug('Config file read:')
        logging.debug(self.conf.sections())
	return None

    def readValue(self,section,param):
        logging.debug('Read config value: '+section+' - '+param)
	val = self.conf.get(section,param)
        logging.debug('Value: '+val)
        return int(val)



