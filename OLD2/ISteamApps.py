import handler

def GetAppList(API_Key: str="", _format: str="json"):
    module = "ISteamApps"
    interface = "GetAppList/v0002"
    args = []
    return handler.data(module, interface, API_Key, args, _format)

def GetServersAtAddress(addr: str, API_Key: str="", _format: str="json"):
    module = "ISteamApps"
    interface = "GetServersAtAddress/v0001"
    args = ['&addr=', addr, 
            ]
    return handler.data(module, interface, API_Key, args, _format)

def GetServersAtAddress(appid: str, version: str, API_Key: str="", 
                        _format: str="json"):
    module = "ISteamApps"
    interface = "GetServersAtAddress/v0001"
    args = ['&appid=', str(appid),
            '&version=', str(version), 
            ]
    return handler.data(module, interface, API_Key, args, _format)
