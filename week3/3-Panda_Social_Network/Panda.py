from BFS import bfs
import json


def valid_mail(mail):
    if len(mail) > 14 and mail[-14:] == '@pandamail.com':
        return True
    else:
        return False


class Panda:

    def __init__(self, panda_name, mail, sex):
        self.panda_name = panda_name
        if (valid_mail(mail)):
            self.mail = mail
        self.sex = sex

    def name1(self):
        return self.panda_name

    def email(self):
        return self.mail

    def gender(self):
        return self.sex

    def isMale(self):
        return (self.sex == 'male')

    def isFemale(self):
        return (self.sex == 'female')

    def __str__(self):
        return self.panda_name

    def __eq__(self, other):
        return (self.panda_name == other.panda_name and self.mail == other.mail and self.sex == other.sex)

    def __hash__(self):
        return hash(self.mail)

    def __repr__(self):
        return "Panda('{}', '{}', '{}')".format(self.panda_name, self.mail, self.sex)


class PandaSocialNetwork:

    def __init__(self):
        self.panda_list = {}

    def add_panda(self, panda):
        if panda in self.panda_list:
            raise ValueError('PandaAlredyThere')
        else:
            self.panda_list[panda] = []
            return self.panda_list

    def has_panda(self, panda):
        return panda in self.panda_list

    def make_friends(self, panda1, panda2):
        if not self.has_panda(panda1):
            self.add_panda(panda1)
        if not self.has_panda(panda2):
            self.add_panda(panda2)
        (self.panda_list[panda1]).append(panda2)
        (self.panda_list[panda2]).append(panda1)

    def are_friends(self, panda1, panda2):
        if panda1 not in self.panda_list:
            self.add_panda(panda1)
        if panda2 not in self.panda_list:
            self.add_panda(panda2)
        if panda1 in self.panda_list[panda2] and panda2 in self.panda_list[panda1]:
            return True
        else:
            return False

    def friends_of(self, panda):
        if panda in self.panda_list:
            return self.panda_list[panda]
        else:
            return False

    def connection_level(self, panda1, panda2):
        if panda1 not in self.panda_list or panda2 not in self.panda_list:
            return False
        else:
            if (bfs(self.panda_list, panda1, panda2) == 0):
                return -1
            else:
                return (bfs(self.panda_list, panda1, panda2))

    def are_connected(self, panda1, panda2):
        if not self.connection_level(panda1, panda2) or self.connection_level(panda1, panda2) == -1:
            return False
        else:
            return True

    def save(self, path):
        my_dict = {}
        for panda in self.panda_list:
            my_dict[repr(panda)] = []
            for panda_friend in self.panda_list[panda]:
                my_dict[repr(panda)].append(repr(panda_friend))

        json_string = json.dumps(my_dict, indent=4)
        with open(path, "w") as f:
            f.write(json_string)

    def load(self, path):
        my_dict = {}
        with open(path, 'r') as pandas_json_file:
            my_dict = json.load(pandas_json_file)
        for panda in my_dict:
            self.add_panda(eval(panda))
            for panda_friend in my_dict[panda]:
                self.panda_list[eval(panda)].append(eval(panda_friend))
