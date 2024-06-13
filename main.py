import pyRofex
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    auth_user: str
    auth_password: str
    auth_account: str

    model_config = SettingsConfigDict(env_file=".env")


class Client:
    def __init__(self):
        # Initiate Websocket Connection
        pyRofex.init_websocket_connection(
            market_data_handler=self._market_data_handler,
            order_report_handler=self._order_report_handler,
            error_handler=self._error_handler,
            exception_handler=self._exception_handler,
        )

    def subscribe(self, instruments, entries):
        # Subscribes to receive market data messages **
        pyRofex.market_data_subscription(tickers=instruments, entries=entries)

        # Subscribes to receive order report messages (default account will be used) **
        pyRofex.order_report_subscription()

    def _market_data_handler(self, message):
        print(f"Market Data Message Received: {message}")

    def _order_report_handler(self, message):
        print(f"Order Report Message Received: {message}")

    def _error_handler(self, message):
        print(f"Error Message Received: {message}")

    def _exception_handler(self, e):
        print(f"Exception Occurred: {e.message}")


def main():
    settings = Settings()

    # Set the environment
    pyRofex.initialize(
        user=settings.auth_user,
        password=settings.auth_password,
        account=settings.auth_account,
        environment=pyRofex.Environment.REMARKET,
    )

    client = Client()

    # Instruments list to subscribe
    instruments = ["YPFD/JUN24", "GGAL/JUN24"]

    # Uses the MarketDataEntry enum to define the entries we want to subscribe to
    entries = [
        pyRofex.MarketDataEntry.BIDS,
        pyRofex.MarketDataEntry.OFFERS,
    ]

    client.subscribe(instruments, entries)


if __name__ == "__main__":
    main()
