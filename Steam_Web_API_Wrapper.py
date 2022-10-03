import urllib.request
import urllib.parse
import json

class Steam:
    def __init__(self, api_key: str="", format: str="json"):
        self.api_key = api_key
        self.format = format

    def deserialize_json(self, object):
        try:
            return json.load(object)
        except Exception:
            print(f'JSON Deserialization Error on: {object}')

    def request(self, url):
        try:
            html_return = urllib.request.urlopen(url)
            if self.format == "json":
                return json.load(html_return)
        except urllib.error.HTTPError:
            print(f'HTTP Error: {url}')

    def url_builder(self,/, module: str, interface: str, api_version: int, *,
                   endpoint: str="http://api.steampowered.com", **kwargs):
        api_version = f'v{api_version}'
        url_start = '/'.join([endpoint, module, interface, api_version])
        url_components = [url_start, '/?', f'key={self.api_key}']
        for name, val in kwargs.items():
            url_components.append(f'&{name}={val}')
        url_components.append(f'&format={self.format}')
        return ''.join(url_components)

    def url_builder_service(self, module: str, 
                            interface: str, api_version: int, *, 
                            endpoint: str="http://api.steampowered.com",
                           **kwargs):
        api_version = f'v{api_version}'
        url_start = '/'.join([endpoint, module, interface, api_version])
        url_components = [url_start, f'/?key={self.api_key}', 
                          f'&format={self.format}&input_json=']
        url_components.append(urllib.parse.quote(json.dumps(kwargs)))
        return ''.join(url_components)

    # IPlayerService
    # https://partner.steamgames.com/doc/webapi/IPlayerService

    def get_recently_played_games(self, steamid: str, count: int=0):
        module = "IPlayerService"
        interface = "GetRecentlyPlayedGames"
        api_version = 1
        url = self.url_builder(module, interface, api_version, 
                               steamid=steamid, count=count)
        return self.request(url)

    def get_owned_games(self, steamid: str, include_appinfo: bool=False,
                       include_played_free_games: bool=False, 
                       appids_filter: list[int]=[]):
        module = "IPlayerService"
        interface = "GetOwnedGames"
        api_version = 1
        url = self.url_builder_service(module, interface, api_version, 
                        steamid=steamid, include_appinfo=include_appinfo,
                        include_played_free_games=include_played_free_games, 
                        appids_filter=appids_filter)
        return self.request(url)

    def get_steam_level(self, steamid: str):
        module = "IPlayerService"
        interface = "GetSteamLevel"
        api_version = 1
        url = self.url_builder(module, interface, api_version, 
                               steamid=steamid)
        return self.request(url)

    def get_badges(self, steamid: str):
        module = "IPlayerService"
        interface = "GetBadges"
        api_version = 1
        url = self.url_builder(module, interface, api_version, 
                               steamid=steamid)
        return self.request(url)

    def get_community_badge_progress(self, steamid: str, badgeid: int):
        module = "IPlayerService"
        interface = "GetCommunityBadgeProgress"
        api_version = 1
        url = self.url_builder(module, interface, api_version, 
                               steamid=steamid, badgeid=badgeid)
        return self.request(url)

    # ISteamApps
    # https://partner.steamgames.com/doc/webapi/ISteamApps

    def get_app_list(self):
        module = "ISteamApps"
        interface = "GetAppList"
        api_version = 2
        url = self.url_builder(module, interface, api_version)
        return self.request(url)

    def up_to_date_check(self, appid: int, version: int):
        module = "ISteamApps"
        interface = "UpToDateCheck"
        api_version = 1
        url = self.url_builder(module, interface, api_version, appid=appid, 
                               version=version)
        return self.request(url)

    # ISteamNews
    # https://partner.steamgames.com/doc/webapi/ISteamNews

    def get_news_for_app(self, appid: int, maxlength: int, enddate: int, 
                         count: int=20, feeds: list[str]=[]):
        module = "ISteamNews"
        interface = "GetNewsForApp"
        api_version = 2
        feeds = ','.join(feeds)
        url = self.url_builder(module, interface, api_version, appid=appid, 
                               maxlength=maxlength, enddate=enddate, 
                               count=count, feeds=feeds)
        return self.request(url)

    # ISteamUserStats
    # https://partner.steamgames.com/doc/webapi/ISteamUserStats
    
    def get_global_achievement_percentages_for_app(self, gameid: int):
        module = "ISteamUserStats"
        interface = "GetGlobalAchievementPercentagesForApp"
        api_version = 2
        url = self.url_builder(module, interface, api_version, gameid=gameid)
        return self.request(url)

    # https://partner.steamgames.com/doc/features/achievements#global_stats
    def get_global_stats_for_game(self, appid: int, count: int, name: str, 
                                  startdate: int, enddate: int):
        module = "ISteamUserStats"
        interface = "GetGlobalStatsForGame"
        api_version = 1
        url = self.url_builder(module, interface, api_version, appid=appid,
                               count=count, name=name, startdate=startdate,
                               enddate=enddate)
        return self.request(url)

    def get_number_of_current_players(self, appid: int):
        module = "ISteamUserStats"
        interface = "GetNumberOfCurrentPlayers"
        api_version = 1
        url = self.url_builder(module, interface, api_version, appid=appid)
        return self.request(url)

    def get_player_achievements(self, steamid: str, appid: int, l: str='en'):
        module = "ISteamUserStats"
        interface = "GetPlayerAchievements"
        api_version = 1
        url = self.url_builder(module, interface, api_version, 
                               steamid=steamid, appid=appid, l=l)
        return self.request(url)

    def get_schema_for_game(self, appid: int, l: str='en'):
        module = "ISteamUserStats"
        interface = "GetSchemaForGame"
        api_version = 2
        url = self.url_builder(module, interface, api_version, appid=appid, 
                               l=l)
        return self.request(url)

    def get_user_stats_for_game(self, steamid: int, appid: int):
        module = "ISteamUserStats"
        interface = "GetUserStatsForGame"
        api_version = 2
        url = self.url_builder(module, interface, api_version, 
                               steamid=steamid, appid=appid)
        return self.request(url)

    # ISteamUser
    # https://partner.steamgames.com/doc/webapi/ISteamUser

    def get_friend_list(self, steamid: int, relationship: str=""):
        module = "ISteamUser"
        interface = "GetFriendList"
        api_version = 1
        url = self.url_builder(module, interface, api_version, 
                               steamid=steamid, relationship=relationship)
        return self.request(url)

    def get_player_bans(self, steamids: list[str]):
        module = "ISteamUser"
        interface = "GetPlayerBans"
        api_version = 1
        steamids = ','.join(steamids)
        url = self.url_builder(module, interface, api_version, 
                               steamids=steamids)
        return self.request(url)

    def get_player_summaries(self, steamids: list[str]):
        module = "ISteamUser"
        interface = "GetPlayerSummaries"
        api_version = 2
        steamids = ','.join(steamids)
        url = self.url_builder(module, interface, api_version, 
                               steamids=steamids)
        return self.request(url)

    def get_user_group_list(self, steamid: int):
        module = "ISteamUser"
        interface = "GetUserGroupList"
        api_version = 1
        url = self.url_builder(module, interface, api_version, 
                               steamid=steamid)
        return self.request(url)

    def get_user_group_list(self, vanityurl: str, url_type: int=1):
        module = "ISteamUser"
        interface = "ResolveVanityURL"
        api_version = 1
        url = self.url_builder(module, interface, api_version, 
                               vanityurl=vanityurl, url_type=url_type)
        return self.request(url)

    # ISteamWebAPIUtil
    # https://partner.steamgames.com/doc/webapi/ISteamWebAPIUtil

    def get_server_info(self):
        module = "ISteamWebAPIUtil"
        interface = "GetServerInfo"
        api_version = 1
        url = self.url_builder(module, interface, api_version)
        return self.request(url)

    def get_supported_api_list(self):
        module = "ISteamWebAPIUtil"
        interface = "GetSupportedAPIList"
        api_version = 1
        url = self.url_builder(module, interface, api_version)
        return self.request(url)
