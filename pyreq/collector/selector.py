from lxml.html import fromstring
from urllib.parse import urljoin
import re


def collect_attr(content, selector, attr):
    root = fromstring(content)
    for el in root.cssselect(selector):
        yield el.get(attr)


def collect_links(content, selector, base_url="/"):
    pattern = re.compile("^http")
    gen = collect_attr(content, selector, "href")
    for url in gen:
        if not pattern.match(url):
            url = urljoin(base_url, url)
            if url == base_url:
                continue
        yield url


if __name__ == "__main__":
    # python -m pyreq.collector.selector
    from ..fetcher.restful_req import Agent

    url = "https://www.naver.com"
    agent = Agent(url)
    content = agent.get().content

    for url in collect_links(content, "a", url):
        print(url)
