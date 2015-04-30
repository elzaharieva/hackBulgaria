from needleInHaystack import count_substrings
from histogramClass import Histogram
import json


def reading_from_histogram_file():
    h = Histogram()
    path = "histogram.txt"
    f = open(path, 'r')
    text = f.read().split('\n')
    f.close()
    for i in range(0, len(text)):
        if count_substrings(text[i], "Apache") > 0:
            h.add("Apache")
        elif count_substrings(text[i], "IIS") > 0 or count_substrings(text[i], "Microsoft") > 0:
            h.add("IIS")
        elif count_substrings(text[i], "nginx") > 0:
            h.add("nginx")
        elif count_substrings(text[i], "light") > 0:
            h.add("lighttpd")
        else:
            pass

    fp = open("hist.json", 'w')
    json.dump(h.my_dict, fp)
