import os
import pandas as pd
import xml.etree.ElementTree as ET
from xml.dom.minidom import parseString
import xml.dom.minidom as xml
import urllib3
import json
http = urllib3.PoolManager()


class DataTransfer:

    def getData(self):
        r = http.request(
            'POST', 'http://labelhub-cookie.awkvector.com/api/product/productDataJson?pid=xxx')
        json_data = json.loads(r.data)
        return json_data['data']

    def transferData(self):
        data = self.getData()
        doc = xml.Document()    # 创建DOM()树对象
        declaration = doc.toxml() # 输出未格式化
        for i in data:
            print(i, ' ------ i in data -------')
            new_xml = ET.Element('annotations')
            folder = ET.SubElement(new_xml, 'folder')
            folder.text = 'AliOSS'
            filename = ET.SubElement(new_xml, 'filename')
            filename.text = i['iname']
            filepath = ET.SubElement(new_xml, 'path')
            filepath.text = i['imagepath']
            source = ET.SubElement(new_xml, 'source')
            database = ET.SubElement(source, 'database')
            database.text = 'Unknown'
            size = ET.SubElement(new_xml, 'size')
            width = ET.SubElement(size, 'width')
            width.text = str(i['width'])
            height = ET.SubElement(size, 'height')
            height.text = str(i['height'])
            depth = ET.SubElement(size, 'depth')
            depth.text = '3'
            segmented = ET.SubElement(new_xml, 'segmented')
            segmented.text = '0'
            xml_string = ET.tostring(new_xml)    # tostring 返回对象是用字符串表示的
            xml_write = parseString(xml_string).toprettyxml()[    
                len(declaration):]  # toprettystring 格式化输出
            with open(os.path.splitext(i['iname'])[0] + '.xml', 'w') as handle:
                handle.write(xml_write)



transDir = DataTransfer()
transDir.transferData()
