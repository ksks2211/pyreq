import urllib.request as req
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urlparse
import json


def get_url(url, query: dict) -> str:
    q = urlencode(query)
    glue = "&" if urlparse(url).query else "?"
    return url + glue + q


def fetch_res(url, read=False, query=dict()):
    if query:
        url = get_url(url, query)
    try:
        res = req.urlopen(url)
    except HTTPError as e:
        print("HTTPError")
        print(e)
    except URLError as e:
        print("URLError")
        print(e)
    except Exception as e:
        print("Exception")
        print(e)
    return res.read() if read else res


def fetch_text(url: str, query=dict(), encoding="utf-8"):
    return fetch_res(url, True, query).decode(encoding)


# JSON => python dict
def fetch_json(url: str, query=dict()) -> dict:
    return json.loads(fetch_res(url, True, query))


if __name__ == "__main__":
    URL = "https://api.ipify.org"
    format = {"format": "json"}
    res = fetch_json(URL, format)
    print(res)

    format = {"format": "text"}
    res = fetch_text(URL, format)
    print(res)
