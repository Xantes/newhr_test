from requests import get, Response, RequestException


def get_response(url=None):
    try:
        response: Response = get(url)
    except RequestException as error:
        raise SystemExit(error)

    return response.json()


def app():

    req_url: str = 'https://api.ipify.org?format=json'
    geo_url: str = 'http://ip-api.com/json/'

    ip: dict[str, str] = get_response(req_url)
    geo: dict[str, str] = get_response(geo_url)

    print('IP: ', ip.get('ip'), '\nREGION: ', geo.get('region'))


if __name__ == '__main__':
    app()
