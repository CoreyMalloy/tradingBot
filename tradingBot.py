from lumibot.brokers import Alpaca
from lumibot.backtesting import YahooDataBacktesting
from lumibot.strategies.strategy import Strategy
from lumibot.traders import Trader
from datetime import datetime

API_KEY = "PKFUMQIUP2KFEBUS96MY"
API_SECRET = "IrJ1is8wfG3kNirfvj7YYTR5Gm6NG6KAsFLODTxs"
BASE_URL = "https://paper-api.alpaca.markets/v2"

ALPACA_CREDS = {
    "API_KEY":API_KEY,
    "API_SECRET": API_SECRET,
    "PAPER": True
}

class MLTrader(Strategy):
    def initialize(self, symbol:str="SPY"):
        self.symbol = symbol
        # how frequently we will trade
        self.sleeptime = "24H"
        self.last_trade = None

    def on_trading_iteration(self):
        if self.last_trade == None:
            order = self.create_order(
                self.symbol,
                10,
                "buy",
                type="market"
            )
            self.submit_order(order)
            self.last_trade = "buy"

start_date = datetime(2024,6,17)
end_date = datetime(2024,6,30)

broker = Alpaca(ALPACA_CREDS)
strategy = MLTrader(name='mlstrat', broker = broker, parameters={"symbol":"SPY"})
strategy.backtest(
    YahooDataBacktesting,
    start_date,
    end_date,
    parameters={"symbol":"SPY"}
)