import ISteamUser
import ISteamNews
import ISteamUserStats
import IPlayerService

#api_key = 
#steamid = 
#appid = 440


x = IPlayerService.GetRecentlyPlayedGames(steamid, api_key)
x.compile()
print(x.img_icon_url)

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
