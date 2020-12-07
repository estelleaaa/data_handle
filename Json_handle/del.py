

import os 
import json

def json_handle(path):
    for parents, dirs, files in os.walk(path):
        for file in files:
            if file != '.DS_Store':
                filepath = os.path.join(parents,file)
                with open(filepath, 'r') as f:
                    json_file = json.load(f)
                    # print(json_file)
                    json_file['flags']={}
                    for a in json_file['shapes']:
                        a['flags']={}
                    json_file['imageData']=None
                    print(json_file)
                    with open(filepath,'w') as f:
                        json.dump(json_file,f, indent=4)   
path = './20201201/'
json_handle(path)