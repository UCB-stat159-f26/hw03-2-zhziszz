import json
import re
from urllib.request import Request, urlopen

import pandas as pd


BASE_URL = "https://www.tennisabstract.com"

# items I need from each row (0-based) and their names, same as hw2.
# item 16 is the opponent's birthday for women and the opponent's age for men
COLUMNS = {0: "date", 1: "tournament", 2: "surface", 4: "result", 8: "round",
           9: "score", 11: "opponent", 16: "opponent_info"}


def _parse_career_js(text):
    # cut off "var morematchmx =" and the ";" at the end
    rows = json.loads(text[text.index("["):].rstrip().rstrip(";"))
    raw = pd.DataFrame(rows).iloc[:, list(COLUMNS)]
    raw.columns = list(COLUMNS.values())
    return raw


def _url_name(player):
    # "serena williams", "Serena Williams", "SerenaWilliams" -> "SerenaWilliams"
    return "".join(word[0].upper() + word[1:] for word in player.split())


def _download(url):
    # the site returns 403 without a browser User-Agent
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(req) as resp:
        return resp.read().decode()


def _player_info(name):
    # name and birthday are on the player page, not in the career file
    page = _download(f"{BASE_URL}/cgi-bin/player.cgi?p={name}")
    fullname = re.search(r"var fullname = '(.*)';", page).group(1)
    dob = re.search(r"var dob = (\d+);", page).group(1)
    return fullname, pd.to_datetime(dob, format="%Y%m%d")
