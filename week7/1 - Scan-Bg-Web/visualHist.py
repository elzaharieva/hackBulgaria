import json
import matplotlib.pyplot as plt


def load():
    json1_file = open('hist.json')
    json1_str = json1_file.read()
    json1_data = json.loads(json1_str)
    return json1_data


def to_hist(json1_data):
    k = []
    sizes = []
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
    explode = (0, 0.1, 0, 0)
    for x in json1_data:
        k.append(x)
        sizes.append(json1_data[x])
    plt.pie(sizes, explode=explode, labels=k, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')

    plt.show()

to_hist(load())
