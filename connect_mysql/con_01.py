# coding:utf-8
# pip install mysql-connector --target F:\python\venv\lib\site-packages https://pypi.tuna.tsinghua.edu.cn/simple
# 安装指定的第三方包到当前环境目录下，方可通过import 使用
import mysql.connector

config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'waxx153818',
    'database': 'vega',
    'auth_plugin': 'mysql_native_password'
}

con = mysql.connector.connect(**config)
username = '1 or 1 = 1'
password = '1 or 1 = 1'
# 将username当作判断语句执行，无论如何都会返回，形成注入攻击
# sql = "SELECT COUNT(*) FROM t_user WHERE username=" + username + \
#      " AND AES_DECRYPT(UNHEX(password), 'HELLO WORLD')=" + password;
# cur = con.cursor()
# cur.execute(sql)
# data = cur.fetchone()[0]
# print(data)
# con.close()

sql = "SELECT COUNT(*) FROM t_user WHERE username=%s" \
      " AND AES_DECRYPT(UNHEX(password), 'HELLO WORLD')= %s"
cur = con.cursor()
# 通过execute进行预编译，传入的参数将不再进行词法分析，只当作值传入进行比对，则避免了注入攻击
cur.execute(sql, (username, password))
data = cur.fetchone()[0]
print(data)
con.close()