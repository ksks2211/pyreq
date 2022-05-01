from ..fetcher import fetch_res
from bs4 import BeautifulSoup
import csv


def table_to_csv(url: str, path: str, selector="table"):
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)

        res_bytes = fetch_res(url, True)
        soup = BeautifulSoup(res_bytes, "html.parser")
        table = soup.select_one(selector)
        rows = table.select("tr")

        ths = [th.get_text().strip() for th in rows[0].select("th")]
        writer.writerow(ths)
        for row in rows[1:]:
            tds = [td.get_text().strip() for td in row.select("td")]
            writer.writerow(tds)


if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Demographics_of_the_United_States"
    path = "./file/usa.csv"
    selector = "#mw-content-text > div.mw-parser-output > table:nth-child(75)"
    table_to_csv(url, path, selector)
