from dotenv import load_dotenv
import requests
import os

load_dotenv()

YOUR_API_KEY = os.getenv("YOUR_API_KEY")

API_endpoint = "https://api-v3.igdb.com/"
API_command = "genres"
API_params = {
        'headers': {'user-key': YOUR_API_KEY},
        'data': """
            fields name;
        """
    }

def get_all_genres():
    genre_list = []
    for i in range(37):
        API_params["data"] = f"""
            fields name;
            where id = {i};
        """
        API_url = API_endpoint + API_command
        r = requests.post(API_url, **API_params)
        data = r.json()
        if data.copy() == [].copy():
            continue
        genre_list.append(data[0]["name"])
    return genre_list

ALL_GENRES = [
    'Point-and-click', 'Fighting', 'Shooter', 'Music', 
    'Platform', 'Puzzle', 'Racing', 'Real Time Strategy (RTS)', 
    'Role-playing (RPG)', 'Simulator', 'Sport', 'Strategy', 
    'Turn-based strategy (TBS)', 'Tactical', "Hack and slash/Beat 'em up", 
    'Quiz/Trivia', 'Pinball', 'Adventure', 'Indie', 'Arcade', 
    'Visual Novel', 'Card & Board Game', 'MOBA'
]

# def get_all_genres():
#     genre_list = []
#     for i in range(37):
#         API_params["data"] = f"""
#             fields name;
#             where id = {i};
#         """
#         API_url = API_endpoint + API_command
#         r = requests.post(API_url, **API_params)
#         data = r.json()
#         if data.copy() == [].copy():
#             continue
#         genre_list.append(data[0]["name"])
#     return genre_list
# 
# print(get_all_genres())

# API_url = API_endpoint + API_command
# r = requests.post(API_url, **API_params)
# data = r.json()
# 
# print(data)
# print(API_url)

# print(r.content)

# from igdb.wrapper import IGDBWrapper
# from igdb.igdbapi_pb2 import GameResult
# 
# wrapper = IGDBWrapper(YOUR_API_KEY)
# IGDB_request = wrapper.api_request(
#     'games.pb', # Note the '.pb' suffix at the endpoint
#     'fields id, name; offset 0; where platforms=48;'
# )
# 
# games_message = GameResult()
# games_message.ParseFromString(IGDB_request)
