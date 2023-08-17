from db.mysql_db import pool


class RoleDao:
    def search_list(self):
        try:
            con = pool.get_connection()
            cur = con.cursor()
            sql = 'SELECT id,role FROM t_role'
            cur.execute(sql)
            res = cur.fetchall()
            return res
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()

