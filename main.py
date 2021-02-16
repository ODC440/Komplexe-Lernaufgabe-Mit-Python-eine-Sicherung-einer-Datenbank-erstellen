import pymysql
import subprocess
from subprocess import Popen, PIPE, STDOUT

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='1234', db='db1')
cur = conn.cursor()

print("Attempting to create new database...")
try:
    cur.execute("CREATE DATABASE Project_Test2")
    print("Creating new database")
except Exception:
    print("Database already exists")
print()

# close connection just to be sure
cur.close()
conn.close()

print("Trying to copy old database to new database...")

subprocess.Popen('mysqldump -h localhost -P 3306 -u -root --column-statistics=0 db1 | mysql -h localhost -P 3306 -u root Project_Test3' , shell=True)

print("output:")
print(output)
