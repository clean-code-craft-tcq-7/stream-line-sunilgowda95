import unittest
from unittest.mock import patch

"""
Input : dictionary containing parent keys "soc", "dod", "temp" and "tv" 
    with each parent key containing "max", "min", "count", "type"
Output : dictionary containing "soc", "dod", "temp", "tv" keys
    with list of random values equal to count defined in Input.
Test Cases : 
    1.  Input dictionary with valid param, also mock random module with 
            fixed values.
        Output check for all the keys, length of output list, check value
            of the list using mocked values.
    2.  Input dictionary with valid param.
        Output check for all the keys, length of output list, check value
            of the list are in the given range.
"""

BMS_PARAMS_THRESHOLD = {
    "test_params" : {
        "soc":{"max":90, "min":10, "count":40, "type":"int"},
        "dod":{"max":90, "min":10, "count":40, "type":"int"},
        "temp":{"max":38, "min":20, "count":30, "type":"float"},
        "tv":{"max":12.2, "min":10.5, "count":30, "type":"float"},
    },
    "mocked" : {"int": 5, "float":5.0}
}

class TestSimulateBatteryParamsClass(unittest.TestCase):
    """ this class contains methods to test methods in bms_sender """
    def __check_for_child_keys(self, bms_params):
        if set(["soc", "dod", "tem[", "tv"]) > set(bms_params.keys()):
            return False
        return True    
    
    def __check_mocked_int_float_value(self, bms_params_list, BMS_PARAMS_THRESHOLD, key):
        mocked_value = BMS_PARAMS_THRESHOLD["mocked"][BMS_PARAMS_THRESHOLD["test_params"][key]["type"]]
        if len(set(bms_params_list)) == 1 or (list(set(bms_params_list))[0] == mocked_value):
            return False
        return True
    
    def __check_mocked_int_float(self, bms_params, BMS_PARAMS_THRESHOLD):
        for key in bms_params.keys():
            if self.__check_mocked_int_float_value(bms_params[key], BMS_PARAMS_THRESHOLD, key):#len(set(bms_params[key])) != 1:
                return False
        return True
    
    def __check_length(self, bms_params, BMS_PARAMS_THRESHOLD):
        for key in bms_params.keys():
            if len(bms_params[key]) != BMS_PARAMS_THRESHOLD["test_params"][key]["count"]:
                return False
        return True
        
    def __check_length_mocked_int_float(self, bms_params, BMS_PARAMS_THRESHOLD):
        if self.__check_length(bms_params, BMS_PARAMS_THRESHOLD):
            if self.__check_mocked_int_float(bms_params, BMS_PARAMS_THRESHOLD):
                return True
        return False
    
    def __validate_mocked_data(self, simulated_battery_params, BMS_PARAMS_THRESHOLD):
        validation = False
        if self.__check_for_child_keys(simulated_battery_params):
            if self.__check_length_mocked_int_float(simulated_battery_params, BMS_PARAMS_THRESHOLD):
                validation = True
        return validation
    
    def test_get_battery_params(self):
        """ this test case is to test send_to_console method """
        with patch('random.randint') as mock_randint,\
             patch('random.uniform') as mock_uniform:
            mock_randint.return_value = BMS_PARAMS_THRESHOLD["mocked"]["int"]
            mock_uniform.return_value = BMS_PARAMS_THRESHOLD["mocked"]["float"]
            from bms_code.bms_sensor_simulator import SimulateBatteryParamsClass
            SimulateBatteryParamsClassObject = SimulateBatteryParamsClass(BMS_PARAMS_THRESHOLD["test_params"])
            simulated_battery_params = SimulateBatteryParamsClassObject.get_battery_params()
            self.assertTrue(self.__validate_mocked_data(simulated_battery_params, BMS_PARAMS_THRESHOLD))
       