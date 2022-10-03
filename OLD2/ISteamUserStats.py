import handler

def GetGlobalAchievementPercentagesForApp(API_Key: str, gameid: str, 
                                          _format: str="json"):
    module = "ISteamUserStats"
    interface = "GetGlobalAchievementPercentagesForApp/v0002"
    args = ['&gameid=', str(gameid), 
            ]
    return handler.data(module, interface, API_Key, args, _format)

def GetPlayerAchievements(API_Key: str, steamid: str, appid: str, 
                          l: str="en", _format: str="json"):
    module = "ISteamUserStats"
    interface = "GetPlayerAchievements/v0001"
    args = ['&steamid=', str(steamid), 
            '&appid=', str(appid),
            '&l=', l,
            ]
    return handler.data(module, interface, API_Key, args, _format)

def GetUserStatsForGame(API_Key: str, steamid: str, appid: str, 
                        l: str="en", _format: str="json"):
    module = "ISteamUserStats"
    interface = "GetUserStatsForGame/v0002"
    args = ['&steamid=', str(steamid), 
            '&appid=', str(appid),
            '&l=', l,
            ]
    return handler.data(module, interface, API_Key, args, _format)
