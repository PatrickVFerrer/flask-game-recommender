from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

YOUR_API_KEY = os.getenv("YOUR_API_KEY")

###############     NOTE: THEY HAVE IMAGES!     ###############
### Group together RTS, Strategy, TBS, Tactical
### Group together Pinball, Quiz/Trivia, Arcade
### Rename "Beat 'em up" to "Brawler" in drop-down selection
ALL_GENRES = [
    'Point-and-click', 'Fighting', 'Shooter', 'Music', 
    'Platform', 'Puzzle', 'Racing', 'Real Time Strategy (RTS)', 
    'Role-playing (RPG)', 'Simulator', 'Sport', 'Strategy', 
    'Turn-based strategy (TBS)', 'Tactical', "Hack and slash/Beat 'em up", 
    'Quiz/Trivia', 'Pinball', 'Adventure', 'Indie', 'Arcade', 
    'Visual Novel', 'Card & Board Game', 'MOBA'
]
ALL_GENRE_IDS = [
    2, 4, 5, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 24, 25,
    26, 30, 31, 32, 33, 34, 35, 36
]

### Group together PC & Mac
### Group together Xbox 360 & Xbox Live Arcade
### Group together iOS & Android
### Group together 3DS & New 3DS
### Group together Oculus, SteamVR, PlayStation VR
ALL_PLATFORMS = [
    'PC (Microsoft Windows)', 'Xbox 360', 'Xbox Live Arcade', 
    'PlayStation 3', 'Mac', 'Android', 'Nintendo 3DS', 'iOS', 
    'Wii U', 'PlayStation 4', 'Xbox One', 'Nintendo Switch', 
    'New Nintendo 3DS', 'Oculus VR', 'SteamVR', 'PlayStation VR', 
    'PlayStation 5', 'Xbox Series X', 'Google Stadia'
]
ALL_PLATFORM_IDS = [
    6, 12, 36, 9, 14, 34, 37, 39, 
    41, 48, 49, 130, 137, 162, 163,
    165, 167, 169, 170
]

API_endpoint = "https://api-v3.igdb.com/"
API_command = "games"
API_params = {
        'headers': {'user-key': YOUR_API_KEY},
        'data': """
            fields *;
            where 
        """
    }

# 
def get_games(platform, genre):
    game_list = []
    API_command = "games"
    platform_id = ALL_PLATFORM_IDS[ALL_PLATFORMS.index(platform)]
    genre_id = ALL_GENRE_IDS[ALL_GENRES.index(genre)]    
    API_params["data"] = f"""
        fields *;
        where platforms = {platform_id} & genres = {genre_id};
        sort popularity desc;
        limit 50;
    """
    API_url = API_endpoint + API_command
    r = requests.post(API_url, **API_params)
    game_list = r.json()
    pprint(game_list)
# 
# pprint(get_games(x, y))

# def get_platform_ids():
#     API_command = "platforms"     
#     id_list = []
#     for platform in ALL_PLATFORMS:
#         # print(f"Query {i}")
#         API_params["data"] = f"""
#             fields name, id;
#             where name = "{platform}";
#         """
#         API_url = API_endpoint + API_command
#         r = requests.post(API_url, **API_params)
#         data = r.json()
#         pprint(data)
#         id_list.append(data[0]["id"])
#     print(len(id_list))
#     print(len(ALL_PLATFORMS))
#     return id_list
# 
# pprint(get_platform_ids())

# def get_genre_ids():
#     API_command = "genres"     
#     id_list = []
#     for genre in ALL_GENRES:
#         # print(f"Query {i}")
#         API_params["data"] = f"""
#             fields name, id;
#             where name = "{genre}";
#         """
#         API_url = API_endpoint + API_command
#         r = requests.post(API_url, **API_params)
#         data = r.json()
#         pprint(data)
#         id_list.append(data[0]["id"])
#     print(len(id_list))
#     print(len(ALL_GENRES))
#     return id_list
# 
# pprint(get_genre_ids())

# API_command = "games"
# API_params["data"] = """
#             fields *;
#             where name = "Animal Crossing: New Horizons";
#         """
# API_url = API_endpoint + API_command
# r = requests.post(API_url, **API_params)
# data = r.json()
# pprint(data)

# def get_all_platforms():
#     API_command = "platforms"
#     platform_list = []
#     for i in range(190):
#         print(f"Query {i}")
#         API_params["data"] = f"""
#             fields name;
#             where id = {i};
#         """
#         API_url = API_endpoint + API_command
#         r = requests.post(API_url, **API_params)
#         data = r.json()
#         if data.copy() == [].copy():
#             continue
#         platform_list.append(data[0]["name"])
#     return platform_list
# 
# pprint(get_all_platforms())

# def get_all_genres():
#     API_command = "genres"     
#     genre_list = []
#     for i in range(37):
#         print(f"Query {i}")
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
# pprint(get_all_genres())

# API_url = API_endpoint + API_command
# r = requests.post(API_url, **API_params)
# data = r.json()
# 
# pprint(data)
# print(API_url)
# 
# pprint(r.content)

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
