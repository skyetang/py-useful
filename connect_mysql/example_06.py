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
        pool_size = 10
    )
    con = pool.get_connection()
    con.start_transaction()
    cur = con.cursor()
    sql = 'DROP TABLE t_emp_new'
    cur.execute(sql)
    # 创建一个新表，和t_emp的表结构及数据相同
    # sql = 'CREATE TABLE t_emp_new AS (SELECT * FROM t_emp)'
    # 创建一个新表，和t_emp的表结构，只要表结构不要数据
    sql = 'CREATE TABLE t_emp_new LIKE t_emp'
    cur.execute(sql)
    # 使用INSERT语句，把部门平均底薪超过公司平均底薪的员工信息导入到t_emp_new 表中，并且让这些员工隶属于sales部门
    sql = 'SELECT AVG(sal) as avg FROM t_emp'
    cur.execute(sql)
    avg_data = cur.fetchone()[0]
    sql = 'SELECT deptno FROM t_emp GROUP BY deptno HAVING AVG(sal) >= %s'
    cur.execute(sql, [avg_data])
    tem_deptno = cur.fetchall()
    sql = 'INSERT INTO t_emp_new SELECT * FROM t_emp WHERE deptno IN ('
    for index in range(len(tem_deptno)):
        if index < len(tem_deptno)-1:
            sql += str(tem_deptno[index][0]) + ','
        else:
            sql += str(tem_deptno[index][0])
    sql += ')'
    cur.execute(sql)
    sql = 'DELETE FROM t_emp WHERE deptno IN('
    for index in range(len(tem_deptno)):
        if index < len(tem_deptno)-1:
            sql += str(tem_deptno[index][0]) + ','
        else:
            sql += str(tem_deptno[index][0])
    sql += ')'
    cur.execute(sql)
    sql = 'SELECT deptno FROM t_dept WHERE dname=%s'
    cur.execute(sql, ['SALES'])
    tem_dept = cur.fetchone()[0]
    print(tem_dept)
    sql = 'UPDATE t_emp_new SET deptno=%s'
    cur.execute(sql, [tem_dept])
    con.commit()
except Exception as e:
    print(e)