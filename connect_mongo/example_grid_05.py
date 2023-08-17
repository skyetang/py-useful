from mongo_db import client
from gridfs import GridFS
import math
import datetime
from bson import ObjectId

db = client.school
gfs = GridFS(db, collection='book')

book = gfs.find_one({'filename': 'linux'})
print(book.filename)
print(book.type)
print('%dM' % math.ceil(book.length/1024/1024))
print('----------------------')

books = gfs.find({'type': 'jpg'})
for one in books:
    # 格林威治时间，转成北京时间
    uploadDate = one.uploadDate + datetime.timedelta(hours=8)
    date = uploadDate.strftime('%Y-%m-%d %H:%M:%S')
    print(one._id, one.filename, date)

# exists判断GridFs是否存储了某个文件
rs = gfs.exists(ObjectId('6398507633b5a316087c1802'))
print(rs)

rs = gfs.exists(**{'type': 'pdf'})
print(rs)
