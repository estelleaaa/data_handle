# Tools for handling data and files
[TOC]
## xml_handle
`xml_handle/dataTransfer.py`
- Get data from a web platform and change the format to xml file
- change the url 
- create a new folder to save xml files

`xml_handle/xml2xml.py`
- change xml file to another format xml file
- this is the path to the folder where saved sourced xml files
```
dirRoot = 'test'
```
___

## Json_handle
 `Json_handle/dataToJson01.py` 
 - get data from a web platform and change the format to write a new json file 
- change the url 
- create a folder that you need to save data 
        
        ```
        # modify the url
        r = requests.post('https://app.labelhub.cn/api/product/productDataJson?pid=xxxx&status=x&check=x', verify=False)

        # modify the path to the folder you created './20201119_02/'
        with open('./20201119_02/' + i['iname'].split('.')[0] + '.json', 'w') as f:
                json.dump(data_json, f, indent = 4)
        ```


`Json_handle/dataToJson02`
- get data from a web platform and change the format to write a new json file
- change the path to the folder to save files
```
with open('./test/' + i['iname'].split('.')[0] + '.json', 'w') as f:
                json.dump(json_obj, f, indent = 4)
```


`Json_handle/del.py`
- To delete the `""` where in the json file `"{}"` `"null"` 
- change the path where saved files `path = './20201201/` 

`Json_handle/json_self_modification.py`
- To modify the contents of json files (in a large number of files)
- Rewrite the source files


`Json_handle/lableme.py`
- Get data from a platform and change the format which is same with lableme json file format

`Json_handle/labelme_json.py`
- change the local files to a new lableme json format

`Json_handle/mergefile.py`
- method1 is to merge local files 
- method2 is to merge the files exported online
___





## Other tools to handle files or data
### compare files in different folders 
`other/comparison.py`  
- the only thing you need to do is to modify the path of two folders
```
dir1 = './test01'
dir2 = './test02'
```

### Match and modify the filename
`other/changhename.py` change other files' name to pcd file 

- change the path of the folder where files saved `path = './convert/'`
___

### bintopcd
`other/bintopcd.py` 
- convert the bin file to pcd file
- change the path where bin files saved `path = './convert/lidar_bin/'` 
- create a new folder to save pcd file `'./lidar_pcd/`
    ```
    filename = './lidar_pcd/' + file.split('.')[0]+'.pcd'
    ```

`other/data_handle.py` 
- this is change merge two functions which are `bintopcd` `change file name to the pcd filename`

### check info 
`other/check_info.py` 
- check the number of the points in the json file and confirm if there is any  `x=0/y=0` 
- change the path of the folder where files saved `dir = './20201119_02'` 

### excel handle
`other/excel_handle.py`
- To read excel file and edit some info

### del exif info of a image file
`other/exif_del.py`
- to del the exif info of a image

