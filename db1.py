
import psycopg2
conn = psycopg2.connect(database="meetup",
                        user='postgres', password='1234', 
                        host='localhost'
)
conn.autocommit = True
cursor = conn.cursor()
sql1='''select value from meetup_message;'''
cursor.execute(sql1)
value_enc=[]

for i in cursor.fetchall():
    value_enc.append(str(i))
print(value_enc)
conn.commit()
conn.close()