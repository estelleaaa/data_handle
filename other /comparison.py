#!/usr/bin/python
__author__ = 'Estelle'

dir1 = './test01'
dir2 = './test02'
import os
f1 = []
f2 = []

for root, dirs, files in os.walk(dir1):
    for filename in files:
        filePath = os.path.join(root,filename)
        f1.append(filePath[5:])
        
for root, dirs, files in os.walk(dir2):
    for filename in files:
        filePath = os.path.join(root,filename)
        f2.append(filePath[4:])

print(set(f1)^set(f2))

