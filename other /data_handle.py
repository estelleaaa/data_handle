# Nuport bin to pcd 
# Nuport change images'name 

import os 
import os.path
import open3d as o3d
import numpy as np
import struct
import sys

class NuPort:
    # bin to pcd 
    '''
    def bin2pcd(path):
        for parents, dirs, files in os.walk(path):
            for file in files:
                filepath = os.path.join(parents, file)
                size_float = 4
                list_pcd = []
                with open(filepath, 'rb') as f:
                    byte = f.read(size_float*4)
                    while byte:
                        x, y, z, intensity = struct.unpack("ffff", byte)
                        list_pcd.append([x, y, z])
                        byte = f.read(size_float*4)

                np_pcd = np.asarray(list_pcd)
                pcd = o3d.geometry.PointCloud()
                v3d = o3d.utility.Vector3dVector
                pcd.points = v3d(np_pcd)
                filename = './lidar_pcd/' + file.split('.')[0]+'.pcd'
                o3d.io.write_point_cloud(filename, pcd)
'''
    def data_handle(self):
        for parents, dirs, files in os.walk(path):
            for file in files:
                filepath = os.path.join(parents, file)
                if os.path.splitext(filepath)[1] == '.jpg':
                    oldname = filepath
                    bianhao = file.split('_')[-1].split('.')[0]  
                    newname = os.path.join(parents, 'lidar_'+bianhao+'.jpg')
                    os.rename(oldname, newname)
                
                if os.path.splitext(filepath)[1] == '.bin':
                    size_float = 4
                    list_pcd = []
                    with open(filepath, 'rb') as f:
                        byte = f.read(size_float*4)
                        while byte:
                            x, y, z, intensity = struct.unpack("ffff", byte)
                            list_pcd.append([x, y, z])
                            byte = f.read(size_float*4)
                    np_pcd = np.asarray(list_pcd)
                    pcd = o3d.geometry.PointCloud()
                    v3d = o3d.utility.Vector3dVector
                    pcd.points = v3d(np_pcd)
                    filename = './lidar_pcd/' + file.split('.')[0]+'.pcd'
                    o3d.io.write_point_cloud(filename, pcd)
                    
path = './sample/'
nuport = NuPort()
nuport.data_handle()