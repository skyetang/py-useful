# 编写一个INSERT语句，向部门表插入两条记录，每条记录都在部门原有最大主键值的基础上+10
import mysql.connector.pooling

config = {
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
    cur = con.cursor()
    sql = 'INSERT INTO t_dept (SELECT MAX(deptno)+10, %s, %s FROM t_dept ' \
          'UNION SELECT MAX(deptno)+20, %s, %s FROM t_dept)'
    cur.execute(sql, ('A部门', '北京', 'B部门', '成都'))
    con.commit()
except Exception as e:
    print(e)