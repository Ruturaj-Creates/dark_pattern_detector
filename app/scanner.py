from scrapling.fetchers import Fetcher

def fetch_page(url):
    page = Fetcher.get(url)

    return page.body.decode("utf-8", errors="ignore")