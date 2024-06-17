from lumibot.brokers import Alpaca
from lumibot.backtesting import YahooDataBacktesting
from lumibot.strategies.strategy import Strategy
from lumibot.traders import Trader
from datetime import datetime

API_KEY = "AKI9454DSDB6V5MQAS7W"
API_SECRET = "QtdU7TcEpih2jST6SQ6zxWhQ0JKxacGxFSGRXZLg"
BASE_URL = "https://api.alpaca.markets"

ALPACA_CREDS = {
    "API_KEY":API_KEY,
    "API_SECRET": API_SECRET,
    "PAPER": True
}
\
class MLTrader(Strategy):
    def initialize(self):
        pass
    def on_trading_iteration(self):
        pass

start_date = datetime(2023,12,15)
end_date = datetime(2023,12,31)

end_date

broker = Alpaca(ALPACA_CREDS)
strategy = MLTrader(name='mlstrat', broker = broker, parameters={})
strategy.backtest(
    YahooDataBacktesting,
    start_date,
    end_date,
    parameters={}
)