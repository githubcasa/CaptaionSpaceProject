from pathlib import Path
import csv
import cv2
import numpy as np
from os import listdir
from os.path import isfile, join
from fastiecm import fastiecm
from fastiecm_IF import fastiecm_IF
from fastiecm_IFH import fastiecm_IFH
from fastiecm_IS import fastiecm_IS
from PIL import Image

onlyfiles = [
                f for f in listdir('.')
                if isfile(join('.', f))
                and f.endswith('.jpg')
            ]

print(onlyfiles)

def create_csv_file(data_file):
    """Create a new CSV file and add the header row"""
    with open(data_file, 'w') as f:
        writer = csv.writer(f)
        header = ("File Name",
                  "IF_no_value",
                  "IF_no_forest",
                  "IF_ok_forest",
                  "IF_error",
                  "IFH_no_value",
                  "IFH_no_forest",
                  "IFH_Unhealthy_plant",
                  "IFH_Healthy_plant",
                  "IFH_error",
                  "IS_Useless_surface",
                  "IS_Usefull_surface",
                  "IS_error"                  
                  )
        writer.writerow(header)

def add_csv_data(data_file, data):
    """Add a row of data to the data_file CSV"""
    with open(data_file, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)

def display(image, image_name):
    image = np.array(image, dtype=float)/float(255)
    shape = image.shape
    height = int(shape[0] / 2)
    width = int(shape[1] / 2)
    image = cv2.resize(image, (width, height))

def contrast_stretch(im):
    in_min = np.percentile(im, 5)
    in_max = np.percentile(im, 95)

    out_min = 0.0
    out_max = 255.0

    out = im - in_min
    out *= ((out_min - out_max) / (in_min - in_max))
    out += in_min

    return out

def calc_ndvi(image):
    b, g, r = cv2.split(image)
    bottom = (r.astype(float) + b.astype(float))
    bottom[bottom==0] = 0.01
    ndvi = (b.astype(float) - r) / bottom
    return ndvi

def IF_pixel_count(image):

    img = Image.open(image)
    
    IF_no_value = 0
    IF_no_forest = 0
    IF_ok_forest = 0
    IF_error = 0    

    for pixel in img.getdata():
        if pixel == ( 0, 0, 0):
            IF_no_value += 1
        elif pixel == ( 95, 95, 95):
            IF_no_forest += 1
        elif pixel == ( 67, 127, 49):
            IF_ok_forest += 1
        else:
            IF_error += 1
            #print(pixel)

    data = (
        image,
        IF_no_value,
        IF_no_forest,
        IF_ok_forest,
        IF_error,
    )
    add_csv_data(data_file, data)

    print('no_value = ' + str(IF_no_value)+', no_forest = ' + str(IF_no_forest)+', ok_forest = ' + str(IF_ok_forest)+', error = ' + str(IF_error))

def IFH_pixel_count(image):

    img = Image.open(image)
    
    IFH_no_value = 0
    IFH_no_forest = 0
    IFH_Unhealthy_plant = 0
    IFH_Healthy_plant = 0
    IFH_error = 0    

    for pixel in img.getdata():
        if pixel == ( 0, 0, 0):
            IFH_no_value += 1
        elif pixel == ( 95, 95, 95):
            IFH_no_forest += 1
        elif pixel == (119, 221, 119):
            IFH_Unhealthy_plant += 1
        elif pixel == ( 37, 66, 0):
            IFH_Healthy_plant += 1
        else:
            IFH_error += 1
            #print(pixel)

    data = (
        image,
        "",
        "",
        "",
        "",
        IFH_no_value,
        IFH_no_forest,
        IFH_Unhealthy_plant,
        IFH_Healthy_plant,
        IFH_error
    )
    add_csv_data(data_file, data)

    print('IFH_no_value = ' + str(IFH_no_value)+
          ', IFH_no_forest = ' + str(IFH_no_forest)+
          ', IFH_Unhealthy_plant = ' + str(IFH_Unhealthy_plant)+
          ', IFH_Healthy_plant = ' + str(IFH_Healthy_plant)+
          ', IFH_error = ' + str(IFH_error)
          )

def IS_pixel_count(image):

    img = Image.open(image)
    
    IS_Useless_surface = 0
    IS_Usefull_surface = 0
    IS_error = 0    

    for pixel in img.getdata():
        if pixel == (0, 0, 255):
            IS_Useless_surface += 1
        elif pixel == ( 67, 127, 49):
            IS_Usefull_surface += 1
        else:
            IS_error += 1
            #print(pixel)

    data = (
        image,
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        IS_Useless_surface,
        IS_Usefull_surface,
        IS_error
    )
    add_csv_data(data_file, data)

    print('IS_Useless_surface = ' + str(IS_Useless_surface)+
          ', IS_Usefull_surface = ' + str(IS_Usefull_surface)+
          ', IS_error = ' + str(IS_error)
          )

### Program setup data  ########################################################
base_folder = Path(__file__).parent.resolve()
# Initialise the CSV file
data_file = base_folder/"data_index.csv"
create_csv_file(data_file)
################################################################################



for currentFile in onlyfiles:
    
    original = cv2.imread(currentFile) # load image

    contrasted = contrast_stretch(original)
    cv2.imwrite(currentFile + '_1_CONTRASTED.png', contrasted) ## è possibile cancellare questa riga nella versione finale del programma
    ndvi = calc_ndvi(contrasted)
    cv2.imwrite(currentFile + '_2_NDVI_ORIGINAL.png', ndvi) ## è possibile cancellare questa riga nella versione finale del programma
    ndvi_contrasted = contrast_stretch(ndvi)
    cv2.imwrite(currentFile + '_3_NDVI_CONTRASTED.png', ndvi_contrasted)
    color_mapped_prep = ndvi_contrasted.astype(np.uint8)
    
    color_mapped_image = cv2.applyColorMap(color_mapped_prep, fastiecm)
    cv2.imwrite(currentFile + '_4_NDVI_.png', color_mapped_image)
    print('NDVI_' + currentFile + '.png')

    color_mapped_image_IS = cv2.applyColorMap(color_mapped_prep, fastiecm_IS)
    cv2.imwrite(currentFile + '_5_IS_.png', color_mapped_image_IS)
    print('IS_' + currentFile + '.png')
    IS_pixel_count(currentFile + '_5_IS_.png')

    color_mapped_image_IF = cv2.applyColorMap(color_mapped_prep, fastiecm_IF)
    cv2.imwrite(currentFile + '_6_IF_.png', color_mapped_image_IF)
    print('IF_' + currentFile + '.png')
    IF_pixel_count(currentFile + '_6_IF_.png')

    color_mapped_image_IFH = cv2.applyColorMap(color_mapped_prep, fastiecm_IFH)
    cv2.imwrite(currentFile + '_7_IFH_.png', color_mapped_image_IFH)
    print('IFH_' + currentFile + '.png')
    IFH_pixel_count(currentFile + '_7_IFH_.png')
    


