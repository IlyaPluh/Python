import psycopg2
# pip install psycopg2-binary
conn = psycopg2.connect(
    dbname = 'qa_ddl_31_28',
    user = 'padawan_user_28',
    password = '24693',
    host = '159.69.151.133',
    port = '5056'
)

cursor = conn.cursor()

if conn:
    print('Connection true')
    sql_req = '''select * from salary'''
    cursor.execute(sql_req)
    
    req_res = cursor.fetchall()
    
    print(cursor.description[1][0])
    print(req_res)
    
    for i in req_res:
        print('id =', i[0], 'salary =', i[1])
        
    conn.commit()
    conn.close()
    