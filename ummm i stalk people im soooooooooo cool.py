import requests
import time

key = ""
steamid = "76561198877328989"

endpoint = f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={key}&steamids={steamid}"
u_player = {}

while True:
	r = requests.get(endpoint)
	d = r.json()

	response = d["response"]
	players = response["players"]
	player = players[0]

	for key, v in player.items():
		if u_player.get(key) != v:
			u_player[key] = v

			print(time.strftime(f"%H:%M:%S: {key} = {v}", time.localtime()))

	time.sleep(60)

