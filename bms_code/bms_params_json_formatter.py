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
            if self.__check_for_child_keys(self.bms_params_raw_values):
                self.bms_params_raw_values = copy.deepcopy(self.bms_params_raw_values)
        return

    def __check_for_child_keys(self):
        for key in self.bms_params_raw_values.keys():
            if set(["max", "min", "count", "type"]) > set(self.bms_params_raw_values[key].items()):
                return False
        return True
    
    def __generate_json_string(self):
        bms_params_json_string = {}
        bms_params_json_string["batt_params"] = self.bms_params_raw_values
        bms_params_json_string["ts"] = int(datetime.datetime.now().timestamp()*1000)
        return json.dumps(bms_params_json_string)

    def format_to_json_string(self):
        """ format to json and return json string """
        bms_params_json = ""
        message = "failed"
        # check if keys "soc", "dod", "temp", "tv" are present in dictionary
        if self.__check_for_params_keys():
            if self.__check_for_child_keys():
                bms_params_json = self.__generate_json_string()
                message = "success"
        return bms_params_json, message
        
