#!/usr/bin/python3
from models.base_model import BaseModel
#from models import storage

from models.engine.file_storage import FileStorage

my = FileStorage()

my.reload()
all = my.all()
print("_____________________")
for obj_id in all.keys():
    obj = all[obj_id]
    print(obj)
new = BaseModel()
my.new(new)
print(my.all())
my.save()
all = my.all()
print("_____________________")
for obj_id in all.keys():
    obj = all[obj_id]
    print(obj)