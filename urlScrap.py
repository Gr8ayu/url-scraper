import requests, sys
from bs4 import BeautifulSoup as bs
from urllib.parse import urlparse

def URLCollector(URL):
    # URL = input("ENTER URL : ")

    try:
        page = requests.get(URL)
    except Exception as e:
        print(e)
        print("\nCouldn't load page : Enter Valid URL in format https://www.example.com")
        return []

    soup = bs(page.content, 'html.parser')

    body =soup.find("body")
    a_tags = body.findAll('a')

    urls = []
    for tag in a_tags:
        if 'href' in tag.attrs:
            url = tag.attrs['href']
        else:
            continue

        if urlparse(url).netloc and url not in urls:
            urls.append(url)

    return urls

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Enter the URL as : https://www.example.com")
    else:
        urls = URLCollector(sys.argv[1])

        for url in urls:
            print(url)
