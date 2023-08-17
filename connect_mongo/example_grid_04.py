from mongo_db import client
from gridfs import GridFS

db = client.school
gfs = GridFS(db, collection='book')

file = open('d:/data/linux.JPG', 'rb')
args ={
    'type': 'jpg',
    'keyword': 'linux'
}
gfs.put(file, filename='linux', **args)
file.close()
