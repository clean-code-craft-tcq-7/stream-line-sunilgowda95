""" This file simulates battery parameters and sends to console in a predefined format """
# user defined modules
import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from bms_code.bms_sensor_simulator import BMS_PARAMS_THRESHOLD, SimulateBatteryParamsClass
from bms_code.bms_params_json_formatter import FormatBatteryParamsClass

def send_to_console(json_string):
    print(json_string)

def bms_generate_format_send():
    """ this function will simulate, format and sends bms parameters to console """
    # simulate parameters
    simulate_battery_params_object = SimulateBatteryParamsClass(BMS_PARAMS_THRESHOLD)
    simulated_battery_params = simulate_battery_params_object.get_battery_params()
    # format the parameters to JSON
    fomatted_battery_params_to_json_object = FormatBatteryParamsClass(simulated_battery_params)
    fomatted_battery_params_to_json_string = fomatted_battery_params_to_json_object.format_to_json_string()
    # send the data to receiver
    send_to_console(fomatted_battery_params_to_json_string)
    return

if __name__ == '__main__':
    bms_generate_format_send()