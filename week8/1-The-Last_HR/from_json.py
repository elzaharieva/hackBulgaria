import sqlite3
from needleInHaystack import count_substrings
from create_cources_table_connection import conn2

cursor2 = conn2.cursor()


def loading():
    with open("request_for_hack_bulgaria.json", 'r') as fp:
        text = fp.read()
        fp.close()
        text.strip(' ')
        text = text[:-1]
        text.strip(' ')
        text = list(text.split('}, {\\"gi'))
        for t in text[1:]:
            t = '{\"gi' + t + '}'
            t.strip(' ')
            t = list(t.split(':'))
            real_d = {}
            real_d['github'] = t[1] + t[2]
            real_d['github'] = real_d['github'][:-15]
            real_d['github'] = str(real_d['github'])
            real_d['name'] = t[4][:-13]
            real_d['name'] = str(real_d['name'])
            cources = str(t[5:])
            real_d['cources'] = []
            if count_substrings(cources, "Programming 101 v2") > 0:
                real_d['cources'].append("Programming 101 v2")
            if count_substrings(cources, "Android") > 0:
                real_d['cources'].append("Android")
            if count_substrings(cources, "NodeJS") > 0:
                real_d['cources'].append("NodeJS")
            if count_substrings(cources, "Core Java v2") > 0:
                real_d['cources'].append("Core Java v2")
            else:
                if count_substrings(cources, 'Core Java') > 0:
                    real_d['cources'].append("Core Java")
            if count_substrings(cources, "Frontend JavaScript v2") > 0:
                real_d['cources'].append("Frontend JavaScript v2")
            elif count_substrings(cources, "Frontend JavaScript v3") > 0:
                real_d['cources'].append("Frontend JavaScript v3")
            else:
                if count_substrings(cources, 'Frontend JavaScript') > 0:
                    real_d['cources'].append("Frontend JavaScript")
            if count_substrings(cources, "System C") > 0:
                real_d['cources'].append("System C")
            if count_substrings(cources, "Programming 101 v3") > 0:
                real_d['cources'].append("Programming 101 v3")
            if count_substrings(cources, "Ruby on Rails") > 0:
                real_d['cources'].append("Ruby on Rails")
            if count_substrings(cources, "Core Ruby") > 0:
                real_d['cources'].append("Core Ruby")
            if count_substrings(cources, "u041f") > 0:
                real_d['cources'].append("Programming 0")
            student_name = str(real_d['name'])
            student_account = str(real_d['github'])
            conn2.execute(
                '''INSERT INTO students(name, profile) VALUES(?,?)''', (student_name, student_account))
            st_id = conn2.execute(
                '''SELECT id FROM students WHERE name = ? ''', (student_name, ))
            r = st_id.fetchone()
            if r['id'] != 1:
                for c in real_d['cources']:
                    c_id = conn2.execute(
                        '''SELECT id FROM cources WHERE name = ? ''', (c, ))
                    rr = c_id.fetchone()
                    conn2.execute(
                        '''INSERT INTO relations(student_id, course_id) VALUES(?,?)''', (r['id'], rr['id']))


if __name__ == "__mein__":
    mein()
