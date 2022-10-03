import handler

def GetPlayerSummaries(API_Key: str, steamids: list, _format: str="json"):
    module = "ISteamUser"
    interface = "GetPlayerSummaries/v0002"
    steamids = handler.forceList(steamids)
    steamids_str = ",".join(steamids)
    args = ['&steamids=', steamids_str, 
            ]
    return handler.data(module, interface, API_Key, args, _format)

def GetFriendList(API_Key: str, steamid: str, relationship: str="friend", 
                  _format: str="json"):
    module = "ISteamUser"
    interface = "GetFriendList/v0001"
    args = ['&steamid=', str(steamid), 
            '&relationship=', relationship,
            ]
    return handler.data(module, interface, API_Key, args, _format)
