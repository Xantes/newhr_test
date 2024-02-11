from requests import get

def app():
    req_url = 'https://api.ipify.org?format=json'
    geo_url = 'http://ip-api.com/json/'

    ip  = get(req_url).json()
    geo = get(geo_url).json()

    print('IP: ', ip.get('ip'), '\nREGION: ', geo.get('region'))


if __name__ == '__main__':
    app()