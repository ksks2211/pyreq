import urllib.request as req
from urllib.error import HTTPError, URLError
import json


def fetch_res(url, read=False):
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


def fetch_text(url: str, encoding="utf-8"):
    return fetch_res(url, True).decode(encoding)


# JSON => python dict
def fetch_json(url: str) -> dict:
    return json.loads(fetch_res(url, True))


if __name__ == "__main__":
    res = fetch_json("http://192.168.0.3:1234")
    print(res)
