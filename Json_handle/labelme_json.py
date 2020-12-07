
import os 
import json

dir = './'

with open(dir, 'r') as f:
    json_file = json.load(f)s
    labelme_json = {}
    # print(json_file)
    for a in json_file:
        labelme_json["Version"] = "LMAI"
        labelme_json["flags"] = {}
        labelme_json["shapes"] = []
        data = a['Data']
        for b in data['svgArr']:
            shapes_obj = {}
            shapes_obj["label"]=b['name']
            shapes_obj["line_color"]=None
            shapes_obj["fill_color"]=None
            shapes_obj["points"] = []
            if not b['data']:
                continue
            for c in b['data']:
                if c['x'] == 0:
                    print(x['x'])

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
            labelme_json["imagePath"]=a['imageName']
            labelme_json["imageData"]=None
            labelme_json["imageHeight"]=a['imageHeight']
            labelme_json["imageWidth"]=a["imageWidth"]
            with open('./test/' + a['imageName'].split('.')[0]+'.json', 'w') as f:
                json.dump(labelme_json, f, indent=4)

   
