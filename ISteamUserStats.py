import urllib.request
import json


def request(url):
    return urllib.request.urlopen(url)


class GetGlobalAchievementPercentagesForApp:
    def __init__(self, gameid):
        self.gameid = gameid
        self.data = None
        self.name = []
        self.percent = []
        return

    def raw(self):

        _url_components = ['http://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002/?','gameid=',self.gameid]

        _url_components = [str(i) for i in _url_components]

        url = ''.join(_url_components)
        raw = request(url)
        return raw


    def _data(self):
        self.data = json.loads(self.raw().read().decode('utf8'))

    def _name(self, n):
        self.name.append(n['name'])

    def _percent(self, n):
        self.percent.append(n['percent'])

    def _data_compiler(self):
        self._data()

        for i in self.data['achievementpercentages']['achievements']:
            self._name(i)
            self._percent(i)

    def compile(self):
        self._data_compiler()


class GetPlayerAchievements:
    def __init__(self, steamid, appid, api_key):
        self.steamid = steamid
        self.appid = appid
        self.api_key = api_key
        self.data = None
        self.gameName = ""
        self.apiname = []
        self.achieved = []
        self.unlocktime = []
        return

    def raw(self):

        _url_components = ['http://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/?','appid=',self.appid,'&key=',self.api_key,'&steamid=',self.steamid]

        _url_components = [str(i) for i in _url_components]

        url = ''.join(_url_components)
        raw = request(url)
        return raw

    def _data(self):
        self.data = json.loads(self.raw().read().decode('utf8'))

    def _apiname(self, n):
        self.apiname.append(n['apiname'])

    def _achieved(self, n):
        self.achieved.append(n['achieved'])

    def _unlocktime(self, n):
        self.unlocktime.append(n['unlocktime'])

    def _data_compiler(self):
        self._data()
        self.gameName = self.data['playerstats']['gameName']

        for i in self.data['playerstats']['achievements']:
            self._apiname(i)
            self._achieved(i)
            self._unlocktime(i)

    def compile(self):
        self._data_compiler()


class GetUserStatsForGame:
    def __init__(self, steamid, appid, api_key):
        self.steamid = steamid
        self.appid = appid
        self.api_key = api_key
        self.data = None
        self.gameName = ""
        self.name = []
        self.value = []
        return

    def raw(self):

        _url_components = ['http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?','appid=',self.appid,'&key=',self.api_key,'&steamid=',self.steamid]

        _url_components = [str(i) for i in _url_components]

        url = ''.join(_url_components)
        raw = request(url)
        return raw

    def _data(self):
        self.data = json.loads(self.raw().read().decode('utf8'))

    def _name(self, n):
        self.name.append(n['name'])

    def _value(self, n):
        self.value.append(n['value'])

    def _data_compiler(self):
        self._data()
        self.gameName = self.data['playerstats']['gameName']

        for i in self.data['playerstats']['stats']:
            self._name(i)
            self._value(i)

    def compile(self):
        self._data_compiler()
