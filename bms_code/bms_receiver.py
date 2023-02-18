import json
from bms_code.bms_receiver_statistics import BatteryParameterStatistics

def get_battery_params():
    return ['soc','dod','temp','tv']

def get_statistics(battery_params_json_string):
    battery_params = get_battery_params()
    battery_param_readings = json.loads(battery_params_json_string)
    battery_param_readings = battery_param_readings['batt_params']
    battery_params_stats_result = {}
    for param in battery_params:
        batteryParamStats = BatteryParameterStatistics();
        battery_params_stats_result[param] = batteryParamStats.compute_statistics_for_battery_param(battery_param_readings[param])
    return battery_params_stats_result

def get_statistics_in_json(battery_params_json_string):
    statistics_json = {}
    statistics_json['statistics'] = get_statistics(battery_params_json_string)
    return json.dumps(statistics_json)

def print_statistics(battery_params_json_string):
    print(get_statistics_in_json(battery_params_json_string))

def read_sender_input():
    return input()

if __name__ == '__main__':
    print_statistics(read_sender_input())