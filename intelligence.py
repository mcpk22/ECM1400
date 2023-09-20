# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification
import numpy as np
from skimage import io


def find_red_pixels(*args,**kwargs):
    """Function to find red pixels of the png image then turn the red pixels into white"""
    #reading the png image using skimage
    originalimage=io.imread('project\project\data\map.png')
    #copy the image as an backup
    copy_image=originalimage.copy()
    new_image=[]
    for r in copy_image:
        red=[]
        for pixel in r:
            if pixel[0]>=100 and pixel[1]<=45 and pixel[2]<=45:
                #scaning red pixels
                red.append([255,255,255])
                #turning red pixels into white pixels 
            else:
                red.append([0,0,0])
                #turning red pixels into black pixels
        new_image.append(red)
    new_image=np.array(new_image)
    io.imsave("map-red-pixels.jpg",new_image)
    return new_image
    

def find_cyan_pixels(*args,**kwargs):
    """Function to find cyan pixels of the png image then turn the cyan pixels into white"""
    #reading the png image using skimage
    originalimage=io.imread("project\project\data\map.png")
    copy_image=originalimage.copy()
    new_image=[]
    for c in copy_image:
        cyan=[]
        for pixel in c:
            if pixel[0]<=80 and pixel[1]>=50 and pixel[2]>=100:
                #scaning red pixels
                cyan.append([255,255,255])
                #turning cyan pixels into white pixels 
            else:
                cyan.append([0,0,0])
                #turning cyan pixels into black pixels
        new_image.append(cyan)
    new_image=np.array(new_image)
    io.imsave("map-cyan-pixels.jpg",new_image)
    return new_image

def pixel_neighbours(self, p):

    rows, cols = self.shape

    i, j = p[0], p[1]

    rmin = i - 1 if i - 1 >= 0 else 0
    rmax = i + 1 if i + 1 < rows else i

    cmin = j - 1 if j - 1 >= 0 else 0
    cmax = j + 1 if j + 1 < cols else j

    neighbours = []

    for x in range(rmin, rmax + 1):
        for y in range(cmin, cmax + 1):
            neighbours.append([x, y])
    neighbours.remove([p[0], p[1]])

    return neighbours


def detect_connected_components(arr):
    """Function to find the connected components"""
    # Your code goes here
    
    arr=np.array(arr)
    row,column,RGB=arr.shape
    print(arr.shape)
    mark=np.zeros((row,column))
    mark_count=1
    Q=[]
    dict={}
    for x in range (0,row):
        for y in range(0,column):
            if arr[x,y][0]!=0 and mark[x,y]==0.0:
                mark[x,y]=mark_count
                Q.append([x,y])
                pixel_count=0
                while len(Q)>0:
                    m,n=Q.pop(0)
                    pixel_count+=1
                    list=pixel_neighbours(mark,(m,n))
                    for coordinate in list:
                        s,t=coordinate
                        if arr[s,t][0]!=0 and mark[s,t]==0.0:
                            mark[s,t]=mark_count
                            Q.append([s,t])
                dict[mark_count] = pixel_count

                mark_count = mark_count+1
    

    print(mark_count)
        
    with open("cc-output-2a.txt","a") as f:
        for keys in dict:
            print(f'connected components {keys}, pixel count = ', dict[keys] , file=f)
        print(f'Total number of connected components = ',mark_count, file=f)
        
    #file.writelines(final)
    
    #print("connected_component: " ,mark_count,",", "number of pixels", pixel_count)



def detect_connected_components_sorted(*args,**kwargs):
    """Your documentation goes here"""
    # Your code goes here
    
    data=open("cc-output-2a.txt").readlines()    
    
    list=[]
    for line in data:
        line=line.strip()
        line=line.split()
        temp= line[0]
        list.append(line[6])
    list.sort()
    


    


new_image = find_red_pixels()
new_image = find_cyan_pixels()
detect_connected_components(new_image)
detect_connected_components_sorted()
