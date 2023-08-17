import mysql.connector.pooling

config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'waxx153818',
    'database': 'demo',
    'auth_plugin': 'mysql_native_password'
}

pool = mysql.connector.pooling.MySQLConnectionPool(
    **config,
    pool_size=10
)
con = pool.get_connection()
cur = con.cursor()
sql = 'select * from t_dept'
cur.execute(sql)
res = cur.fetchall()
print(res)
