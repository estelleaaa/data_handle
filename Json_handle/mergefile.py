import json
import os 
import os.path 
import requests



# method 01 

# final_json = []
# dirRoot = './1'
# for parent, dirnames, filenames in os.walk(dirRoot):
#     for f in filenames:
#         # print(f)
#         with open('./1/' + f,'r') as f1:
#             json1 = json.load(f1)
#             # print(json1)

#             for i in json1:
#                 final_json.append(i)
#                 # print(final_json)

#             with open('./2/final.json', 'w') as a:
#                 json.dump(final_json, a, indent=4)
            
# 合并一个项目里面的json

class DataJson():
    def getData(self):
        r = requests.post('https://app.labelhub.cn/api/product/productDataJson?pid=xxxxx', verify=False)
        json_data = json.loads(r.text)
        # print(json_data)
        return json_data

    def mergeFile(self):
        final_json = {}
        final_json['data'] = []
        json1 = self.getData()

        data = json1['data']
        for a in data:
            final_json['data'].append(a)
                # return final_json
            # print(final_json)
        with open('./2/final.json', 'w') as a:
            json.dump(final_json, a, indent=4)

transDir = DataJson()
transDir.mergeFile()
