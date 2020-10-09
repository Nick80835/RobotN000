import sys
from logging import INFO, basicConfig

import telethon as tt
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
from telethon.network.connection.tcpabridged import \
    ConnectionTcpAbridged as CTA

from .event_handler import EventHandler
from .settings import Settings

if sys.version_info.major < 3 or (sys.version_info.major == 3 and sys.version_info.minor < 6):
    print("This program requires at least Python 3.6.0 to work correctly, exiting.")
    sys.exit(1)

basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=INFO)


class Robot():
    client = None
    settings = Settings()

    def __init__(self):
        self.start_client()
        self.event_handler = EventHandler(self.client)

    def run_until_done(self):
        self.client.run_until_disconnected()

    def _check_config(self):
        session_name = self.settings.get_config("session_name")
        api_key = self.settings.get_config("api_key")
        api_hash = self.settings.get_config("api_hash")

        while not api_key:
            api_key = input("Enter your API key: ")

        self.settings.set_config("api_key", api_key)

        while not api_hash:
            api_hash = input("Enter your API hash: ")

        self.settings.set_config("api_hash", api_hash)

        if not session_name:
            session_name = "user0"
            self.settings.set_config("session_name", session_name)

        return api_key, api_hash, session_name

    def start_client(self):
        api_key, api_hash, session_name = self._check_config()
        self.client = tt.TelegramClient(session_name, api_key, api_hash, connection=CTA)
        self.client.start()


robot_n000 = Robot()
robot_n000.run_until_done()
