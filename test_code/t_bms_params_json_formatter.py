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
    
    def __check_output_parent_keys(self):
        if set(self.OUTPUT_KEYS) <= set(self.output_json.keys()):
            return False
        return True

    def __check_output_batt_params_keys(self):
        if set(self.INPUT_KEYS) <= set(self.output_json["batt_params"].keys()):
            return True
        return False
    
    def __check_output_batt_params_key_values(self, input):
        for key, value in self.output_json["batt_params"].items():
            if input[key] != value:
                return False
        return True
    
    def test_json_formatter_case0(self):
        input = {}
        FormatBatteryParamsObject = FormatBatteryParamsClass(input)
        self.output_json = json.loads(FormatBatteryParamsObject.format_to_json_string())
        self.assertTrue(self.__check_output_parent_keys())
        self.assertEqual(self.output_json["msg"], "failed")
        self.assertEqual(self.output_json["batt_params"], {})
        
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
            FormatBatteryParamsObject = FormatBatteryParamsClass(input)
            self.output_json = json.loads(FormatBatteryParamsObject.format_to_json_string())
            self.assertTrue(self.__check_output_parent_keys())
            self.assertEqual(self.output_json["msg"], "failed")
            self.assertEqual(self.output_json["batt_params"], {})
            
    def test_json_formatter_case1(self):
        input = {"soc":[1,2,3], "dod":[1,2,3], "temp":[1,2,3], "tv":[1,2,3]}
        FormatBatteryParamsObject = FormatBatteryParamsClass(input)
        self.output_json = json.loads(FormatBatteryParamsObject.format_to_json_string())
        self.assertTrue(self.__check_output_parent_keys())
        self.assertEqual(self.output_json["msg"], "success")
        self.assertTrue(self.__check_output_batt_params_keys())
        self.assertTrue(self.__check_output_batt_params_key_values(input))
        