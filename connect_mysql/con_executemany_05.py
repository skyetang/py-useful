import mysql.connector.pooling

conifg = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'waxx153818',
    'database': 'demo',
    'auth_plugin': 'mysql_native_password'
}

try:
    pool = mysql.connector.pooling.MySQLConnectionPool(
        **conifg,
        pool_size=10
    )
    con = pool.get_connection()
    con.start_transaction()
    cur = con.cursor()
    sql = 'INSERT INTO t_dept(deptno, dname, loc) VALUES (%s, %s, %s)'
    data = [
        ['100', 'A部门', '北京'], ['110', 'B部门', '上海']
    ]
    # 通过传入的数据列表，来判断SQL语句执行多少次
    cur.executemany(sql, data)
    con.commit()
except Exception as e:
    if 'con' in dir():
        con.rollback()
    print(e)