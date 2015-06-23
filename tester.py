
from ipath import *

top = Folder(r"C:/Users\\kimo/Desktop")
print top.path, top.size
for folder in top.folders:
    print folder.name, folder.size
print top.overview(maxdepth=2)
for e in loop_folder(r"C:/Users\\kimo/Desktop", maxdepth=1):
    print(e)
print( current_script().path )
print( current_folder().path )
folder = Folder(r"C:/Users\\kimo/Desktop")
print( folder.path,folder.name,folder.content )
folder.up()
print( folder.path )
for e in folder.loop():
    print e.path
folder.down("Desktop")
print( folder.path )
