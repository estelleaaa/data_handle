# get data from web and change the format to write a new json file

import os
import json
import requests

class DataTransfer:

    def getData(self):
        r = requests.post('https://app.labelhub.cn/api/product/productDataJson?pid=xxxx&status=x&check=x', verify=False)
  
        json_data = json.loads(r.text)    # str to dict
        return json_data['data']

    def transferData(self):
        data = self.getData()
        data_json = {}
        for i in data:
            
            data_json['shapes'] = []
            detail = json.loads(i['detail'])
            for j in detail['svgArr']:
                shape_obj = {}
                shape_obj['shape_type'] = j['tool']
                shape_obj['points'] = []
                
                if not j['data']:
                    continue
                for k in j['data']:
                    if k['x'] == 0:
                        print(k['x'], '---------------------00')
                    
                        
                    points_arr = []    
                    points_arr.append(k['x'])
                    points_arr.append(k['y'])
                    shape_obj['points'].append(points_arr)
                
                data_json['shapes'].append(shape_obj)
                shape_obj['flags'] = {}
                shape_obj['group_id'] = None
                shape_obj['label'] = j['name']
            data_json['imagePath'] = i['iname']
            data_json['flags'] = {}
            data_json['imageWidth'] = i['width']
            data_json['imageHeight'] = i['height']
            with open('./20201119_02/' + i['iname'].split('.')[0] + '.json', 'w') as f:
                json.dump(data_json, f, indent = 4)

transDir = DataTransfer()
transDir.transferData()
