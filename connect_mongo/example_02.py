from mongo_db import client

try:
    client.school.teacher.update_many({}, {'$set': {'role': ['教师']}})
    client.school.teacher.update_one({'name': 'scott'}, {'$push': {'role': '年级主任'}})
    res = client.school.teacher.find()
    for one in res:
        print(one['name'], one['role'][0])
except Exception as e:
    print(e)
    