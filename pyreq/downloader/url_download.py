import urllib.request as req
import os
from urllib.error import HTTPError, URLError


def download(url, path):
    try:
        file, header = req.urlretrieve(
            url,
            path,
        )
    except HTTPError as e:
        print("Download Failed")
        print(e)
    except URLError as e:
        print("Download Failed")
        print(e)
    except Exception as e:
        print("Download Failed")
        print(e)
    else:
        print(file + " Download Compeleted")
    return path


if __name__ == "__main__":

    url = "https://upload.wikimedia.org/wikipedia/en/0/05/Hello_kitty_character_portrait.png"
    path = "./kitty.png"
    try:
        download(url, path)
    except:
        pass
    else:
        os.remove(path)
        print("Success")
