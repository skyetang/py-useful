import mysql.connector.pooling

config={
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'waxx153818',
    'database': 'demo',
    'auth_plugin': 'mysql_native_password'
}
try:
    pool = mysql.connector.pooling.MySQLConnectionPool(
        **config,
        pool_size=10
    )
    con = pool.get_connection()
    con.start_transaction()
    cursor = con.cursor()
    sql = 'DELETE e,d FROM t_emp e JOIN t_dept d ON e.deptno = d.deptno WHERE d.deptno = 20 '
    # sql = 'TRUNCATE TABLE t_emp'
    cursor.execute(sql)
    con.commit()
except Exception as e:
    print(e)
