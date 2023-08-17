# coding:utf-8

# 学生信息库
class StudentInfo(object):
    def __init__(self, students):
        self.students = students

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
        check = self.check_user_info(**kwargs)
        if check != True:
            print(check)
            return
        self.__add(**kwargs)

    def adds(self, new_students):
        for student in new_students:
            check = self.check_user_info(**student)
            if check != True:
                print(check)
                continue
            id_ = max(self.students) + 1
            self.__add(**student)

    def __add(self, **student):
        id_ = max(self.students) + 1
        self.students[id_] = student



    def delete(self, student_id):
        if student_id not in self.students:
            print('ID：{}不存在'.format(student_id))
        else:
            user_info = self.students.pop(student_id)
            print('----学号：{},{}同学的信息已经被删除了'.format(student_id, user_info['name']))

    def deletes(self, ids):
        for id_ in ids:
            if id_ not in self.students:
                print(f'{id_}不在学生库中')
                continue
            else:
                student_info = self.students.pop(id_)
                print(f'学号 {id_} 学生{student_info["name"]}已移除')

    def update(self, student_id, **kwargs):
        if student_id not in self.students:
            print(f'这个学号不存在{student_id}')
        check = self.check_user_info(**kwargs)
        if check != True:
            print(check)
            return
        self.students[student_id] = kwargs
        print(f'{student_id}同学的信息更新完毕')

    def updates(self, update_students):
        print(update_students)
        for student in update_students:
            print('x', student)
            key = list(student.keys())[0]
            if key not in self.students:
                print(f'学号{key}不存在')
                continue
            check = self.check_user_info(**student[key])
            if check != True:
                print(check)
                continue
            self.students[key] = student[key]
            print(f'学号{key}已更新')


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
        if 'name' not in kwargs:
            return '没有发现学生姓名'
        if 'age' not in kwargs:
            return '没有学生年龄'
        if 'sex' not in kwargs:
            return '没有学生性别'
        if 'class_number' not in kwargs:
            return '没有学生班级'
        return True


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
    students_info = StudentInfo(students)
    user = students_info.get_user_by_id(1)
    students_info.add(name='李林', age=34, class_number='E', sex='boy')
    users = [
        {'name': '张五', 'age': 22, 'class_number': 'E', 'sex': 'boy'},
        {'name': '王六', 'age': 22, 'class_number': 'E', 'sex': 'boy'},
    ]
    students_info.adds(users)
    students_info.deletes([7, 8])
    update_users = [
        {1: {'name': 'ab', 'age': 21, 'class_number': 'E', 'sex': 'boy'}},
        {2: {'name': '张九', 'age': 22, 'class_number': 'E', 'sex': 'boy'}}
    ]
    students_info.updates(update_users)
    students_info.get_all_students()
    print(students_info.search_users(name=''))



