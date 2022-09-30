import handler

def GetOwnedGames(API_Key: str, steamid: str, include_appinfo: bool=False, 
                  include_played_free_games: bool=False, _format: str="json"):
    module = "IPlayerService"
    interface = "GetOwnedGames/v0001"
    args = ['&steamid=', str(steamid), 
            '&include_appinfo=', handler.boolForceString(include_appinfo), 
            '&include_played_free_games=', 
            handler.boolForceString(include_played_free_games), 
            ]
    return handler.data(module, interface, API_Key, args, _format)

def GetRecentlyPlayedGames(API_Key: str, steamid: str, count: str="", 
                           _format: str="json"):
    module = "IPlayerService"
    interface = "GetRecentlyPlayedGames/v0001"
    args = ['&steamid=', str(steamid), 
            '&count=', str(count), 
            ]
    return handler.data(module, interface, API_Key, args, _format)