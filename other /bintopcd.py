# 2 methods for converting bin to pcd files

import os
import os.path
import open3d as o3d
import struct 
import numpy as np
import sys

# method 1
def bin_to_pcd(path):
    # read files from the path
    for parents,dirs,files in os.walk(path):
        for file in files:
            filepath = os.path.join(parents,file)
            # define float size is 4 byte
            size_float = 4 
            list_pcd = []
            # read each file contents
            with open(filepath,'rb') as f:
                # read bytes from file
                byte = f.read(size_float*4)
                print(sys.getsizeof(byte), ' this is size of byte--------------')
                
                while byte:
                    # struct.unpack() is to format string
                    x, y, z, intensity = struct.unpack("ffff", byte)
                    list_pcd.append([x,y,z])
                    byte = f.read(size_float*4)
            # create array
            np_pcd = np.asarray(list_pcd)
            # o3d.geometry.PointCloud() A point cloud consists of point coordinates, optionally point color and point normals
            pcd = o3d.geometry.PointCloud()
            # o3d.utility.Vector3dVector: convert float64 numpy array of shape(n,3) to open 3D format 
            v3d = o3d.utility.Vector3dVector
            pcd.points = v3d(np_pcd)
            # create filename
            filename = './lidar_pcd/' + file.split('.')[0]+'.pcd'
            # write the pcd file
            # open3d.io.write_point_cloud(filename, pointcloud, write_ascii=False, compressed=False, print_progress=False
            o3d.io.write_point_cloud(filename, pcd)

path = './convert/lidar_bin/'
bin_to_pcd(path)
                   
'''
# method2
def bin_convert_pcd(path):
    for parents, dirs, files in os.walk(path):
        for file in files:
            filepath=os.path.join(parents,file)
            # load binary piunt cloud
            # np.fromfile(file, dtype=float, count=1,sep='',offset=0) is a high way of reading binary data with a known data-type
            bin_pcd = np.fromfile(filepath, dtype=np.float32)
            # reshape 
            points = bin_pcd.reshape((-1, 4))[:,0:3]
            o3d_pcd = o3d.geometry.PointCloud(o3d.utility.Vector3dVector(points))
            filename = './lidar_pcd/' + file.split('.')[0]+'.pcd'
            o3d.io.write_point_cloud(filename, o3d_pcd)

path = './convert/lidar_bin/'
bin_convert_pcd(path)
'''