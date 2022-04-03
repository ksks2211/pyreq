import requests
import urllib.parse as parse
from multimethod import multimethod
from copy import deepcopy

# URL: str = "https//www.example.com"
# HEADERS: dict = {"Content-Type": "application/json; charset=utf-8"}
# BODY: dict = {"KEY": "VALUE"}
# COOKIES: dict = {"session_id": "session id"}
# AUTH: tuple = ("id", "password")
# FILES: dict = {"file": ("img.jpg", open("img.jpg", "rb"))}


class Agent:
    def __init__(self, url: str, session=False):
        url = parse.urlparse(url)
        self.url_dict = {
            "scheme": url.scheme,
            "netloc": url.netloc,
            "path": "",  # /path/to/something
            "params": "",
            "fragment": "",
            "query": "",  # /?key=value
        }

        self.options_dict = {
            "headers": {"content-type": "application/json; charset=utf-8"}
        }

        self.req = requests.session() if session else requests

    def get_url(self, **kwargs):
        url_dict = self.url_dict.copy()
        if kwargs.get("query"):
            url_dict["query"] = parse.urlencode(kwargs.get("query"))
        if kwargs.get("path"):
            url_dict["path"] = kwargs.get("path")
        return parse.ParseResult(**url_dict).geturl()

    def set_url(self, **kwargs):
        if kwargs.get("query"):
            self.url_dict["query"] = parse.urlencode(kwargs.get("query"))
        if kwargs.get("path"):
            self.url_dict["path"] = kwargs.get("path")

    def add_header(self, name, value):
        self.options_dict["headers"][name] = value

    def remove_header(self, name):
        if self.options_dict["headers"].get(name):
            del self.options_dict["headers"][name]

    def get_headers(self):
        return self.options_dict["headers"]

    @multimethod
    def get(self, **options: str):
        return self.get(self.get_url(), **options)

    @multimethod
    def get(self, url: str, **options: str):
        if not options:
            options = self.options_dict
        return self.req.get(url, **options)

    @multimethod
    def post(self, body=dict(), **options: str):
        print(body)
        return self.post(self.get_url(), json=body, **options)

    @multimethod
    def post(self, url: str, body=dict(), **options: str):
        if not options:
            options = self.options_dict
        if body:
            options = deepcopy(options)
            options["json"] = body
        return self.req.post(url, **options)

    @multimethod
    def delete(self, **options: str):

        return self.delete(self.get_url(), **options)

    @multimethod
    def delete(self, url: str, **options: str):
        if not options:
            options = self.options_dict
        return self.req.delete(url, **options)

    @multimethod
    def put(self, **options: str):
        return self.put(self.get_url(), **options)

    @multimethod
    def put(self, url: str, **options: str):
        if not options:
            options = self.options_dict
        return self.req.put(url, **options)


if __name__ == "__main__":

    agent = Agent("http://192.168.0.3:1234")

    agent.add_header("key", "value")
    data = {"name": "kim", "age": 10, "arr": [1, 2, 3, 4]}
    print(agent.post(data).json())
