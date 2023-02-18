import unittest

class TestBMSReceiverStatistics(unittest.TestCase):   
    
    def test_bms_receiver_statistics_for_single_param(self):
        battery_param_name = 'soc'
        battery_param_readings = [1,2,3,4,9,8,7,6,5,4]
        expected_result = {'maxVal':9, 'minVal':1, 'SMAVal':6}

        from bms_code.bms_receiver_statistics import BatteryParameterStatistics
        batteryParamStats = BatteryParameterStatistics();

        #checking single battery statistics
        actual_result = batteryParamStats.compute_statistics_for_battery_param(battery_param_readings);
        assert(actual_result == expected_result)