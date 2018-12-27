import xml.etree.ElementTree as ET
from os import getcwd

import random

sets=[('traffic_light_train'), ('traffic_light_test')]

classes = ["trafficlight"]


def convert_annotation(image_id, list_file):
    in_file = open('traffic_dataset/annotations/trafficlight%s.xml'%(image_id))
    tree=ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

wd = getcwd()   # current working path

# 1 arrange train, val, test dataset:
# ids = list(range(1,200))
# random.shuffle(ids)
# train = ids[:150]
# test = ids[150:]
# dataset = [train, test]
# k = 0
# for image_set in dataset:
#     subset_name = sets[k]
#     k += 1
#     image_ids = open('traffic_dataset/%s.txt'%(subset_name), 'w')
#     for i in range(len(image_set)):
#         image_ids.write('%d\n'%(image_set[i]))
#     image_ids.close()


# 2 produce train, val, test data:
for image_set in sets:
    image_ids = open('traffic_dataset/%s.txt'%(image_set)).read().strip().split()
    list_file = open('traffic_dataset/%s_data.txt'%(image_set), 'w')
    for image_id in image_ids:
        list_file.write('traffic_dataset/images/trafficlight%s.jpg'%(image_id))
        convert_annotation(image_id, list_file)
        list_file.write('\n')
    list_file.close()