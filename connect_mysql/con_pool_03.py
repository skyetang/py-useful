import mysql.connector.pooling

config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'waxx153818',
    'database': 'demo',
    'auth_plugin': 'mysql_native_password'
}
# 通过建立数据库连接池，在每次需要执行数据库的时候，则调用已创建好的连接使用即可，不用每次都重新创建连接（每次单独创建效率较低）
# 从而提高使用效率
try:
    connect_pool = mysql.connector.pooling.MySQLConnectionPool(
        **config,
        pool_size=10
    )
    con = connect_pool.get_connection()
    con.start_transaction()
    cur = con.cursor()
    sql = 'UPDATE t_emp SET sal=sal+%s WHERE deptno=%s'
    cur.execute(sql, (200, 20))
    con.commit()
except Exception as e:
    if 'con' in dir():
        con.rollback()
    print(e)