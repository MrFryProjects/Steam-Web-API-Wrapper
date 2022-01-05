import ISteamUser
import ISteamNews
import ISteamUserStats

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

#import Steam_API_Utility as sau

#a = sau.ISteamUser(steamIDs).GetPlayerSummaries
#b = sau.ISteamUser(steamIDs).GetPlayerSummaries.personaname
#c = sau.ISteamUser(steamIDs).GetPlayerSummaries.avatar

#d = sau.ISteamUser(steamIDs).GetFriendList
#e = sau.ISteamUser(steamIDs).GetFriendList.steamid
#f = sau.ISteamUser(steamIDs).GetFriendList.friend_since
