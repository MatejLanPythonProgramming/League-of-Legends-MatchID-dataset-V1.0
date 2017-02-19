import os

def create_files():
    queue = "IDs/queue.txt"
    match_IDs = "IDs/matchIDs.txt"
    player_IDs = "IDs/playerIDs.txt"
    if not os.path.exists("IDs"):
        os.makedirs("IDs")
    if not os.path.isfile(queue):
        with open(queue, "w") as f:
            f.write("")
    if not os.path.isfile(match_IDs):
        with open(match_IDs, "w") as f:
            f.write("")
    if not os.path.isfile(player_IDs):
        with open(player_IDs, "w") as f:
            f.write("")


def write_file(file, data):
    with open(file, "a") as file:
        file.write(str(data) + "\n")


def file_set(file):
    results = set()
    with open(file, "rt") as f:
        for line in f:
            results.add(line.replace("\n", ""))
    return results


def set_file(data, file):
    with open(file, "w") as f:
        pass
    for matchID in data:
        write_file(file, matchID)
