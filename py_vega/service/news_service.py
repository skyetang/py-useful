from db.news_dao import NewsDao


class NewsService:
    __news_dao = NewsDao()

    # 查询未审批新闻列表
    def search_unreview_list(self, page):
        res = self.__news_dao.search_unreview_list(page)
        return res

    # 查询未审批新闻总页数
    def search_unreview_count_page(self):
        res = self.__news_dao.search_unreview_count_page()
        return res

    # 审批新闻
    def update_unreview_news(self, id):
        self.__news_dao.update_unreview_news(id)

    # 查询所有新闻列表
    def search_list(self, page):
        res = self.__news_dao.search_list(page)
        return res

    # 删除新闻
    def delete_by_id(self, id):
        self.__news_dao.delete_by_id(id)

    # 查询新闻列表总页数
    def search_count_page(self):
        count_page = self.__news_dao.search_count_page()
        return count_page