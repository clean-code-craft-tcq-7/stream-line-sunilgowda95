class BatteryParameterStatistics(object):
    def __init__(self):
        self.statistics = {
            'maxVal': None,
            'minVal': None,
            'SMAVal': None
        }
        self.sma_period = 5;
        
    def compute_statistics_for_battery_param(self, param_readings):
        self.statistics['maxVal'] = round(max(param_readings),2);
        self.statistics['minVal'] = round(min(param_readings),2);
        self.statistics['SMAVal'] = round(sum(param_readings[-self.sma_period:])/self.sma_period,2);
        return self.statistics

        
