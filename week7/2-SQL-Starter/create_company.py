import sqlite3

conn = sqlite3.connect("company_empl.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS company(id INTEGER PRIMARY KEY, name TEXT,
                   monthly_salary INTEGER, yearly_bonus INTEGER, position TEXT)
""")

conn.execute('''INSERT INTO company(name, monthly_salary, yearly_bonus, position) VALUES(?,?,?,?)''',
             ("Ivan Ivanov", 5000, 10000, "Software Developer"))
conn.execute('''INSERT INTO company(name, monthly_salary, yearly_bonus, position) VALUES(?,?,?,?)''',
             ("Rado Rado", 500, 0, "Technical Support Intern"))
conn.execute('''INSERT INTO company(name, monthly_salary, yearly_bonus, position) VALUES(?,?,?,?)''',
             ("Ivo Ivo", 10000, 100000, "CEO"))
conn.execute('''INSERT INTO company(name, monthly_salary, yearly_bonus, position) VALUES(?,?,?,?)''',
             ("Petar Petrov", 3000, 1000, "Marketing Manager"))
conn.execute('''INSERT INTO company(name, monthly_salary, yearly_bonus, position) VALUES(?,?,?,?)''',
             ("Maria Georgieva", 8000, 10000, "COO"))

conn.commit()
