import Queue
import threading
import time

from execution import Execution
from settings import STREAM_DOMAIN, API_DOMAIN, ACCESS_TOKEN, ACCOUNT_ID
from strategy import TestRandomStrategy
from streaming import StreamingForexPrices
from portfolio import Portfolio

def trade(events, strategy, portfolio, execution):
    """
    Carries out an infinite while loop that polls the events queue and directs each event to
    either the strategy component of the execution handler. The loop will then pause for
    'heartbeat' seconds and continue.
    """
    while True:
        try:
            event = events.get(False)
        except Queue.Empty:
            pass
        else:
            if event is not None:
                if event.type == 'TICK':
                    strategy.calculate_signals(event)
                elif event.type == 'SIGNAL':
                    portfolio.execute_signal(event)
                elif event.type == 'ORDER':
                    print "Executing order!"
                    execution.execute_order(event)
        time.sleep(heartbeat)

if __name__ == "__main__":
    heartbeat = 0.5
    events = Queue.Queue()

    # Define trade parameters
    instrument = "EUR_USD"
    units = 2000

    # Create OANDA market price streaming
    prices = StreamingForexPrices(STREAM_DOMAIN, ACCESS_TOKEN, ACCOUNT_ID, instrument, events)

    # Create the execution handler
    execution = Execution(API_DOMAIN, ACCESS_TOKEN, ACCOUNT_ID)

    # Create the strategy (signal) generator
    strategy = TestRandomStrategy(instrument, events)

    # Create Portfolio
    portfolio = Portfolio(prices, events, equity = 2000.00)

    # Create two separate threads -> one for trading, and the other one for price streaming
    trade_thread = threading.Thread(target = trade, args = (events, strategy, portfolio, execution))
    price_thread = threading.Thread(target = prices.stream_to_queue, args = [])

    # Start threads
    trade_thread.start()
    price_thread.start()
