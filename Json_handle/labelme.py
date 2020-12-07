

import os 
import requests
import json

class DataTransfer:

    def getData(self):
        r = requests.post('https://app.labelhub.cn/api/product/productDataJson?pid=xxx&status=x&check=xx', verify=False)
        json_data = json.loads(r.text)
        return json_data['data']

    def transferData(self):
        data = self.getData()
        labelme_json={}
        for a in data:
            labelme_json["Version"]="LMAI"
            labelme_json["flags"]={}
            labelme_json["shapes"]=[]
            details = json.loads(a['detail'])
            for b in details['svgArr']:
                shapes_obj = {}
                shapes_obj["label"]=b['name']
                shapes_obj["line_color"]=None
                shapes_obj["fill_color"]=None
                shapes_obj["points"] = []
                if not b['data']:
                    continue
                for c in b['data']:
                    if c['x'] == 0:
                        print(c['x'])

                    points_arr = []
                    points_arr.append(c['x'])
                    points_arr.append(c['y'])
                    shapes_obj["points"].append(points_arr)
            
                labelme_json["shapes"].append(shapes_obj)
                shapes_obj["shape_type"]= b['tool']
                shapes_obj["flags"]={}
            labelme_json["lineColor"]=[
                0,
                255,
                0,
                128
            ]
            labelme_json["fillColor"]=[
                255,
                0,
                0,
                128
            ]
            labelme_json["imagePath"]=a['iname']
            labelme_json["imageData"]=None
            labelme_json["imageHeight"]=a['height']
            labelme_json["imageWidth"]=a["width"]
            with open('./test/' + a['iname'].split('.')[0]+'.json', 'w') as f:
                json.dump(labelme_json, f, indent=4)


transDir = DataTransfer()
transDir.transferData()

                    
