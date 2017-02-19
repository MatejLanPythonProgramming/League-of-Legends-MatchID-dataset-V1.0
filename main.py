import requests
from files import create_files, file_set, set_file
from time import sleep

summoner_name = 
server = 
key = 
base_url = "https://{}.api.pvp.net/api/lol/{}".format(server, server)


# gets summoner ID from name
def summoner_ID(name):
    url = base_url + "/v1.4/summoner/by-name/" + name + "?api_key=" + key
    page = requests.get(url).json()
    ID = page[name.lower()]["id"]
    return ID


# gets all match ID from summoner ID
def matches(summoner_ID):
    url = base_url + "/v2.2/matchlist/by-summoner/" + str(summoner_ID) + "?api_key=" + key
    page = requests.get(url).json()
    page = page["matches"]
    for i in page:
        if i["season"] == "PRESEASON2017" and i["matchId"] not in match_IDs:
            queue.add(i["matchId"])


# dobi name oz. id-je vseh summonerjev iz matcha
def get_IDs(matchId):
    url = base_url + "/v2.2/match/" + str(matchId) + "?api_key=" + key
    page = requests.get(url).json()
    page = page["participantIdentities"]
    for i in page:
        player_IDs.add(i["player"]["summonerId"])

create_files()
queue = file_set("IDs/queue.txt")
match_IDs = file_set("IDs/matchIDs.txt")
player_IDs = file_set("IDs/playerIDs.txt")
if len(queue) == 0:
    ID = summoner_ID(summoner_name)
    matches(ID)


# gre skoz ceu queue, dobiva id-je od playerjev in doda match idje v matchIDs
counter = 0
temp_queue = set(queue)
for i in temp_queue:
    try:
        sleep(0.4)
        get_IDs(i)
        queue.remove(i)
        match_IDs.add(i)
        counter += 1
        if counter % 30 == 0:
            set_file(queue, "IDs/queue.txt")
            set_file(match_IDs, "IDs/matchIDs.txt")
            set_file(player_IDs, "IDs/playerIDs.txt")
        print("Queue: " + str(len(queue)) + "   Match: " + str(len(match_IDs)) + "   Player: " + str(len(player_IDs)))
    except:
        print(i)


# gre skoz vse playerje in dobi iz njih matche --> queue
counter = 0
temp_player = set(player_IDs)
for i in temp_player:
    try:
        sleep(0.4)
        matches(i)
        counter += 1
        if counter % 30 == 0:
            set_file(queue, "IDs/queue.txt")
        print("Queue: " + str(len(queue)) + "   Match: " + str(len(match_IDs)) + "   Player: " + str(len(player_IDs)))
    except:
        print(i)
