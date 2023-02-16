import unittest
from unittest.mock import patch
import copy
"""
Input : dictionary containing parent keys "soc", "dod", "temp" and "tv" 
    with each parent key containing "max", "min", "count", "type"
Output : dictionary containing "soc", "dod", "temp", "tv" keys
    with list of random values equal to count defined in Input.
Test Cases : 
    1.  Input dictionary with valid parameters, also mock random module with 
            fixed values.
        Output: check for all the keys, length of output list, check value
            of the list using mocked values.
    2.  Input dictionary with valid parameters.
        Output: check for all the keys, length of output list, check value
            of the list are in the given range.
    3.  Input dictionary with all parameters as 0
        Output: check for all the keys, length of output list, check value
            of the list are in the given range.
"""

class TestSimulateBatteryParamsClass(unittest.TestCase):
    """ this class contains methods to test methods in bms_sender """
    def __check_for_child_keys(self, bms_params):
        if set(["soc", "dod", "temp", "tv"]) > set(bms_params.keys()):
            return False
        return True    
    
    def __is_value_out_of_boundary(self, value, thresholds_dictionary):
        if value > thresholds_dictionary["max"] or value < thresholds_dictionary["min"]:
            return True # out of bound values
        return False
    
    def __is_int_float_values_out_of_boundary(self, values_list, thresholds_dictionary):
        for each in values_list:
            if self.__is_value_out_of_boundary(each, thresholds_dictionary):
                return True # out of bound values
        return False # no out of bound values
    
    def __check_int_float_boundaries(self, bms_params, BMS_PARAMS_THRESHOLD):
        for key in bms_params.keys():
            if self.__is_int_float_values_out_of_boundary(bms_params[key], BMS_PARAMS_THRESHOLD["test_params"][key]):
                return False
        return True
    
    def __check_mocked_int_float_value(self, bms_params_list, BMS_PARAMS_THRESHOLD, key):
        mocked_value = BMS_PARAMS_THRESHOLD["mocked"][BMS_PARAMS_THRESHOLD["test_params"][key]["type"]]
        if len(set(bms_params_list)) == 1 or (list(set(bms_params_list))[0] == mocked_value):
            return False
        return True
    
    def __check_mocked_int_float(self, bms_params, BMS_PARAMS_THRESHOLD):
        for key in bms_params.keys():
            if self.__check_mocked_int_float_value(bms_params[key], BMS_PARAMS_THRESHOLD, key):
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

    def __check_length_int_float(self, bms_params, BMS_PARAMS_THRESHOLD):
        if self.__check_length(bms_params, BMS_PARAMS_THRESHOLD):
            if self.__check_int_float_boundaries(bms_params, BMS_PARAMS_THRESHOLD):
                return True
        return False
    
    def __validate_mocked_data(self, simulated_battery_params, BMS_PARAMS_THRESHOLD):
        validation = False
        if self.__check_for_child_keys(simulated_battery_params):
            if self.__check_length_mocked_int_float(simulated_battery_params, BMS_PARAMS_THRESHOLD):
                validation = True
        return validation
    
    def __validate_data(self, simulated_battery_params, BMS_PARAMS_THRESHOLD):
        validation = False
        if self.__check_for_child_keys(simulated_battery_params):
            if self.__check_length_int_float(simulated_battery_params, BMS_PARAMS_THRESHOLD):
                validation = True
        return validation
    
    def __init_get_simulator_data(self, BMS_PARAMS_THRESHOLD):    
        from bms_code.bms_sensor_simulator import SimulateBatteryParamsClass
        test_input = copy.deepcopy(BMS_PARAMS_THRESHOLD["test_params"])
        del(test_input["dod"])
        SimulateBatteryParamsClassObject = SimulateBatteryParamsClass(test_input)
        return SimulateBatteryParamsClassObject.get_battery_params()
                    
    
    def test_get_battery_params_1(self):
        BMS_PARAMS_THRESHOLD = {
            "test_params" : {
                "soc":{"max":90, "min":10, "count":40, "type":"int"},
                "dod":{"max":90, "min":10, "count":40, "type":"int"},
                "temp":{"max":38, "min":20, "count":30, "type":"float"},
                "tv":{"max":12.2, "min":10.5, "count":30, "type":"float"},
            },
            "mocked" : {"int": 5, "float":5.0}
        }        
        """ this test case is to test send_to_console method """
        with patch('random.randint') as mock_randint,\
             patch('random.uniform') as mock_uniform:
            mock_randint.return_value = BMS_PARAMS_THRESHOLD["mocked"]["int"]
            mock_uniform.return_value = BMS_PARAMS_THRESHOLD["mocked"]["float"]
            simulated_battery_params = self.__init_get_simulator_data(BMS_PARAMS_THRESHOLD)
            self.assertTrue(self.__validate_mocked_data(simulated_battery_params, BMS_PARAMS_THRESHOLD))

    def test_get_battery_params_2_3(self):
        input_2_3 = [
            {
            "test_params" : {
                "soc":{"max":50, "min":10, "count":10, "type":"int"},
                "dod":{"max":50, "min":10, "count":10, "type":"int"},
                "temp":{"max":50, "min":0, "count":5, "type":"float"},
                "tv":{"max":12, "min":0, "count":3, "type":"float"},
            }
        },
        {
            "test_params" : {
                "soc":{"max":0, "min":0, "count":0, "type":"int"},
                "dod":{"max":0, "min":0, "count":0, "type":"int"},
                "temp":{"max":0, "min":0, "count":0, "type":"float"},
                "tv":{"max":0, "min":0, "count":0, "type":"float"},
            }
        }]
        for BMS_PARAMS_THRESHOLD in input_2_3:
            """ this test case is to test send_to_console method """
            simulated_battery_params = self.__init_get_simulator_data(BMS_PARAMS_THRESHOLD)
            self.assertTrue(self.__validate_data(simulated_battery_params, BMS_PARAMS_THRESHOLD))
       