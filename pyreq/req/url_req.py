import urllib.request as req
from urllib.error import HTTPError, URLError


def res(url, read=False):
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


def res_text(url, encoding="utf-8"):
    return res(url, True).decode(encoding)


if __name__ == "__main__":
    res = res_text("https://google.com")

    print(res)
