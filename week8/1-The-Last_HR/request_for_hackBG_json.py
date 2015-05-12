import json
import requests


def take_json():
    site_link = "https://hackbulgaria.com/api/students/"
    r = requests.get(site_link)
    html = r.text
    f = open("request_for_hack_bulgaria.json", 'w')
    json.dump(html, f)
