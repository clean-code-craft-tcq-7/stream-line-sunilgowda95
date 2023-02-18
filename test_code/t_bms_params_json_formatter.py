""" This file consists of test methods to test bms_params_json_formatter """
import unittest
from unittest.mock import patch
import json
from bms_code.bms_params_json_formatter import FormatBatteryParamsClass

"""
Input : dictionary containing keys "soc", "dod", "temp" and "tv"
Output : JSON string with keys "batt_params", "ts" and "message"
            "batt_params" --> "soc", "dod", "temp" and "tv"
Test Cases : 
    1.  Input empty dictionary.
        Output check for "msg" : "failed"
            with "batt_params" : {}
    2.  Input missing one of the keys.
        Output check for "msg" : "failed"
            with "batt_params" : {}
    3.  Input with all the keys.
        Output check for "msg" : "success"
            with "batt_params" : containing all the keys
"""

class TestFormatBatteryParamsClass(unittest.TestCase):
    """ This class is to test methods in bms_params_json_formatter """
    INPUT_KEYS = ["soc", "dod", "temp", "tv"]
    OUTPUT_KEYS = ["batt_params", "ts", "message"]
    
    def __check_output_parent_keys(self, output_json):
        if set(self.OUTPUT_KEYS) <= set(output_json.keys()):
            return False
        return True

    def __check_output_batt_params_keys(self, output_json):
        if set(self.INPUT_KEYS) <= set(output_json["batt_params"].keys()):
            return True
        return False
    
    def __check_output_batt_params_key_values(self, input, output_json):
        for key, value in output_json["batt_params"].items():
            if input[key] != value:
                return False
        return True
    
    def test_json_formatter_case0(self):
        input0 = {}
        FormatBatteryParamsObject0 = FormatBatteryParamsClass(input0)
        output_json0 = json.loads(FormatBatteryParamsObject0.format_to_json_string())
        self.assertTrue(self.__check_output_parent_keys(output_json0))
        self.assertEqual(output_json0["msg"], "failed")
        self.assertEqual(output_json0["batt_params"], {})
        
    def test_json_formatter_case1(self):
        input_list = [
            {"dod":[], "temp":[], "tv":[]},
            {"temp":[], "tv":[]},
            {"tv":[]},
            {"soc":[], "dod":[], "temp":[]},
            {"soc":[], "dod":[]},
            {"soc":[]},
        ]
        for input in input_list:
            FormatBatteryParamsObject1 = FormatBatteryParamsClass(input)
            output_json1 = json.loads(FormatBatteryParamsObject1.format_to_json_string())
            self.assertTrue(self.__check_output_parent_keys(output_json1))
            self.assertEqual(output_json1["msg"], "failed")
            self.assertEqual(output_json1["batt_params"], {})
            
    def test_json_formatter_case2(self):
        input2 = {"soc":[1,2,3], "dod":[1,2,3], "temp":[1,2,3], "tv":[1,2,3]}
        FormatBatteryParamsObject2 = FormatBatteryParamsClass(input2)
        output_json2 = json.loads(FormatBatteryParamsObject2.format_to_json_string())
        self.assertTrue(self.__check_output_parent_keys(output_json2))
        self.assertEqual(output_json2["msg"], "success")
        self.assertTrue(self.__check_output_batt_params_keys(output_json2))
        self.assertTrue(self.__check_output_batt_params_key_values(input2, output_json2))
        