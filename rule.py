# This file implements the rule class.
import logging, sys
 
class Rule:
    def __init__(self,(lam),(sensors)):
        self.functor = lam
        self.sensors = list(sensors)

    def check(self):
        logging.debug('Checking a rule')        
        return self.functor(self.sensors)
