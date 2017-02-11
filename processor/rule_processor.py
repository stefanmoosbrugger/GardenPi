import logging, sys

class RuleProcessor:
    def __init__(self,*rule_relay_pairs):
        logging.debug('Starting Rule Processor')
        self.rrp = rule_relay_pairs

    def process(self):
        for pair in self.rrp:
            logging.debug('Processing a rule')
            old_state = pair[1].get_state()
            state = pair[0].check()
            pair[1].set_state(state)
            logging.debug('Old state: %s', old_state)
            logging.debug('Got state: %s', state)
            logging.debug('Read state: %s', pair[1].get_state())
                        
