""" This file consists of code which simulates following parameters
    1. SOC - 100 to 0 %
    2. DOD - 0 to 100 % 
        SOC and DOD are mutually opposite.
    3. Temperature - 25 - 40 celcius
        assumming valid operating Temperature
    4. Terminal Voltage - 12.6 to 10 Volts. """
import copy
import random

BMS_PARAMS_THRESHOLD = {
    "soc":{"max":100, "min":0, "count":50, "type":"int"},
    "temp":{"max":40, "min":25, "count":50, "type":"float"},
    "tv":{"max":12.6, "min":10, "count":50, "type":"float"}
}

class SimulateBatteryParamsClass(object):
    """ Class to simulate BMS parameters """
    def __init__(self, bms_params_thresholds):
        """ initialize max and minimum values for each params
            check if all required keys available in dictionary """
        self.init_done = False
        if set(["soc", "temp", "tv"]) <= set(bms_params_thresholds.keys()):
            if self.__check_for_child_keys(bms_params_thresholds):
                self.bms_params_thresholds = copy.deepcopy(bms_params_thresholds)
                self.init_done = True
        return

    def __check_for_child_keys(self, bms_params_thresholds):
        for key in bms_params_thresholds.keys():
            if set(["max", "min", "count", "type"]) > set(bms_params_thresholds[key].items()):
                return False
        return True

    def __generate_soc_dod(self, key, battery_params):
        # using soc / dod get other values
        generated_values = []
        for each in battery_params[key]:
            generated_values.append(abs(self.bms_params_thresholds[key]["max"]-each+self.bms_params_thresholds[key]["min"]))
        return generated_values
    
    def __check_for_soc_doc_and_simulate(self, key, battery_params):
        if key == "dod":
            return self.__generate_soc_dod("soc", battery_params)
        return self.__simulate_values(key)
    
    def __simulate_values(self, key):
        values = []
        if self.bms_params_thresholds[key]["type"] == "int":
            values = self.__simulate_int_values(key)
        elif self.bms_params_thresholds[key]["type"] == "float":
            values = self.__simulate_float_values(key)
        return values

    def __simulate_int_values(self, key):
        return [random.randint(self.bms_params_thresholds[key]["min"],\
            self.bms_params_thresholds[key]["max"]) \
            for _ in range(self.bms_params_thresholds[key]["count"])]
    
    def __simulate_float_values(self, key):
        return [round(random.uniform(self.bms_params_thresholds[key]["min"], \
            self.bms_params_thresholds[key]["max"]), 2) \
            for _ in range(self.bms_params_thresholds[key]["count"])]
    
    def get_battery_params(self):
        """ get array of each battery params """
        battery_params = {}
        for key in self.bms_params_thresholds.keys():
            battery_params[key] = self.__check_for_soc_doc_and_simulate(key, battery_params)
            if key == "soc":
                key = "dod"
                battery_params[key] = self.__check_for_soc_doc_and_simulate(key, battery_params)
        return battery_params
