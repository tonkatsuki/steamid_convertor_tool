import re


# define an id pattern
def find_steam_ids(text, pattern=r"STEAM_[0-9]:[0-9]:[0-9]+"):
    return re.findall(pattern, text)
