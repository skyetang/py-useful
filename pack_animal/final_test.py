# coding:utf-8

import json
import os
import logging

class NotArgsError(Exception):
    def __init__(self, message):
        self.message = message


class PathNotExist(Exception):
    def __init__(self, message):
        self.message = message


class FormatError(Exception):
    def __init__(self, message):
        self.message = message


# 学生信息库
class StudentInfo(object):
    def __init__(self, stu_path, log_path):
        self.stu_path = stu_path
        self.log_path = log_path
        self.__log()
        self.__path_exist()
        self.__read()

    def __log(self):
        if os.path.exists(self.log_path):
            mode = 'a'
        else:
            mode = 'w'
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s - %(filename)s - %(lineno)d - %(levelname)s - %(message)s',
            filename=self.log_path,
            filemode=mode
        )
        self.log = logging

    def __path_exist(self):
        if not os.path.exists(self.stu_path):
            raise PathNotExist(f'没有找到相关文件--{self.stu_path}')
        if not self.stu_path.endswith('.json'):
            raise FormatError(f'{self.stu_path}--不是json文件')

    def __read(self):
        with open(self.stu_path, 'r') as f:
            data = f.read()
        print(json.loads(data))
        self.students = json.loads(data)

    def __save(self):
        with open(self.stu_path, 'w') as f:
            json_data = json.dumps(self.students)
            f.write(json_data)

    def __save_read(self):
        self.__save()
        self.__read()

    def get_user_by_id(self, student_id):
        return self.students.get(student_id)

    def get_students(self):
        for id_ in self.students:
            value = self.students[id_]
            print('学号：{}，姓名：{},年龄：{},班级：{}'.format(
                id_, value['name'], value['age'], value['class_number']
            ))

    def get_all_students(self):
        for id_, value in self.students.items():
            print('学号：{}，姓名：{},年龄：{},班级：{}'.format(
                id_, value['name'], value['age'], value['class_number']
            ))
        return self.students

    def add(self, **kwargs):
        try:
            self.check_user_info(**kwargs)
        except Exception as e:
            print(e)
            return
        self.__add(**kwargs)
        self.__save_read()

    def adds(self, new_students):
        for student in new_students:
            try:
                self.check_user_info(**student)
            except Exception as e:
                print(e)
                continue
            self.__add(**student)
        self.__save_read()

    def __add(self, **student):
        if len(self.students) == 0:
            id_ = 1
        else:
            keys = list(self.students.keys())
            _keys = []
            for item in keys:
                _keys.append(int(item))
            id_ = max(_keys) + 1
        self.students[id_] = student
        self.log.info(f'学生{student["name"]}被注册了')



    def delete(self, student_id):
        if student_id not in self.students:
            self.log.warning('ID：{}不存在'.format(student_id))
        else:
            user_info = self.students.pop(student_id)
            self.log.warning('----学号：{},{}同学的信息已经被删除了'.format(student_id, user_info['name']))
        self.__save_read()

    def deletes(self, ids):
        for id_ in ids:
            if id_ not in self.students:
                print(f'{id_}不在学生库中')
                continue
            else:
                student_info = self.students.pop(id_)
                self.log.warning(f'学号 {id_} 学生{student_info["name"]}已移除')
        self.__save_read()

    def update(self, student_id, **kwargs):
        if student_id not in self.students:
            print(f'这个学号不存在{student_id}')
        check = self.check_user_info(**kwargs)
        if check != True:
            print(check)
            return
        self.students[student_id] = kwargs
        print(f'{student_id}同学的信息更新完毕')
        self.__save_read()

    def updates(self, update_students):
        print(update_students)
        for student in update_students:
            print('x', student)
            try:
                key = list(student.keys())[0]
            except IndexError as e:
                print(e)
                continue
            if key not in self.students:
                print(f'学号{key}不存在')
                continue
            try:
                self.check_user_info(**student[key])
            except Exception as e:
                print(e)
                continue
            self.students[key] = student[key]
            print(f'学号{key}已更新')
        self.__save_read()

    def search_users(self, **kwargs):
        print(self.students.keys())
        print(self.students.values())
        print(self.students.items())
        print(kwargs.keys())
        print(kwargs.values())
        values = list(self.students.values())
        key = None
        value = None
        res = []
        if 'name' in kwargs:
            key = 'name'
            value = kwargs[key]
        elif 'sex' in kwargs:
            key = 'sex'
            value = kwargs[key]
        elif 'age' in kwargs:
            key = 'age'
            value = kwargs[key]
        elif 'class_number' in kwargs:
            key = 'class_number'
            value = kwargs[key]
        else:
            print('没有发现的搜索关键字')

        for user in values:
            if value in user[key]:
                res.append(user)
        return res

    def check_user_info(self, **kwargs):
        assert len(kwargs) == 4, '参数的长度应该为4'

        if 'name' not in kwargs:
            raise NotArgsError('没有学生姓名')
        if 'age' not in kwargs:
            raise NotArgsError('没有学生年龄')
        if 'sex' not in kwargs:
            raise NotArgsError('没有学生性别')
        if 'class_number' not in kwargs:
            raise NotArgsError('没有学生班级')

        # isinstance 判断参数的类型
        if not isinstance(kwargs['name'], str):
            raise TypeError('姓名应该为字符串类型')
        if not isinstance(kwargs['age'], int):
            raise TypeError('年龄应该为整型')
        if not isinstance(kwargs['sex'], str):
            raise TypeError('性别应该为字符串类型')
        if not isinstance(kwargs['class_number'], str):
            raise TypeError('班级应为字符串类型')


students = {
    1: {
        'name': 'aiya',
        'age': 33,
        'sex': 'boy',
        'class_number': 'A'
    },
    2: {
        'name': 'yige',
        'age': 22,
        'sex': 'boy',
        'class_number': 'B'
    },
    3: {
        'name': '张三',
        'age': 12,
        'sex': 'girl',
        'class_number': 'C'
    },
    4: {
        'name': '李四',
        'age':28,
        'sex': 'boy',
        'class_number': 'C'
    },
    5: {
        'name': '小蔡',
        'age': 28,
        'sex': 'girl',
        'class_number': 'B'
    }
}

if __name__ == '__main__':
   students_info = StudentInfo('students.json', 'students.log')
   # user = students_info.get_user_by_id(1)
   # students_info.add(name='李林', age=34, class_number='E', sex='boy')
   users = [
       {'name': '张五', 'age': 22, 'class_number': 'E', 'sex': 'girl'},
       {'name': '王六', 'age': 22, 'class_number': 'E', 'sex': 'boy'},
   ]
   students_info.adds(users)
   # students_info.get_all_students()
   students_info.deletes(['7', '8'])
   # update_users = [
   #     {1: {'name': 'ab', 'age': 21, 'class_number': 'E', 'sex': 'boy'}},
   #     {2: {'name': '张九', 'age': 22, 'class_number': 'E', 'sex': 'boy'}}
   # ]
   # students_info.updates(update_users)
   # students_info.get_all_students()



