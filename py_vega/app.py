from colorama import Fore, Style
from getpass import getpass
from service.user_service import UserService
from service.news_service import NewsService
from service.role_service import RoleService
import os
import sys
import time

__user_service = UserService()
__news_service = NewsService()
__role_service = RoleService()

while True:
    print(Fore.LIGHTBLUE_EX, '=============')
    print(Fore.LIGHTBLUE_EX, '欢迎使用新闻管理系统')
    print(Fore.LIGHTBLUE_EX, '=============')
    print(Fore.LIGHTGREEN_EX, '1.登陆系统')
    print(Fore.LIGHTGREEN_EX, '2.退出系统')
    print(Style.RESET_ALL)
    opt = input('请输入操作指令：')
    if opt == '1':
        username = input('请输入用户名：')
        password = getpass('请输入密码：')
        login_res = __user_service.login(username, password)
        # 登录成功
        if login_res:
            role = __user_service.search_user_role(username)
            while True:
                os.system('clear')
                if role == '管理员':
                    print(Fore.LIGHTBLUE_EX, '1.新闻管理')
                    print(Fore.LIGHTBLUE_EX, '2.用户管理')
                    print(Fore.LIGHTBLUE_EX, 'back:退出登陆')
                    print(Fore.LIGHTBLUE_EX, 'exit:退出系统')
                    print(Style.RESET_ALL)
                    opt = input('请输入操作指令：')
                    if opt == '1':
                        while True:
                            os.system('clear')
                            print(Fore.LIGHTBLUE_EX, '1.审批新闻')
                            print(Fore.LIGHTBLUE_EX, '2.删除新闻')
                            print(Fore.LIGHTBLUE_EX, 'back.返回上一级')
                            print(Style.RESET_ALL)
                            opt = input('请输入操作指令：')
                            if opt == '1':
                                page = 1
                                while True:
                                    os.system('clear')
                                    news_list = __news_service.search_unreview_list(page)
                                    count_page = __news_service.search_unreview_count_page()
                                    for index in range(len(news_list)):
                                        list = news_list[index]
                                        print(Fore.LIGHTBLUE_EX, '%d:%s \t %s \t %s' % (index+1, list[1], list[2], list[3]))
                                    print(Fore.LIGHTBLUE_EX, '%d / %d' % (page, count_page))
                                    print(Fore.LIGHTBLUE_EX, '-----------------------')
                                    print(Fore.LIGHTGREEN_EX, 'back.返回上一层')
                                    print(Fore.LIGHTGREEN_EX, 'prev.上一页')
                                    print(Fore.LIGHTGREEN_EX, 'next.下一页')
                                    print(Style.RESET_ALL)
                                    opt = input('请输入操作指令：')
                                    if opt == 'back':
                                        break
                                    elif opt == 'prev' and page > 1:
                                        page -= 1
                                    elif opt == 'next' and page < count_page:
                                        page += 1
                                    elif 1 <= int(opt) <= len(news_list):
                                        target_id = news_list[int(opt)-1][0]
                                        __news_service.update_unreview_news(target_id)
                            elif opt == '2':
                                page = 1
                                while True:
                                    os.system('clear')
                                    news_list = __news_service.search_list(page)
                                    count_page = __news_service.search_count_page()
                                    for index in range(len(news_list)):
                                        list = news_list[index]
                                        print(Fore.LIGHTBLUE_EX, '%d:%s \t %s \t %s' % (index+1, list[1], list[2], list[3]))
                                    print(Fore.LIGHTBLUE_EX, '%d / %d' % (page, count_page))
                                    print(Fore.LIGHTBLUE_EX, '-----------------------')
                                    print(Fore.LIGHTGREEN_EX, 'back.返回上一层')
                                    print(Fore.LIGHTGREEN_EX, 'prev.上一页')
                                    print(Fore.LIGHTGREEN_EX, 'next.下一页')
                                    print(Style.RESET_ALL)
                                    opt = input('请输入操作指令：')
                                    if opt == 'back':
                                        break
                                    elif opt == 'prev' and page > 1:
                                        page -= 1
                                    elif opt == 'next' and page < count_page:
                                        page += 1
                                    elif 1 <= int(opt) <= len(news_list):
                                        target_id = news_list[int(opt)-1][0]
                                        __news_service.delete_by_id(target_id)
                            elif opt =='back':
                                break
                    elif opt == '2':
                        while True:
                            os.system('clear')
                            print(Fore.LIGHTBLUE_EX, '1.添加用户')
                            print(Fore.LIGHTBLUE_EX, '2.修改用户')
                            print(Fore.LIGHTBLUE_EX, '3.删除用户')
                            print(Fore.LIGHTBLUE_EX, 'back.返回上一级')
                            print(Style.RESET_ALL)
                            opt = input('请输入操作指令：')
                            if opt == '1':
                                print('------请输入新用户信息-----')
                                username = input('用户名:')
                                password = getpass('密码：')
                                repassword = getpass('重复密码：')
                                if password != repassword:
                                    print(Fore.LIGHTRED_EX, '两次密码不一致，3S后自动返回')
                                    time.sleep(3)
                                    continue
                                email = input('邮箱：')
                                role_list = __role_service.search_list()
                                for index in range(len(role_list)):
                                    list = role_list[index]
                                    print(Fore.LIGHTBLUE_EX, '%d.%s' % (index+1, list[1]))
                                print(Style.RESET_ALL)
                                opt_role = input('选择角色：')
                                role_id = role_list[int(opt_role)-1][0]
                                __user_service.insert(username, password, email, role_id)
                                print(Fore.LIGHTGREEN_EX, '添加成功，3S后自动返回')
                                time.sleep(3)
                                continue
                            elif opt == '2':
                                page = 1
                                while True:
                                    os.system('clear')
                                    user_list = __user_service.search_list(page)
                                    count_page = __user_service.search_count_page()
                                    for index in range(len(user_list)):
                                        list = user_list[index]
                                        print(Fore.LIGHTBLUE_EX, '%d.%s \t %s' % ((index+1), list[1], list[2]))
                                    print(Fore.LIGHTBLUE_EX, '%d/%d' % (page, count_page))
                                    print(Fore.LIGHTBLUE_EX, '-----------------------')
                                    print(Fore.LIGHTGREEN_EX, 'back.返回上一层')
                                    print(Fore.LIGHTGREEN_EX, 'prev.上一页')
                                    print(Fore.LIGHTGREEN_EX, 'next.下一页')
                                    print(Style.RESET_ALL)
                                    opt = input('请输入操作指令：')
                                    if opt == 'back':
                                        break
                                    elif opt == 'prev' and page > 1:
                                        page -= 1
                                    elif opt == 'next' and page < count_page:
                                        page += 1
                                    elif 1 <= int(opt) <= len(user_list):
                                        os.system('clear')
                                        print('------请输入新用户信息-----')
                                        username = input('用户名:')
                                        password = getpass('密码：')
                                        repassword = getpass('重复密码：')
                                        if password != repassword:
                                            print(Fore.LIGHTRED_EX, '两次密码不一致，3S后自动返回')
                                            time.sleep(3)
                                            continue
                                        email = input('邮箱：')
                                        role_list = __role_service.search_list()
                                        for index in range(len(role_list)):
                                            list = role_list[index]
                                            print(Fore.LIGHTBLUE_EX, '%d.%s' % (index + 1, list[1]))
                                        print(Style.RESET_ALL)
                                        opt_role = input('选择角色：')
                                        role_id = role_list[int(opt_role) - 1][0]
                                        is_save = input('是否保存 Y / N：')
                                        if is_save == 'Y' or is_save == 'y':
                                            user_id = user_list[int(opt)-1][0]
                                            __user_service.update(user_id, username, password, email, role_id)
                                            print(Fore.LIGHTGREEN_EX, '修改成功，3S后自动返回')
                                            time.sleep(3)
                                            continue
                            elif opt == '3':
                                page = 1
                                while True:
                                    os.system('clear')
                                    user_list = __user_service.search_list(page)
                                    count_page = __user_service.search_count_page()
                                    for index in range(len(user_list)):
                                        list = user_list[index]
                                        print(Fore.LIGHTBLUE_EX, '%d.%s \t %s' % ((index + 1), list[1], list[2]))
                                    print(Fore.LIGHTBLUE_EX, '%d/%d' % (page, count_page))
                                    print(Fore.LIGHTBLUE_EX, '-----------------------')
                                    print(Fore.LIGHTGREEN_EX, 'back.返回上一层')
                                    print(Fore.LIGHTGREEN_EX, 'prev.上一页')
                                    print(Fore.LIGHTGREEN_EX, 'next.下一页')
                                    print(Style.RESET_ALL)
                                    opt = input('请输入操作指令：')
                                    if opt == 'back':
                                        break
                                    elif opt == 'prev' and page > 1:
                                        page -= 1
                                    elif opt == 'next' and page < count_page:
                                        page += 1
                                    elif 1 <= int(opt) <= len(user_list):
                                        u_id = user_list[int(opt)-1][0]
                                        __user_service.delete_by_id(u_id)
                                        print(Fore.LIGHTGREEN_EX, '删除成功，3S后自动返回')
                                        time.sleep(3)
                                        continue
                            elif opt == 'back':
                                break
                    elif opt == 'back':
                        break
                    elif opt == 'exit':
                        sys.exit(0)
                elif role == '新闻编辑':
                    print('test')
        # 登录失败
        else:
            print('\t登陆失败，3秒后自动返回')
            time.sleep(3)
    elif opt == '2':
        sys.exit(0)

