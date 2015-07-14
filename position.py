class Position(object):
    def __init__(self, side, market, units, exposure, avg_price, current_price):
        self.side = side
        self.market = market
        self.units = units
        self.exposure = exposure
        self.avg_price = avg_price
        self.current_price = current_price
        self.profit_base = self.calculate_profit_base()
        self.profit_percentage = self.calculate_profit_percentage()

    def calculate_pips(self):
        multiplier = 1.0
        if self.side == "SHORT":
            multiplier = -1.0
        return multiplier * (self.current_price - self.avg_price)

    def calculate_profit_base(self):
        pips = self.calculate_pips()
        return pips * self.exposure / self.current_price

    def calculate_profit_percentage(self):
        return (self.profit_base / self.exposure) * 100.0

    def update_position_price(self, current_price):
        self.current_price = current_price
        self.profit_base = self.calculate_profit_base()
        self.profit_percentage = self.calculate_profit_percentage()

