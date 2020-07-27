from dotenv import load_dotenv
import requests
import os

load_dotenv()

YOUR_API_KEY = os.getenv("YOUR_API_KEY")

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

API_endpoint = "https://api-v3.igdb.com/"
API_command = ""
API_params = {
        'headers': {'user-key': YOUR_API_KEY},
        'data': """
            fields name;
        """
    }



API_command = "games"
API_params["data"] = """
            fields *;
            where name = "Animal Crossing: New Horizons";
        """
API_url = API_endpoint + API_command
r = requests.post(API_url, **API_params)
data = r.json()
print(data)

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

# print(get_all_platforms())

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
