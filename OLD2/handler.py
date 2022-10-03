import urllib.request

def request(url):
    try:
        return urllib.request.urlopen(url)
    except urllib.error.HTTPError:
        print("".join(["HTTP Error: ",url]))

def join(components):
    return "".join(components)

def listCheck(object):
    if isinstance(object, list):
        return True
    else:
        return False

def forceList(object):
    if listCheck(object):
        return(object)
    else:
        return [str(object)]

def boolForceString(object):
    if isinstance(object, bool):
        return str(object)
    else:
        return object

def data(module, interface, API_Key, args, _format, 
        site="http://api.steampowered.com"):
    components = [site, '/',
                  module, '/',
                  interface, '/?',
                  '&key=', API_Key,
                  '&format=', _format, 
                  ]
    components += args
    print(join(components))
    return request(join(components))
