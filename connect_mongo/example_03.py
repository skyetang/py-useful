from mongo_db import client

try:
    # client.school.teacher.delete_one({'name': 'scott'})
    # client.school.teacher.delete_many({})
    res = client.school.student.find().skip(0).limit(2)
    for one in res:
        print(one['name'], one['age'])
    names = client.school.student.distinct('name')
    for one in names:
        print(one)
    students = client.school.student.find().sort([('name', -1)])
    for one in students:
        print(one['name'], one['age'])
except Exception as e:
    print(e)
