import mysql.connector
import cplex
import cplex.exceptions

config = {
    'user': 'belgrades',
    'password': '230190fc',
    'host': '127.0.0.1',
    'database': 'mlb',
    'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)

cursor = cnx.cursor()

query = ("SELECT * FROM teams LIMIT 10")

cursor.execute(query)

for i in cursor:
    print(i)


cnx.close()


