""" This file simulates battery parameters and sends to console in a predefined format """
# user defined modules
from bms_sensor_simulator import BMS_PARAMS_THRESHOLD, SimulateBatteryParamsClass
from bms_params_json_formatter import format_to_json_string

def bms_generate_format_send():
    """ this function will simulate, format and sends bms parameters to console """
    # simulate parameters
    simulate_battery_params_object = SimulateBatteryParamsClass(BMS_PARAMS_THRESHOLD)
    # format the parameters to JSON
    format_to_json_string(simulate_battery_params_object)
    # send the data to receiver
    return
