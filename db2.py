import psycopg2
import pandas as pd
  
conn = psycopg2.connect(database="meetup",
                        user='postgres', password='1234', 
                        host='localhost'
)
  
conn.autocommit = True
cursor = conn.cursor()

encrypted_l =[]
decrypted_l=[]
def encryptfunc(value,encrypted_l,decrypted_l):
    import rsa
    publicKey, privateKey = rsa.newkeys(512)
    for message in value:
        encMessage = rsa.encrypt(message[1].encode(),publicKey)
        encrypted_l.append([message[0],encMessage])

        decMessage = rsa.decrypt(encMessage, privateKey).decode()
        decrypted_l.append([message[0],decMessage])

       
    return encrypted_l,decrypted_l

sql1='''select id,value from meetup_message;'''
cursor.execute(sql1)
value_enc=[]
for i,j in cursor.fetchall():
    value_enc.append([i,str(j)])
#print(value_enc)
encryptfunc(value_enc,encrypted_l,decrypted_l)

  
#sql2 = '''CREATE TABLE Dupli(id int NOT NULL,encrypted_message char(10000),decrypted_message char(10000));'''
#cursor.execute(sql2)
df=pd.read_csv('C:\\Users\\pushp\\Desktop\\csv\\MyDataOutput5.CSV')
l1=list(df['id'])
l2=list(df['encypted_value'])
l3=[]
for i in range(len(l2)):
    l3.append([l1[i],l2[i]])
l4=(sorted(l3, key=lambda x:x[0]))



l5=(sorted(decrypted_l, key=lambda x:x[0]))
print(l5)

 
for i in range(len(l4)):
      cursor.execute("insert into dupli values((%s),(%s),(%s));",(str(l5[i][0]),l4[i][1],l5[i][1]))
for i in range(len(encrypted_l)):
    cursor.execute("update  meetup_message set encypted_value=(%s) where id=(%s);",(encrypted_l[i][1],encrypted_l[i][0]))


sql ='''COPY meetup_message(id,encypted_value,date,room) TO 'C:\\Users\\pushp\\Desktop\\csv\\MyDataOutput10.CSV' DELIMITER ',' CSV HEADER;''' 
cursor.execute(sql)





conn.commit()
conn.close()