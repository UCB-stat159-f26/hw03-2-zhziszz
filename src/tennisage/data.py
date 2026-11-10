import json

import pandas as pd


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
