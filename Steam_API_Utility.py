import ISteamUser

api = 
#steamid = 
steamid = 


y = ISteamUser.GetFriendList(steamid, api).raw().read()
z = ISteamUser.GetFriendList(steamid, api)
z.compile()
#print(y)
print(z.steamids)
#print(z)












#https://partner.steamgames.com/doc/webapi

# https://steamcommunity.com/dev
# https://developer.valvesoftware.com/wiki/Steam_Web_API

#def APIpull(self, steamID):
#    return urllib.request.urlopen('https://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key='+self.apiKey+'&steamid='+steamID).read().decode('utf8')


#def apiPull2(steamID):
#return urllib.request.urlopen('https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key='+self.apiKey+'&steamids='+steamID).read().decode('utf8') #use + between steamID to pull multiple steam IDs







#import Steam_API_Utility as sau

#a = sau.ISteamUser(steamIDs).GetPlayerSummaries
#b = sau.ISteamUser(steamIDs).GetPlayerSummaries.personaname
#c = sau.ISteamUser(steamIDs).GetPlayerSummaries.avatar

#d = sau.ISteamUser(steamIDs).GetFriendList
#e = sau.ISteamUser(steamIDs).GetFriendList.steamid
#f = sau.ISteamUser(steamIDs).GetFriendList.friend_since