import os
import json
import requests


class DataTransfer:

    def getData(self):
        r = requests.post('https://app.labelhub.cn/api/product/productDataJson?pid=xxx', verify=False)
       
        json_data = json.loads(r.text)
        return json_data['data']

    def transferData(self):
        data = self.getData()
        data_json = {}
        for i in data:
            
            data_json['shapes'] = []
            detail = json.loads(i['detail'])
            json_obj = []
            shape_obj = {}
            shape_obj['task_id'] = detail['svgArr'][0]['id']
            shape_obj['reviews_status'] = 'approved'
            shape_obj['instruction_url'] = i['imagepath']
            shape_obj['annotation_type'] = 'image'
            shape_obj['annotation_objects'] = {}
            shape_obj['annotation_attributes'] = {}
            
                
            if len(detail['svgArr'])<=1:
                for j in detail['svgArr']:
                    if j['name'] == 'vehicle':
                        shape_obj['annotation_objects']['vehicle'] = []
                        shape_obj['annotation_objects']['vehicle'].append(j['data'][3]['x'])
                        shape_obj['annotation_objects']['vehicle'].append(j['data'][3]['y'])
                        shape_obj['annotation_objects']['vehicle'].append(j['data'][1]['x'])
                        shape_obj['annotation_objects']['vehicle'].append(j['data'][1]['y'])
                        shape_obj['annotation_objects']['license plate'] = []
                        shape_obj['annotation_objects']['license plate'].append(-1)
                        shape_obj['annotation_objects']['license plate'].append(-1)
                        shape_obj['annotation_objects']['license plate'].append(-1)
                        shape_obj['annotation_objects']['license plate'].append(-1)
                        shape_obj['annotation_attributes']['vehicle'] = {}
                        for k in j['secondaryLabel']:
                            if k['value'] is not None and k['value'] != '':
                                if k['name'] in ('pose', 'color'):
                                    shape_obj['annotation_attributes']['vehicle'][k['name']] = k['value']
                                shape_obj['annotation_attributes']['vehicle']['make'] = k['name']
                                shape_obj['annotation_attributes']['vehicle']['model'] = k['value']
                        
                    if j['name'] == 'license plate':
                        shape_obj['annotation_objects']['license plate'] = []
                        shape_obj['annotation_objects']['license plate'].append(j['data'][3]['x'])
                        shape_obj['annotation_objects']['license plate'].append(j['data'][3]['y'])
                        shape_obj['annotation_objects']['license plate'].append(j['data'][1]['x'])
                        shape_obj['annotation_objects']['license plate'].append(j['data'][1]['y'])
                        shape_obj['annotation_objects']['vehicle'] = []
                        shape_obj['annotation_objects']['vehicle'].append(-1)
                        shape_obj['annotation_objects']['vehicle'].append(-1)
                        shape_obj['annotation_objects']['vehicle'].append(-1)
                        shape_obj['annotation_objects']['vehicle'].append(-1)
                        for k in j['secondaryLabel']:
                            print(k,' ----- license plate ----k ')
                            if k['value'] is not None and k['value'] != '':
                                if k['name'] not in ('states', 'number'):
                                    shape_obj['annotation_attributes']['license plate'][k['name']] = k['value']
                                else:
                                    shape_obj['annotation_attributes']['license plate']['number'].append(k['value'])
                    
            if len(detail['svgArr'])>=2:
                for j in detail['svgArr']:    
                     
                    if j['name'] == 'vehicle':
                        shape_obj['annotation_objects']['vehicle'] = []
                        shape_obj['annotation_objects']['vehicle'].append(j['data'][3]['x'])
                        shape_obj['annotation_objects']['vehicle'].append(j['data'][3]['y'])
                        shape_obj['annotation_objects']['vehicle'].append(j['data'][1]['x'])
                        shape_obj['annotation_objects']['vehicle'].append(j['data'][1]['y'])
                        shape_obj['annotation_attributes']['vehicle'] = {}
                        for k in j['secondaryLabel']:
                            if k['value'] is not None and k['value'] != '':
                                if k['name'] in ('pose', 'color'):
                                    shape_obj['annotation_attributes']['vehicle'][k['name']] = k['value']
                                shape_obj['annotation_attributes']['vehicle']['make'] = k['name']
                                shape_obj['annotation_attributes']['vehicle']['model'] = k['value']
                    if j['name'] == 'license plate':
                        shape_obj['annotation_objects']['license plate'] = []
                        shape_obj['annotation_objects']['license plate'].append(j['data'][3]['x'])
                        shape_obj['annotation_objects']['license plate'].append(j['data'][3]['y'])
                        shape_obj['annotation_objects']['license plate'].append(j['data'][1]['x'])
                        shape_obj['annotation_objects']['license plate'].append(j['data'][1]['y'])
                        shape_obj['annotation_attributes']['license plate'] = {}
                        shape_obj['annotation_attributes']['license plate']['number'] = []
                        for k in j['secondaryLabel']:
                            print(k,' ----- license plate ----k ')
                            if k['value'] is not None and k['value'] != '':
                                if k['name'] not in ('states', 'number'):
                                    shape_obj['annotation_attributes']['license plate'][k['name']] = k['value']
                                else:
                                    shape_obj['annotation_attributes']['license plate']['number'].append(k['value'])
            json_obj.append(shape_obj)           
            
            with open('./test/' + i['iname'].split('.')[0] + '.json', 'w') as f:
                json.dump(json_obj, f, indent = 4)

            print(json_obj, ' json obj ')

transDir = DataTransfer()
transDir.transferData()
