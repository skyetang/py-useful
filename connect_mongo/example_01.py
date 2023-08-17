from mongo_db import client

client.school.studnet.insert_one({'name': 'scott'})
client.school.teacher.insert_many([
    {'name': 'skye'},
    {'name': 'byte'}
])
res = client.school.teacher.find()
for one in res:
    print(one['name'], one['_id'])
res2 = client.school.teacher.find_one({'name': 'scott'})
print(res2['name'], res2['_id'])

