import sqlite3

DATABASE = 'db/data.db'

def get_vacancies(name):
    try:
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute("SELECT name,company_name,work_time,salary,department FROM vacancies WHERE name='"+name+"';")
        data = cur.fetchall()
        conn.close()
    except Exception as e:
        return 'SQL:' + str(e)
    return data

def get_all():
    try:
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute("SELECT name,company_name,work_time,salary,department FROM vacancies;")
        data = cur.fetchall()
        conn.close()
    except Exception as e:
        return 'SQL:' + str(e)
    return data