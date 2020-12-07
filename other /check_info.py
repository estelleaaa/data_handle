
import os 
import os.path
import json

dir = './20201119_02/'
class Verify:
    def points_verify(self):
        for parent, dirnames, filenames in os.walk(dir):
            for f in filenames:
                filepath = os.path.join(parent, f)
                with open(filepath,'r') as f1:
                    json_content = json.load(f1)
                    
                    for a in json_content['shapes']:
                        # 查该文件里面有的点位信息xy是否为0
                        WrongFile = []
                        WrongData = []
                        BoxCounts = []
                        for xy in a['points']:
                            if xy[0] == 0:
                                print(f, '----------this point is x:0')
                            if xy[1] == 0:
                                print(f, '----------this point is y:0')
                        
                        if len(a['points']) != 4:
                            print('文件名/filename:',f,'点位数量/numbers of points:',len(a['points']),'------this is not 4 points files')

                        
                    
                            


pointsV = Verify()
pointsV.points_verify()   
                    