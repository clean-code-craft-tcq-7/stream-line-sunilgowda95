""" This file contains methods which will format the data into JSON """
import copy
import datetime
import json

class FormatBatteryParamsClass(object):
    """ format to json and return json string """
    def __init__(self, bms_params_raw_values):
        self.bms_params_raw_values = copy.deepcopy(bms_params_raw_values)
        
    def __check_for_params_keys(self):
        if set(["soc", "dod", "temp", "tv"]) <= set(self.bms_params_raw_values.keys()):
            return True
        return False
   
    def __generate_json(self):
        bms_params_json = {}
        bms_params_json["batt_params"] = self.bms_params_raw_values
        return bms_params_json

    def format_to_json_string(self):
        """ format to json and return json string """
        bms_params_json = {}
        bms_params_json["batt_params"] = {}
        message = "failed"
        # check if keys "soc", "dod", "temp", "tv" are present in dictionary
        if self.__check_for_params_keys():
            bms_params_json = self.__generate_json()
            message = "success"
        bms_params_json["ts"] = int(datetime.datetime.now().timestamp()*1000)
        bms_params_json["msg"] = message
        return json.dumps(bms_params_json)
        
