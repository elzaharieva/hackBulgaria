import sqlite3


conn = sqlite3.connect("company_empl.db")

conn.row_factory = sqlite3.Row
cursor = conn.cursor()


def list_employees():

    result = cursor.execute("SELECT name, position FROM company")
    for row in result:
        print (row['name'], " - ", row['position'])


def monthly_spending():

    result = cursor.execute("SELECT monthly_salary FROM company")
    spending = 0
    for row in result:
        spending += row['monthly_salary']
    return spending


def yearly_spending():

    result = cursor.execute("SELECT yearly_bonus FROM company")
    spending = 12 * monthly_spending()
    for row in result:
        spending += row['yearly_bonus']
    return spending


def add_employee():

    new_name = input("<name>")
    new_monthly_salary = input("<monthly_salary>")
    new_yearly_bonus = input("<yearly_bonus>")
    new_position = input("<position>")
    conn.execute('''INSERT INTO company(name, monthly_salary, yearly_bonus, position) VALUES(?,?,?,?)''',
                 (new_name, new_monthly_salary, new_yearly_bonus, new_position))


def delete_employee():
    employee_id = input("id: ")
    cursor.execute('''DELETE FROM users WHERE id = ? ''', (employee_id,))


def update_employee(self):
    employee_id = input("id: ")
    field = input("Enter field: ")
    field_info = input("Field info: ")
    cursor.execute(
        '''UPDATE company SET {} = ? WHERE id = ? '''.format(field), (field_info, employee_id))


conn.commit()
