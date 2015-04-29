from bs4 import BeautifulSoup
import requests
import urllib.request


def prepare_link(url, href):
    return urllib.parse.urljoin(url, href)


def take_servers():
    f = open("histogram.txt", 'w')
    site_link = "http://register.start.bg/"
    r = requests.get(site_link)
    html = r.text
    soup = BeautifulSoup(html)
    for link in soup.find_all('a'):
        new_link = prepare_link(site_link, link.get('href'))
        try:
            my_req = requests.get(new_link, timeout=4)
        except:
            continue
        try:
            serv = my_req.headers["Server"]
        except:
            continue
        f.write("{}\n".format(serv))
    f.close()

take_servers()
