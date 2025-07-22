from config import Config

class TradeManager:
    def __init__(self):
        self.strategy = Config.STRATEGY
        self.risk = Config.RISK_PER_TRADE

    def evaluate(self, chart_data):
        if self.strategy == "ES_SCALPER":
            return self._es_scalper_rules(chart_data)
        else:
            return self._swing_rules(chart_data)

    def _es_scalper_rules(self, data):
        entry = data['levels']['pivot']
        stop = entry * (1 - 0.005)  # 0.5% stop
        target = entry * (1 + 0.01)  # 1% target
        return {
            'entry': round(entry, 2),
            'stop': round(stop, 2),
            'target': round(target, 2),
            'rr_ratio': 2.0
        }
