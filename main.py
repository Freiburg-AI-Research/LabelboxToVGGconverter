
print('Start program')

file_name = 'labelbox.json' #filename.json

import json
# import numpy as np
# import os
# from PIL import Image, ImageDraw


print('Open label JSON')

with open(file_name) as json_file:
    labelbox_data = json.load(json_file)

images = []

print('Create info from JSON')

for data_row in labelbox_data:

    image = {}
    image['filename'] = data_row['External ID']

    regions = []

    #Append polygonoms
    for poly in data_row['Label']['objects']:
        region = {}

        points = [[], []]

        if 'polygon' in poly:
            for pnt in poly['polygon']:
                points[0].append(int(pnt['x']))
                points[1].append(int(pnt['y']))

            region['shape_attributes'] = {
                'name': 'polygon',
                'all_points_x': points[0],
                'all_points_y': points[1]
            }
        else:
            region['shape_attributes'] = {
                'name': 'point',
                'cx': int(poly['point']['x']),
                'cy': int(poly['point']['y'])
            }

        region['region_attributes'] = {
            'keypoint': poly['title']
        }

        regions.append(region)

    image['regions'] = regions
    images.append(image)



print('Create new JSON structure')

via_labels = {}

for img in images:
    via_labels[img['filename']] = img

print('Export JSON')

with open('via_region_data.json', 'w') as outfile:
    json.dump(via_labels, outfile)

print('via labels JSON exported')