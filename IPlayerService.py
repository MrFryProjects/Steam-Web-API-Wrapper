import urllib.request
import json


def request(url):
    return urllib.request.urlopen(url)


class GetOwnedGames:
    def __init__(self, steamid, api_key):
        self.steamid = steamid
        self.api_key = api_key
        self.data = None
        self.game_count = int()
        self.appid = []
        self.playtime_forever = []
        self.playtime_windows_forever = []
        self.playtime_mac_forever = []
        self.playtime_linux_forever = []
        return

    def raw(self):

        _url_components = ['http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?','&key=',self.api_key,'&steamid=',self.steamid]

        _url_components = [str(i) for i in _url_components]

        url = ''.join(_url_components)
        raw = request(url)
        return raw

    def _data(self):
        self.data = json.loads(self.raw().read().decode('utf8'))

    def _appid(self, n):
        self.appid.append(n['appid'])

    def _playtime_forever(self, n):
        self.playtime_forever.append(n['playtime_forever'])

    def _playtime_windows_forever(self, n):
        self.playtime_windows_forever.append(n['playtime_windows_forever'])

    def _playtime_mac_forever(self, n):
        self.playtime_mac_forever.append(n['playtime_mac_forever'])

    def _playtime_linux_forever(self, n):
        self.playtime_linux_forever.append(n['playtime_linux_forever'])

    def _data_compiler(self):
        self._data()
        self.game_count = self.data['response']['game_count']

        for i in self.data['response']['games']:
            self._appid(i)
            self._playtime_forever(i)
            self._playtime_windows_forever(i)
            self._playtime_mac_forever(i)
            self._playtime_linux_forever(i)

    def compile(self):
        self._data_compiler()


class GetRecentlyPlayedGames:
    def __init__(self, steamid, api_key):
        self.steamid = steamid
        self.api_key = api_key
        self.data = None
        self.total_count = int()
        self.appid = []
        self.name = []
        self.playtime_2weeks = []
        self.playtime_forever = []
        self.img_icon_url = []
        self.img_logo_url = []
        self.playtime_windows_forever = []
        self.playtime_mac_forever = []
        self.playtime_linux_forever = []
        return

    def raw(self):

        _url_components = ['http://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/?','appid=',self.appid,'&key=',self.api_key,'&steamid=',self.steamid]

        _url_components = [str(i) for i in _url_components]

        url = ''.join(_url_components)
        raw = request(url)
        return raw

    def _data(self):
        self.data = json.loads(self.raw().read().decode('utf8'))

    def _appid(self, n):
        self.appid.append(n['appid'])

    def _name(self, n):
        self.name.append(n['name'])

    def _playtime_2weeks(self, n):
        self.playtime_2weeks.append(n['playtime_2weeks'])

    def _playtime_forever(self, n):
        self.playtime_forever.append(n['playtime_forever'])

    def _img_icon_url(self, n):
        self.img_icon_url.append(n['img_icon_url'])

    def _img_logo_url(self, n):
        self.img_logo_url.append(n['img_logo_url'])

    def _playtime_windows_forever(self, n):
        self.playtime_windows_forever.append(n['playtime_windows_forever'])

    def _playtime_mac_forever(self, n):
        self.playtime_mac_forever.append(n['playtime_mac_forever'])

    def _playtime_linux_forever(self, n):
        self.playtime_linux_forever.append(n['playtime_linux_forever'])

    def _data_compiler(self):
        self._data()
        self.total_count = self.data['response']['total_count']

        for i in self.data['response']['games']:
            self._appid(i)
            self._name(i)
            self._playtime_2weeks(i)
            self._playtime_forever(i)
            self._img_icon_url(i)
            self._img_logo_url(i)
            self._playtime_windows_forever(i)
            self._playtime_mac_forever(i)
            self._playtime_linux_forever(i)

    def compile(self):
        self._data_compiler()