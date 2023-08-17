from mongo_db import client
from gridfs import GridFS
from bson import ObjectId

# 读取文件保存到本地
db = client.school
gfs = GridFS(db, collection='book')
doc = gfs.get(ObjectId('6398507633b5a316087c1802'))
file = open('d:/data/linux_new.jpg', 'wb')
file.write(doc.read())
file.close()

# delete函数可以从GridFs中删除文件，并且只能通过主键删除
gfs.delete(ObjectId('6398507633b5a316087c1802'))
