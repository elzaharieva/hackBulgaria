import json

class Histogram:

    def __init__(self):
        self.my_dict = {}

    def add(self, strr):
        if strr != "Apache" and strr != "IIS" and strr != "nginx" and strr != "lighttpd":
            return False
        else:
            if strr not in self.my_dict:
                self.my_dict[strr] = 1
            else:
                self.my_dict[strr] += 1

    def count(self, strr):
        if strr not in self.my_dict:
            return None
        else:
            return self.my_dict[strr]

    def __str__(self):
        for key, count in self.my_dict.items():
            print("{}: {}".format(key, count))

    def get_dict(self):
        return self.my_dict

    def saving_method(self, path):
        with open(path, 'w') as fp:
            json.dump(self.my_dict, fp)
