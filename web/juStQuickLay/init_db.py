import sqlite3

DATABASE = 'db/data.db'

conn = sqlite3.connect(DATABASE)
cur = conn.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS vacancies(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name TEXT NOT NULL,
    company_name TEXT NOT NULL,
    work_time TEXT NOT NULL,
    salary TEXT NOT NULL,
    department TEXT NOT NULL);""")

cur.execute("""CREATE TABLE IF NOT EXISTS nosecret_table(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name TEXT NOT NULL,
    flag TEXT NOT NULL,
    description TEXT NOT NULL);""")
cur.execute("INSERT INTO vacancies (name,company_name,work_time,salary,department) VALUES ('Marketing & Communication Supervisor','ReCorp','Part-Time','30','Marketing');")
cur.execute("INSERT INTO vacancies (name,company_name,work_time,salary,department) VALUES ('UX Designer & UI Developer','ISCorp','Full-Time','90','Design');")
cur.execute("INSERT INTO vacancies (name,company_name,work_time,salary,department) VALUES ('Information Security Analyst / Expert','ITGigant','Part-Time','20','Infra Supervision');")
cur.execute("INSERT INTO vacancies (name,company_name,work_time,salary,department) VALUES ('Information Security Analyst / Expert','InfoSecIT','Part-Time','10','Infra Supervision');")
cur.execute("INSERT INTO vacancies (name,company_name,work_time,salary,department) VALUES ('Information Security Analyst / Expert','GameDevIT','Part-Time','30','Infra Supervision');")
cur.execute("INSERT INTO vacancies (name,company_name,work_time,salary,department) VALUES ('Senior Software Engineer / Developer','ITipa','Part-Time','20','Software Development');")
cur.execute("INSERT INTO vacancies (name,company_name,work_time,salary,department) VALUES ('Senior Data Analyst / Scientist','GameDevIT','Full-Time','50','Artificial Intelligence');")
cur.execute("INSERT INTO vacancies (name,company_name,work_time,salary,department) VALUES ('UX Designer & UI Developer','ISCorp','Full-Time','60','Design');")
cur.execute("INSERT INTO vacancies (name,company_name,work_time,salary,department) VALUES ('Senior Data Analyst / Scientist','ReCorp','Full-Time','90','Artificial Intelligence');")
cur.execute("INSERT INTO vacancies (name,company_name,work_time,salary,department) VALUES ('Senior Software Engineer / Developer','FinSec','Full-Time','50','Software Development');")
cur.execute("INSERT INTO vacancies (name,company_name,work_time,salary,department) VALUES ('Information Security Analyst / Expert','InfoSecIT','Part-Time','40','Infra Supervision');")
cur.execute("INSERT INTO vacancies (name,company_name,work_time,salary,department) VALUES ('Marketing & Communication Supervisor','JBK','Full-Time','60','Marketing');")
cur.execute("INSERT INTO vacancies (name,company_name,work_time,salary,department) VALUES ('UX Designer & UI Developer','ISCorp','Full-Time','70','Design');")
cur.execute("INSERT INTO vacancies (name,company_name,work_time,salary,department) VALUES ('Information Security Analyst / Expert','StartUP','Full-Time','70','Infra Supervision');")
cur.execute("INSERT INTO vacancies (name,company_name,work_time,salary,department) VALUES ('Marketing & Communication Supervisor','YaSearch','Part-Time','20','Marketing');")
cur.execute("INSERT INTO vacancies (name,company_name,work_time,salary,department) VALUES ('Senior Software Engineer / Developer','QwertySecure','Full-Time','60','Software Development');")
cur.execute("INSERT INTO vacancies (name,company_name,work_time,salary,department) VALUES ('Information Security Analyst / Expert','InfoSecIT','Part-Time','30','Infra Supervision');")
cur.execute("INSERT INTO vacancies (name,company_name,work_time,salary,department) VALUES ('Information Security Analyst / Expert','LookUp','Part-Time','20','Infra Supervision');")
cur.execute("INSERT INTO vacancies (name,company_name,work_time,salary,department) VALUES ('Marketing & Communication Supervisor','ITipa','Part-Time','30','Marketing');")
cur.execute("INSERT INTO vacancies (name,company_name,work_time,salary,department) VALUES ('Information Security Analyst / Expert','StartUP','Part-Time','20','Infra Supervision');")
cur.execute("INSERT INTO vacancies (name,company_name,work_time,salary,department) VALUES ('Marketing & Communication Supervisor','JBK','Part-Time','30','Marketing');")
cur.execute("INSERT INTO vacancies (name,company_name,work_time,salary,department) VALUES ('Senior Software Engineer / Developer','IT-Company','Part-Time','20','Software Development');")
cur.execute("INSERT INTO vacancies (name,company_name,work_time,salary,department) VALUES ('Information Security Analyst / Expert','QwertySecure','Part-Time','20','Infra Supervision');")
cur.execute("INSERT INTO vacancies (name,company_name,work_time,salary,department) VALUES ('Senior Software Engineer / Developer','GameDevIT','Full-Time','70','Software Development');")
cur.execute("INSERT INTO vacancies (name,company_name,work_time,salary,department) VALUES ('Information Security Analyst / Expert','QwertySecure','Full-Time','70','Infra Supervision');")
cur.execute("INSERT INTO vacancies (name,company_name,work_time,salary,department) VALUES ('Senior Data Analyst / Scientist','YaSearch','Part-Time','30','Artificial Intelligence');")
cur.execute("INSERT INTO vacancies (name,company_name,work_time,salary,department) VALUES ('Senior Software Engineer / Developer','IT-Company','Full-Time','60','Software Development');")
cur.execute("INSERT INTO vacancies (name,company_name,work_time,salary,department) VALUES ('Information Security Analyst / Expert','IT-Company','Part-Time','40','Infra Supervision');")
cur.execute("INSERT INTO vacancies (name,company_name,work_time,salary,department) VALUES ('Senior Software Engineer / Developer','YaSearch','Full-Time','50','Software Development');")
cur.execute("INSERT INTO vacancies (name,company_name,work_time,salary,department) VALUES ('Senior Software Engineer / Developer','ISCorp','Full-Time','100','Software Development');")
cur.execute("INSERT INTO vacancies (name,company_name,work_time,salary,department) VALUES ('UX Designer & UI Developer','ITipa','Part-Time','30','Design');")
cur.execute("INSERT INTO vacancies (name,company_name,work_time,salary,department) VALUES ('Senior Software Engineer / Developer','StartUP','Full-Time','100','Software Development');")
cur.execute("INSERT INTO vacancies (name,company_name,work_time,salary,department) VALUES ('Marketing & Communication Supervisor','ITipa','Part-Time','10','Marketing');")
cur.execute("INSERT INTO vacancies (name,company_name,work_time,salary,department) VALUES ('Senior Data Analyst / Scientist','ITGigant','Full-Time','80','Artificial Intelligence');")
cur.execute("INSERT INTO vacancies (name,company_name,work_time,salary,department) VALUES ('Information Security Analyst / Expert','QwertySecure','Full-Time','70','Infra Supervision');")
cur.execute("INSERT INTO vacancies (name,company_name,work_time,salary,department) VALUES ('Senior Software Engineer / Developer','GameDevIT','Part-Time','20','Software Development');")
cur.execute("INSERT INTO vacancies (name,company_name,work_time,salary,department) VALUES ('Marketing & Communication Supervisor','IT-Company','Part-Time','40','Marketing');")
cur.execute("INSERT INTO vacancies (name,company_name,work_time,salary,department) VALUES ('Senior Software Engineer / Developer','JBK','Part-Time','20','Software Development');")
cur.execute("INSERT INTO vacancies (name,company_name,work_time,salary,department) VALUES ('Marketing & Communication Supervisor','GameDevIT','Full-Time','90','Marketing');")
cur.execute("INSERT INTO vacancies (name,company_name,work_time,salary,department) VALUES ('UX Designer & UI Developer','FinSec','Full-Time','70','Design');")
cur.execute("INSERT INTO vacancies (name,company_name,work_time,salary,department) VALUES ('Marketing & Communication Supervisor','FinSec','Full-Time','50','Marketing');")
cur.execute("INSERT INTO vacancies (name,company_name,work_time,salary,department) VALUES ('Senior Data Analyst / Scientist','ITGigant','Part-Time','10','Artificial Intelligence');")
cur.execute("INSERT INTO vacancies (name,company_name,work_time,salary,department) VALUES ('Senior Data Analyst / Scientist','LookUp','Part-Time','20','Artificial Intelligence');")
cur.execute("INSERT INTO vacancies (name,company_name,work_time,salary,department) VALUES ('Senior Software Engineer / Developer','YaSearch','Full-Time','80','Software Development');")
cur.execute("INSERT INTO vacancies (name,company_name,work_time,salary,department) VALUES ('Information Security Analyst / Expert','ISCorp','Full-Time','90','Infra Supervision');")
cur.execute("INSERT INTO vacancies (name,company_name,work_time,salary,department) VALUES ('Information Security Analyst / Expert','ITGigant','Full-Time','100','Infra Supervision');")
cur.execute("INSERT INTO vacancies (name,company_name,work_time,salary,department) VALUES ('Senior Data Analyst / Scientist','InfoSecIT','Full-Time','90','Artificial Intelligence');")
cur.execute("INSERT INTO vacancies (name,company_name,work_time,salary,department) VALUES ('Senior Software Engineer / Developer','JBK','Full-Time','90','Software Development');")
cur.execute("INSERT INTO vacancies (name,company_name,work_time,salary,department) VALUES ('Marketing & Communication Supervisor','InfoSecIT','Part-Time','40','Marketing');")
cur.execute("INSERT INTO vacancies (name,company_name,work_time,salary,department) VALUES ('Information Security Analyst / Expert','JBK','Part-Time','20','Infra Supervision');")
cur.execute("INSERT INTO nosecret_table (name,flag,description) VALUES ('Secret','flag{SQL_1NJ3ct10N_1n_s34Rch_f13Ld}','Поздравляю! Вы смогли найти флаг с помощью SQL Injection.');")
conn.commit()
conn.close()
