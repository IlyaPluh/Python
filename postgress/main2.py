import psycopg
import names
import secrets
import string
import time

# pip install psycopg2-binary

conn = psycopg.connect(
    dbname = 'qa_ddl_31_28',
    user = 'padawan_user_28',
    password = '24693',
    host = '159.69.151.133',
    port = '5056'
)

cursor = conn.cursor()

user_email = ''
user_password = '' 
user_name = '' 
user_phone = '' 

user_data_list = []
letters = string.ascii_letters
digits = string.digits
alphabet = letters + digits
pwd_length = 12

for i in range(0,50):
    
    if conn:
    
        pwd = ''
        phn = '+'
        for i in range(pwd_length):
            pwd += ''.join(secrets.choice(alphabet))
            phn += ''.join(secrets.choice(digits))
        
        user_name = names.get_full_name()
        user_email = user_name.replace(' ', '.') + '@gmail.com'
        user_password = pwd
        user_phone = phn
        
        based_data = (user_email, user_password, user_phone, user_name)
        
        insert_query = """ insert into public.users(email, password_field, phone, user_name) values(%s, %s, %s, %s) """
        
        cursor.execute(insert_query, based_data)
        conn.commit()

        print(based_data)
        time.sleep(.100)
        
        
# truncate_query = 'truncate public.users'
# cursor.execute(truncate_query)
# conn.commit()


cursor.close()
    