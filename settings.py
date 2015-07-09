import os

ENVIRONMENTS = {
    "streaming": {
        "practice": "stream-fxtrade.oanda.com",
        "sandbox": "stream-sandbox.oanda.com"
        },
    "api": {
        "practice": "api-fxpractice.oanda.com",
        "sandbox": "api-sandbox.oanda.com"
        }
}

DOMAIN = "practice"
STREAM_DOMAIN = ENVIRONMENTS["streaming"][DOMAIN]
API_DOMAIN = ENVIRONMENTS["api"][DOMAIN]
ACCESS_TOKEN = os.environ.get('OANDA_API_ACCESS_TOKEN', None)
ACCOUNT_ID = os.environ.get('OANDA_API_ACCOUNT_ID', None)
