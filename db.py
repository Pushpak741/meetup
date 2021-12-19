
import psycopg2
import pandas as pd
  
conn = psycopg2.connect(database="meetup",
                        user='postgres', password='1234', 
                        host='localhost'
)
  
conn.autocommit = True
cursor = conn.cursor()
'''df=pd.read_csv('C:\\Users\\pushp\\Desktop\\csv\\MyDataOutput2.CSV')
l=list(df['value'])
print(l)'''
encrypted_l =[]
def encryptfunc(value,encrypted_l):
    import rsa
    publicKey, privateKey = rsa.newkeys(512)
    for message in value:
        encMessage = rsa.encrypt(message.encode(),publicKey)
        encrypted_l.append(encMessage)
    return encrypted_l
decrypted_l=[]
def decryptfunc(encrypted_l,decrypted_l):
    import rsa
    publicKey, privateKey = rsa.newkeys(512)
    for message in encrypted_l:
        decMessage = rsa.decrypt(message, privateKey).decode()
        decrypted_l.append(decMessage)
    return decrypted_l

    

#sql2='''alter table meetup_message add column encypted_value varchar ;'''
sql1='''select value from meetup_message;'''
#cursor.execute(sql2)
cursor.execute(sql1)
value_enc=[]
'''for i in cursor.fetchall():
    print(i)'''
for i in cursor.fetchall():
    value_enc.append(str(i))
encryptfunc(value_enc,encrypted_l)
sql2='''select encypted_value from meetup_message;'''
cursor.execute(sql2)
enc_value=[]
for i in cursor.fetchall():
    enc_value.append(i)
decryptfunc(enc_value,decrypted_l)
print(decrypted_l)

for i in range(len(encrypted_l)):
   cursor.execute("update  meetup_message set encypted_value=(%s) where id=(%s);",(encrypted_l[i],i+1))
#sql2='''select * from meetup_message'''
#cursor.execute(sql2)
#for i in cursor.fetchall():
 #   print(i)
#sql ='''COPY meetup_message TO 'C:\\Users\\pushp\\Desktop\\csv\\MyDataOutput2.CSV' DELIMITER ',' CSV HEADER;'''  
#cursor.execute("COPY meetup_message FROM 'C:\\Users\\pushp\\Desktop\\csv\\MyDataOutput2.CSV' DELIMITER ',' CSV HEADER;")
#cursor.execute("select * from meetup_message;")

'''for i in cursor.fetchall():
    print(i)
  '''
conn.commit()
conn.close()