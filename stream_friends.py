from ast import literal_eval
from configparser import ConfigParser
import logging
import requests

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

logging.debug("Parsing config file")
cfg = ConfigParser()
cfg.read("settings.cfg")

lol_server = cfg.get("main", "LOL_SERVER", fallback="na1")
logger.debug("League of Legends Server: {}".format(lol_server))
lol_base_api_url = "https://{server}.api.riotgames.com/lol/".format(server=lol_server)
logger.debug("API Base URL: {}".format(lol_base_api_url))

start_streaming_shortcut = cfg.get("main", "START_STREAMING_SHORTCUT", fallback=None)
logger.debug("Start streaming Shortcut: {}".format(start_streaming_shortcut))
stop_streaming_shortcut = cfg.get("main", "STOP_STREAMING_SHORTCUT", fallback=None)
logger.debug("Stop streaming Shortcut: {}".format(stop_streaming_shortcut))

lol_api_key = cfg.get("main", "LOL_API_KEY")
logger.debug("Using LOL API Key: {}".format(lol_api_key))

summoners = literal_eval(cfg.get("main", "SUMMONERS"))
assert isinstance(summoners, list)
assert all(isinstance(summoner, str) for summoner in summoners)
logger.debug("Summoners: {}".format(" ".join(summoners)))


# https://developer.riotgames.com/getting-started.html
# https://developer.riotgames.com/spectating-games.html

def request():
    r = requests.get("https://na1.api.riotgames.com/lol/")