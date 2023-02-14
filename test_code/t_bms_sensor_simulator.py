import unittest
from unittest.mock import patch

class TestBmsSenderClass(unittest.TestCase):
    """ this class contains methods to test methods in bms_sender """
    def __check_for_child_keys(self, bms_params):
        if set(["soc", "dod", "tem[", "tv"]) > set(bms_params.keys()):
            return False
        return True    
    
    def __check_mocked_random_int_float(self, bms_params):
        for key in bms_params.keys():
            if len(set(bms_params[key])) != 1:
                return False
        return True
    
    def __check_length(self, bms_params, BMS_PARAMS_THRESHOLD):
        for key in bms_params.keys():
            if len(bms_params[key]) != BMS_PARAMS_THRESHOLD[key]["count"]:
                return False
        return True
        
    def __check_length_mocked_int_float(self, bms_params, BMS_PARAMS_THRESHOLD):
        if self.__check_length(bms_params, BMS_PARAMS_THRESHOLD):
            if self.__check_mocked_random_int_float(bms_params):
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
            mocked_int = 5
            mocked_float = 5.0
            mock_randint.return_value = mocked_int=5
            mock_uniform.return_value = 5.0
            from bms_code.bms_sensor_simulator import BMS_PARAMS_THRESHOLD, \
                SimulateBatteryParamsClass
            SimulateBatteryParamsClassObject = SimulateBatteryParamsClass(BMS_PARAMS_THRESHOLD)
            simulated_battery_params = SimulateBatteryParamsClassObject.get_battery_params()
            self.assertTrue(self.__validate_mocked_data(simulated_battery_params, BMS_PARAMS_THRESHOLD))
       