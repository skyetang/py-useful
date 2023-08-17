# coding:utf-8

# 学生信息库

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


def get_students():
    for id_ in students:
        value = students[id_]
        print('学号：{}，姓名：{},年龄：{},班级：{}'.format(
            id_, value['name'], value['age'], value['class_number']
        ))


# get_students()


def get_all_students():
    for id_, value in students.items():
        print('学号：{}，姓名：{},年龄：{},班级：{}'.format(
            id_, value['name'], value['age'], value['class_number']
        ))
    return students


get_all_students()


def add_students(**kwargs):
    if 'name' not in kwargs:
        print('没有发现学生姓名')
        return
    if 'age' not in kwargs:
        print('没有学生年龄')
        return
    if 'sex' not in kwargs:
        print('没有学生性别')
        return
    if 'class_number' not in kwargs:
        print('没有学生班级')
        return
    id_ = max(students) + 1
    students[id_] = {
        'name': kwargs['name'],
        'age': kwargs['age'],
        'sex': kwargs['sex'],
        'class_number': kwargs['class_number']
    }


# add_students(name='小白', age=19, class_number='B', sex='girl')
# get_all_students()


def delete_student(student_id):
    if student_id not in students:
        print('ID：{}不存在'.format(student_id))
    else:
        user_info = students.pop(student_id)
        print('----学号：{},{}同学的信息已经被删除了'.format(student_id, user_info['name']))


# delete_student(1)
# get_all_students()


def check_user_info(**kwargs):
    if 'name' not in kwargs:
        return '没有发现学生姓名'
    if 'age' not in kwargs:
        return '没有学生年龄'
    if 'sex' not in kwargs:
        return '没有学生性别'
    if 'class_number' not in kwargs:
        return '没有学生班级'
    return True


def update_student(student_id, **kwargs):
    if student_id not in students:
        print(f'这个学号不存在{student_id}')
    check = check_user_info(**kwargs)
    if check != True:
        print(check)
        return
    students[student_id] = kwargs
    print(f'{student_id}同学的信息更新完毕')


update_student(1, name='小白', age=19, class_number='B', sex='girl')
get_all_students()


def get_user_by_id(student_id):
    return students.get(student_id)

#print(get_user_by_id(3))

def search_users(**kwargs):
    values = list(students.values())
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
        if user[key] == value:
            res.append(user)
    return res

print(search_users(sex='girl'))

