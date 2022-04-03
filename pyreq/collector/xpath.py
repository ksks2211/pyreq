from lxml.html import fromstring, tostring
import json


def collect_attr(content, xpath, attr=None):
    root = fromstring(content)
    for el in root.xpath(xpath):
        if attr:
            yield el.get(attr)
        else:
            yield el


if __name__ == "__main__":
    # python -m pyreq.collector.xpath
    from ..fetcher.restful_req import Agent

    url = "https://www.naver.com"
    agent = Agent(url)
    content = agent.get().content

    xpath1 = "//div[@class='thumb_area']/div/a[@class='thumb']/img"
    xpath2 = "//div[@class='thumb_area']/div/div[@class='popup_wrap']/a[3]"

    names = collect_attr(content, xpath1)
    addrs = collect_attr(content, xpath2)

    result = dict()
    for name, addr in zip(names, addrs):
        result[name.get("alt")] = addr.get("href")

    with open("./file.json", "w") as f:
        json.dump(result, f)
