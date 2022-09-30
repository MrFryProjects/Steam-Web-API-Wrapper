import handler

def GetNewsForApp(API_Key: str, appid: str, count: str="3", 
                  maxlength: str="300", _format: str="json"):
    module = "ISteamNews"
    interface = "GetNewsForApp/v0002"
    args = ['&appid=', str(appid), 
            '&count=', str(count), 
            '&maxlength=', str(maxlength), 
            ]
    return handler.data(module, interface, API_Key, args, _format)