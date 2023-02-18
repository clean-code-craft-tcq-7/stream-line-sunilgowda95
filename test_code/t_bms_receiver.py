import unittest
import json
from unittest.mock import patch
from bms_code.bms_receiver import get_statistics_in_json,get_battery_params

class TestBMSReceiver(unittest.TestCase):   
    
    def test_bms_receiver_output(self):
        battery_params = get_battery_params()
        battery_params_json_string = '''{
            "batt_params": {
                "soc": [40,30,29,46,10,9,15,5,20,22],
                "dod": [60,70,71,72,22,16,1,21,59,75,95],
                "temp": [38.03,25.1,30.68,27.59,34.16,27.74,32.07,34.38,25.47,28],
                "tv": [10.08,10.35,11.27,10.85,10.14,11.75,12.21,11,11.29,11.19]
            }
        }'''
        expected_result = {
            "soc": {"maxVal": 46, "minVal": 5, "SMAVal": 14.2},
            "dod": {"maxVal": 95, "minVal": 1, "SMAVal": 50.2},
            "temp": {"maxVal": 38.03, "minVal": 25.10, "SMAVal": 29.53},
            "tv": {"maxVal": 12.21, "minVal": 10.08, "SMAVal": 11.49}
        }
        actual_result = get_statistics_in_json(battery_params_json_string)
        actual_result = json.loads(actual_result)
        actual_result = actual_result['statistics']
        
        # checking all battery parameters present in result
        assert(all(param in actual_result for param in battery_params));

        # checking statistics with expected value
        for battery_param in expected_result:
            assert(expected_result[battery_param] == actual_result[battery_param])

