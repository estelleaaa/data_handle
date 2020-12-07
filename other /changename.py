# 将名字前缀更改为和主文件一样的
import os 
import os.path

def changename(path):

    for parents,dirs,files in os.walk(path):
        for file in files:
            filepath = os.path.join(parents,file)
            if os.path.splitext(filepath)[1] == '.jpg':
                oldname= filepath
                bianhao = file.split('_')[-1].split('.')[0]
                newname= os.path.join(parents, 'lidar_' + bianhao + '.jpg')
                # print(newname)
                os.rename(oldname,newname)
                
            #     print(file)

path = './convert/'
changename(path)