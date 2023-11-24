# /bin/python3

# 1. Get current steamid from file as loop
# 2. Store as variable, webAPI lookup for new variable
# 3. Replace variable
#
#
# python3 main.py admins.cfg
# it will export admins_new.cfg
#

# Global vars
steamid64ident = 76561197960265728


def steamid_to_commid(steamid):
    sid_split = steamid.split(":")
    commid = int(sid_split[2]) * 2

    if sid_split[1] == "1":
        commid += 1

    commid += steamid64ident
    return commid


print(steamid_to_commid("STEAM_0:1:1934414"))
