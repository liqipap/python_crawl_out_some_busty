#import request
import sys
from bs4 import BeautifulSoup
from urllib2 import urlopen
from pymongo import MongoClient

#first_arg = sys.argv[1]


def spide_that_page(max_pages=100):
    client = MongoClient('localhost:27017')
    db = client.users_of_xvideos
    page = 1
    while page <= max_pages:
        url = 'http://www.xvideos.com/new/' + str(page)
        source_code = urlopen(url)
        # source_code = request.get(url)
        html = source_code
        soup = BeautifulSoup(html, "lxml")
        for tag in soup.find_all('div', {'class': 'thumb-block'}):
            for link in tag.find_all('a'):
                base_url = ("http://www.xvideos.com")
                hrefol = link.get('href')
                href = base_url + str(hrefol)
                # title = link.get('title')

            title = link.string

            print(href)
            print(title)
            db.mycollection.insert_one({"href": href, "name": title})
        page += 1
        exit
spide_that_page()
