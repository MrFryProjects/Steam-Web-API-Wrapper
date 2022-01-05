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