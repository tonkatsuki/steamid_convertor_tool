import os
from steamid_to_commid import steamid_to_commid
from search import find_steam_ids


def main(filename):
    # check if the file exists
    if os.path.exists(filename):
        # the file exists then read the file
        with open(filename, "r") as f:
            lines = f.readlines()

        new_lines = []

        for line in lines:
            # if an id exists, then pass def steamid_to_commid
            found_ids = find_steam_ids(line)
            if found_ids:
                steam_id = found_ids[0]
                comm_id = steamid_to_commid(steam_id)
                # replace the steam id to the command id
                new_line = line.replace(steam_id, str(comm_id))
                new_lines.append(new_line)
            else:
                new_lines.append(line)
# create a new file
        with open("new.cfg", "w") as new_file:
            new_file.writelines(new_lines)

        print("Done")
    else:
        print('The file does not exist.')


if __name__ == "__main__":
    main("old.cfg")
