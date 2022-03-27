import urllib.request as req
from urllib.error import HTTPError, URLError


def get_response(url, read=False):
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


def get_text(url, encoding="utf-8"):
    return get_response(url, True).decode(encoding)


if __name__ == "__main__":
    res = get_text("https://google.com")

    print(res)
