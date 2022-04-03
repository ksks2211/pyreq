import urllib.request as req
from urllib.error import HTTPError, URLError
import json


def fetch_res(url, read=False):
    try:
        res = req.urlopen(url)
    except HTTPError as e:
        print("Failed")
        print(e)
    except URLError as e:
        print("Failed")
        print(e)
    except Exception as e:
        print("Failed")
        print(e)

    if read:
        return res.read()
    return res


def fetch_text(url, encoding="utf-8"):
    return fetch_res(url, True).decode(encoding)


# JSON => python dict
def fetch_json(url):
    return json.loads(fetch_res(url, True))


if __name__ == "__main__":
    res = fetch_json("http://192.168.0.3:1234/")

    print(res)
