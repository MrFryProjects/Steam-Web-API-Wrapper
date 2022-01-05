import urllib.request
import json


def request(url):
    return urllib.request.urlopen(url)


class GetNewsForApp:
    def __init__(self, appid, maxlength=0, enddate=None, count=None):
        self.appid = appid
        self.maxlength = maxlength
        self.enddate = enddate
        self.count = count
        self.data = None
        self.gid = []
        self.title = []
        self.url = []
        self.is_external_url = []
        self.author = []
        self.contents = []
        self.feedlabel = []
        self.date = []
        self.feedname = []
        self.feed_type = []

    def raw(self):
        _url_components = ['http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?','appid=',self.appid,'&maxlength=',self.maxlength]
        
        if self.enddate is not None:
            _url_components.extend(['&enddate=',self.enddate])
        
        if self.count is not None:
            _url_components.extend(['&count=',self.count])

        _url_components = [str(i) for i in _url_components]

        url = ''.join(_url_components)
        raw = request(url)
        return raw

    def _data(self):
        self.data = json.loads(self.raw().read().decode('utf8'))

    def _gid(self, n):
        self.gid.append(n['gid'])

    def _title(self, n):
        self.title.append(n['title'])

    def _url(self, n):
        self.url.append(n['url'])

    def _is_external_url(self, n):
        self.is_external_url.append(n['is_external_url'])

    def _author(self, n):
        self.author.append(n['author'])

    def _contents(self, n):
        self.contents.append(n['contents'])

    def _feedlabel(self, n):
        self.feedlabel.append(n['feedlabel'])

    def _date(self, n):
        self.date.append(n['date'])

    def _feedname(self, n):
        self.feedname.append(n['feedname'])

    def _feed_type(self, n):
        self.feed_type.append(n['feed_type'])

    def _data_compiler(self):
        self._data()

        for i in self.data['appnews']['newsitems']:
            self._gid(i)
            self._title(i)
            self._url(i)
            self._is_external_url(i)
            self._author(i)
            self._contents(i)
            self._feedlabel(i)
            self._date(i)
            self._feedname(i)
            self._feed_type(i)

    def compile(self):
        self._data_compiler()