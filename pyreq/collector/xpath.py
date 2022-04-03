from lxml.html import fromstring, tostring


def collect_attr(content, xpath, attr=None):

    root = fromstring(content)
    for el in root.xpath(xpath):
        if attr:
            yield el.get(attr)
        else:
            yield el


if __name__ == "__main__":
    # python -m pyreq.collector.xpath
    import simplejson as json
    from ..fetcher.restful_req import Agent

    url = "https://www.naver.com"
    agent = Agent(url)
    content = agent.get().content
    with open("save/something.html", "w") as f:
        f.write(content.decode("utf-8"))

    xpath1 = "//div[@class='thumb_area']/div/a[@class='thumb']/img"
    xpath2 = "//div[@class='thumb_area']/div/div[@class='popup_wrap']/a[3]"

    names = collect_attr(content, xpath1, "alt")
    addrs = collect_attr(content, xpath2, "href")

    result = dict()
    for name, addr in zip(names, addrs):
        result[name] = addr

    with open("./save/file.json", "w") as f:
        json.dump(result, f, ensure_ascii=False, indent=2 * " ")
