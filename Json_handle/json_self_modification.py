
import os 
import os.path 
import json


def changeId(path):
    for parents,dirs, files in os.walk(path):
        for file in files:
            if file == '.DS_Store':
                pass
            else:            
                filepath = os.path.join(parents,file)
                with open(filepath,'r') as f:
                    oldfile = json.load(f)  
                    categories = []
                    for c in oldfile['categories']:
                        categ_info={}
                        categ_info['name']=c['name']
                        categ_info['id']=c['id']
                        categories.append(categ_info)  
                        
                    for a in oldfile['annotations']:
                        for b in categories:
                            if a['category_id'] == b['name']: 
                                a['category_id']=b['id']
                                new = oldfile

                                with open(filepath,'w') as f:
                                    json.dump(new,f)


path = './test'
changeId(path)

