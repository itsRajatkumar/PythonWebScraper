import requests
import json
import csv

def configure_api():
    url = "https://footballapi.pulselive.com/football/players"

    headers = {
        "content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "DNT": "1",
        "Origin": "https://www.premierleague.com",
        "Referer": "https://www.premierleague.com/players",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }

    queryParams = {
        "pageSize": 32,
        "compSeasons": 274,
        "altIds": True,
        "page": 0,
        "type": "player",
        "id": -1,
        "compSeasonId": 274
    }
    return url, headers, queryParams

def Scraper(url , headers , queryParams):
    response = requests.get(url = url, headers = headers, params = queryParams)
    if response.status_code == 200:
        # load the json data
        data = json.loads(response.text)
        # print the required data
        for player in data["content"]:
            obj =({
                "name": player["name"]["display"],
                "nationalTeam": player["nationalTeam"]["country"],
                "position": player["info"]["positionInfo"]
            })
            list.append(obj)

keys = list[0].keys()
with open('list.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(list)