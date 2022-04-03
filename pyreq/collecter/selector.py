from lxml.html import fromstring, tostring
from urllib.parse import urljoin
import re


def collect_links(content, selector, base_url="/"):
    root = fromstring(content)
    pattern = re.compile("^http")
    for el in root.cssselect(selector):
        url = el.get("href")
        if not pattern.match(url):
            url = urljoin(base_url, url)
            if url == base_url:
                continue
        yield url
