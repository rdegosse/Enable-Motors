import os
from CeleryPy import log
from CeleryPy import config_update

class MyFarmware():

    def get_input_env(self):
        prefix = self.farmwarename.lower().replace('-','_')
        
        self.input_movement_keep_active_x = os.environ.get(prefix+"_movement_keep_active_x", '1')
        self.input_movement_keep_active_y = os.environ.get(prefix+"_movement_keep_active_y", '1')
        self.input_movement_keep_active_z = os.environ.get(prefix+"_movement_keep_active_z", '1')
        self.input_debug = int(os.environ.get(prefix+"_debug", 1))

        if self.input_debug >= 1:
            log('movement_keep_active_x: {}'.format(self.input_movement_keep_active_x), message_type='debug', title=self.farmwarename)
            log('movement_keep_active_y: {}'.format(self.input_movement_keep_active_y), message_type='debug', title=self.farmwarename)
            log('movement_keep_active_z: {}'.format(self.input_movement_keep_active_z), message_type='debug', title=self.farmwarename)
            log('debug: {}'.format(self.input_debug), message_type='debug', title=self.farmwarename)
        
    def __init__(self,farmwarename):
        self.farmwarename = farmwarename
        self.get_input_env()

    def check_celerypy(self,ret):
        try:
            status_code = ret.status_code
        except:
            status_code = -1
        try:
            text = ret.text[:100]
        except expression as identifier:
            text = ret
        if status_code == -1 or status_code == 200:
            if self.input_debug >= 1: log("{} -> {}".format(status_code,text), message_type='debug', title=self.farmwarename + ' check_celerypy')
        else:
            log("{} -> {}".format(status_code,text), message_type='error', title=self.farmwarename + ' check_celerypy')
            raise

    def config_update_motors(self):
        config = {}
        config["movement_keep_active_x"] = int(self.input_movement_keep_active_x)
        config["movement_keep_active_y"] = int(self.input_movement_keep_active_y)
        config["movement_keep_active_z"] = int(self.input_movement_keep_active_z)
        self.check_celerypy(config_update(config_dict=config))
        
    
    def run(self):
        self.config_update_motors()
        