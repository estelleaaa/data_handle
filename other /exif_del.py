# 删除图片exif信息
import exifread as exif
import os
import os.path 
import piexif



dir = 'elel'


class DelExif:
    def read_info(self):
        for parent, dirs, files in os.walk(dir):
            for f in files:
                filepath  = os.path.join(parent,f)
                with open (filepath, 'rb') as f1:
                    tags = exif.process_file(f1)
                    if tags:
                        # piexif.remove(filepath)        
                        print('文件名：',f)
                    # else:
                    #     print('all exifdeleted')


exifDel = DelExif()
exifDel.read_info()
    
