import urllib.request
import json


#Calling ISteamUser.GetPlayerSummaries.compile() will auto-populate the data fields
#Calling ISteamUser.GetPlayerSummaries.raw() will return the HTTP object without populating the data fields

def request(url):
    return urllib.request.urlopen(url)

class GetPlayerSummaries:
    def __init__(self, steamid, api_key):
        self.steamid = steamid
        self.api_key = api_key
        self.data = None
        self.communityvisibilitystate = []
        self.profilestate = []
        self.personaname = []
        self.profileurl = []
        self.avatar = []
        self.avatarmedium = []
        self.avatarfull = []
        self.avatarhash = []
        self.lastlogoff = []
        self.personastate = []
        self.primaryclanid = []
        self.timecreated = []
        self.personastateflags = []
        self.loccountrycode = []

    def raw(self):
        _steam_id_string = '+'.join(self.steamid)
        _url_components = ['https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=',self.api_key,'&steamids=',_steam_id_string]
        _url_components.append(_steam_id_string)
        url = ''.join(_url_components)
        raw = request(url)
        return raw

    def _data(self):
        self.data = json.loads(self.raw().read().decode('utf8'))

    def _communityvisibilitystate(self, n):
        self.communityvisibilitystate.append(n['communityvisibilitystate'])

    def _profilestate(self, n):
        self.profilestate.append(n['profilestate'])

    def _personaname(self, n):
        self.personaname.append(n['personaname'])

    def _profileurl(self, n):
        self.profileurl.append(n['profileurl'])

    def _avatar(self, n):
        self.avatar.append(n['avatar'])

    def _avatarmedium(self, n):
        self.avatarmedium.append(n['avatarmedium'])

    def _avatarfull(self, n):
        self.avatarfull.append(n['avatarfull'])

    def _avatarhash(self, n):
        self.avatarhash.append(n['avatarhash'])

    def _lastlogoff(self, n):
        self.lastlogoff.append(n['lastlogoff'])

    def _personastate(self, n):
        self.personastate.append(n['personastate'])

    def _primaryclanid(self, n):
        self.primaryclanid.append(n['primaryclanid'])

    def _timecreated(self, n):
        self.timecreated.append(n['timecreated'])

    def _personastateflags(self, n):
        self.personastateflags.append(n['personastateflags'])

    def _loccountrycode(self, n):
        self.loccountrycode.append(n['loccountrycode'])

    def _data_compiler(self):
        self._data()

        for i in self.data['response']['players']:
            self._communityvisibilitystate(i)
            self._profilestate(i)
            self._personaname(i)
            self._profileurl(i)
            self._avatar(i)
            self._avatarmedium(i)
            self._avatarfull(i)
            self._avatarhash(i)
            self._lastlogoff(i)
            self._personastate(i)
            self._primaryclanid(i)
            self._timecreated(i)
            self._personastateflags(i)
            self._loccountrycode(i)

    def compile(self):
        self._data_compiler()



class GetFriendList:
    def __init__(self, steamid, api_key):
        self.steamid = steamid
        self.api_key = api_key
        self.data = None
        self.steamids = []
        self.relationship = []
        self.friend_since = []

    def raw(self):
        _url_components = ['http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key=',self.api_key,'&steamid=',self.steamid,'&relationship=friend']
        url = ''.join(_url_components)
        raw = request(url)
        return raw

    def _data(self):
        self.data = json.loads(self.raw().read().decode('utf8'))

    def _steamids(self, n):
        self.steamids.append(n['steamid'])

    def _relationship(self, n):
        self.relationship.append(n['relationship'])

    def _friend_since(self, n):
        self.friend_since.append(n['friend_since'])

    def _data_compiler(self):
        self._data()

        for i in self.data['friendslist']['friends']:
            self._steamids(i)
            self._relationship(i)
            self._friend_since(i)

    def compile(self):
        self._data_compiler()

