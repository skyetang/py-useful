from db.mysql_db import pool

class UserDao:
    # 验证用户登录
    def login(self, username, password):
        try:
            con = pool.get_connection()
            cur = con.cursor()
            sql = 'SELECT COUNT(*) FROM t_user WHERE username=%s ' \
                  'AND AES_DECRYPT(UNHEX(password), "HELLOWORLD")=%s'
            cur.execute(sql,(username, password))
            count = cur.fetchone()[0]
            return True if count == 1 else False
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()
    # 查询用户角色
    def search_user_role(self, username):
        try:
            con = pool.get_connection()
            cur = con.cursor()
            sql = 'SELECT r.role FROM t_user u JOIN t_role r ' \
                  'ON u.role_id = r.id WHERE u.username = %s'
            cur.execute(sql, [username])
            role = cur.fetchone()[0]
            return role
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    # 添加用户
    def insert(self, username, password, email, role_id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cur = con.cursor()
            sql = 'INSERT INTO t_user(username, password, email, role_id) VALUES(%s, HEX(AES_ENCRYPT(%s, "HELLOWORLD")), %s, %s)'
            cur.execute(sql, (username, password, email, role_id))
            con.commit()
        except Exception as e:
            if 'con' in dir():
                con.rollback()
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    # 查询用户列表
    def search_list(self, page):
        try:
            con = pool.get_connection()
            cur = con.cursor()
            sql = 'SELECT u.id,u.username,r.role ' \
                  'FROM t_user u JOIN t_role r ' \
                  'ON u.role_id = r.id ' \
                  'ORDER BY u.id ' \
                  'LIMIT %s,%s'
            cur.execute(sql, ((page-1)*10, 10))
            res = cur.fetchall()
            return res
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    # 查询用户列表总页数
    def search_count_page(self):
        try:
            con = pool.get_connection()
            cur = con.cursor()
            sql = 'SELECT CEIL(COUNT(*)/10) FROM t_user'
            cur.execute(sql)
            count_page = cur.fetchone()[0]
            return count_page
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    # 修改用户信息
    def update(self, id, username, password, email, role_id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cur = con.cursor()
            sql = 'UPDATE t_user SET username=%s, password=HEX(AES_ENCRYPT(%s, "HELLOWORLD")), email = %s, role_id=%s WHERE id = %s'
            cur.execute(sql, (username, password, email, role_id, id))
            con.commit()
        except Exception as e:
            if 'con' in dir():
                con.rollback()
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    # 删除用户
    def delete_by_id(self, id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cur = con.cursor()
            sql = 'DELETE FROM t_user WHERE id=%s'
            cur.execute(sql, [id])
            con.commit()
        except Exception as e:
            if 'con' in dir():
                con.rollback()
            print(e)
        finally:
            if 'con' in dir():
                con.close()