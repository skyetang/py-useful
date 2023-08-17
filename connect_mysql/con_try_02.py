import mysql.connector

try:
    con = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='waxx153818',
        database='demo',
        auth_plugin='mysql_native_password'
    )
    con.start_transaction()
    cur = con.cursor()
    sql = 'INSERT INTO t_emp(empno,ename,job,mgr,hiredate,sal,comm,deptno) ' \
          'VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'
    cur.execute(sql, (9600, 'nana', 'SALESMAN', None, '1985-12-1', 2500, None, 10))
    con.commit()
except Exception as e:
    if 'con' in dir():
        con.rollback()
    print(e)
finally:
    if 'con' in dir():
        con.close()