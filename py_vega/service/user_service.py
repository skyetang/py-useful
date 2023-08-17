from db.user_dao import UserDao


class UserService:
    __user_dao = UserDao()

    # 用户登录
    def login(self, username, password):
        res = self.__user_dao.login(username, password)
        return res

    # 查询用户角色
    def search_user_role(self, username):
        role = self.__user_dao.search_user_role(username)
        return role

    # 添加用户
    def insert(self, username, password, email, role_id):
        self.__user_dao.insert(username, password, email, role_id)

    # 查询用户列表
    def search_list(self, page):
        res = self.__user_dao.search_list(page)
        return res

    # 查询用户列表总页数
    def search_count_page(self):
        count_page = self.__user_dao.search_count_page()
        return count_page

    # 修改用户信息
    def update(self, id, username, password, email, role_id):
        self.__user_dao.update(id, username, password, email, role_id)

    # 删除用户
    def delete_by_id(self, id):
        self.__user_dao.delete_by_id(id)
