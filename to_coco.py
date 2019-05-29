import json
import os
import datetime
import cv2

def to_coco(SYMBOL):
    if SYMBOL=='test':
        target_dir = {}
        target_dir['info'] = {"year" : 2019, "version" : '1.0',
        "description" : 'VisDrone2019_det_' + SYMBOL +'_annotations_COCOformat',
        "contributor" : 'L&others', "url" : 'http://www.aiskyeye.com/views/index', "date_created" : datetime.date.today().ctime()}
        url = 'http://www.aiskyeye.com/views/index'
        data_time = datetime.date.today().ctime()
        print('1 done')

        images = []
        image_list = os.listdir(os.path.join('VisDrone2019-DET-test-challenge\VisDrone2018-DET-test-challenge','images'))
        for i, file_img in enumerate(image_list):
            path = os.path.join('VisDrone2019-DET-test-challenge\VisDrone2018-DET-test-challenge','images',file_img)
            img = cv2.imread(path)
            h, w, c= img.shape
            image = {'id': i, "width" : w, "height" : h, "file_name" : file_img, "license" : 1,
            "flickr_url" : url, "coco_url" : url, "date_captured" : data_time}
            images.append(image)
            # print(h,w)
        print('2 done')
        print('3 done')

        categories = [{"id" : 1, "name" : 'pedestrian', "supercategory" : 'human'},
        {"id" : 2, "name" : 'people', "supercategory" : 'human'},
        {"id" : 3, "name" : 'bicycle', "supercategory" : 'vehicle'},
        {"id" : 4, "name" : 'car', "supercategory" : 'vehicle'},
        {"id" : 5, "name" : 'van', "supercategory" : 'vehicle'},
        {"id" : 6, "name" : 'truck', "supercategory" : 'vehicle'},
        {"id" : 7, "name" : 'tricycle', "supercategory" : 'vehicle'},
        {"id" : 8, "name" : 'awning-tricycle', "supercategory" : 'vehicle'},
        {"id" : 9, "name" : 'bus', "supercategory" : 'vehicle'},
        {"id" : 10, "name" : 'motor', "supercategory" : 'vehicle'},
        {"id" : 11, "name" : 'others', "supercategory" : 'others'}]
        print('4 done')

        target_dir['license'] = {"id" : 1, "name" : 'MIT', "url" : url}

        target_dir['images'] = images
        # target_dir['annotations'] = annotations
        print('5 done')

        #json文件名称
        store_path=os.getcwd() + '/DET_' + SYMBOL + '.json'
        with open(store_path, 'w') as f:
            json.dump(target_dir, f)
        print('all done')
    
    if SYMBOL!='test':
        target_dir = {}
        target_dir['info'] = {"year" : 2019, "version" : '1.0',
        "description" : 'VisDrone2019_det_' + SYMBOL +'_annotations_COCOformat',
        "contributor" : 'L&others', "url" : 'http://www.aiskyeye.com/views/index', "date_created" : datetime.date.today().ctime()}
        url = 'http://www.aiskyeye.com/views/index'
        data_time = datetime.date.today().ctime()
        print('1 done')

        images = []
        image_list = os.listdir(os.path.join('VisDrone2019-DET-'+ SYMBOL +'\VisDrone2018-DET-' + SYMBOL,'images'))
        for i, file_img in enumerate(image_list):
            path = os.path.join('VisDrone2019-DET-'+ SYMBOL +'\VisDrone2018-DET-' + SYMBOL,'images',file_img)
            img = cv2.imread(path)
            h, w, c= img.shape
            image = {'id': i, "width" : w, "height" : h, "file_name" : file_img, "license" : 1,
            "flickr_url" : url, "coco_url" : url, "date_captured" : data_time}
            images.append(image)
            # print(h,w)
        print('2 done')

        annotations = []
        annotation_list = os.listdir(os.path.join('VisDrone2019-DET-'+ SYMBOL +'\VisDrone2018-DET-' + SYMBOL,'annotations'))
        annotation_num = 0
        for i, file_anno in enumerate(annotation_list):
            img_index = file_anno.split('.')[0] + '.jpg'
            image_id = image_list.index(img_index)
            with open(os.path.join('VisDrone2019-DET-'+ SYMBOL +'\VisDrone2018-DET-' + SYMBOL,'annotations',file_anno), 'r') as f:
                for line in f.readlines():
                    curline = line.strip().split(',')
                    if int(curline[4])==0:
                        continue
                    annotation = {"id" : annotation_num, "image_id" : image_id, "category_id" : int(curline[5]),
                    "segmentation" : [[]], "area" : float(curline[2])*float(curline[3]),
                    "bbox" : [int(curline[0])+int(int(curline[2])/2), int(curline[1])-int(int(curline[3])/2), int(curline[2]), int(curline[3])],
                    "iscrowd" : int(bool(curline[7]))}
                    annotation_num += 1
                    annotations.append(annotation)
        print('3 done')

        categories = [{"id" : 1, "name" : 'pedestrian', "supercategory" : 'human'},
        {"id" : 2, "name" : 'people', "supercategory" : 'human'},
        {"id" : 3, "name" : 'bicycle', "supercategory" : 'vehicle'},
        {"id" : 4, "name" : 'car', "supercategory" : 'vehicle'},
        {"id" : 5, "name" : 'van', "supercategory" : 'vehicle'},
        {"id" : 6, "name" : 'truck', "supercategory" : 'vehicle'},
        {"id" : 7, "name" : 'tricycle', "supercategory" : 'vehicle'},
        {"id" : 8, "name" : 'awning-tricycle', "supercategory" : 'vehicle'},
        {"id" : 9, "name" : 'bus', "supercategory" : 'vehicle'},
        {"id" : 10, "name" : 'motor', "supercategory" : 'vehicle'},
        {"id" : 11, "name" : 'others', "supercategory" : 'others'}]
        print('4 done')

        target_dir['license'] = {"id" : 1, "name" : 'MIT', "url" : url}

        target_dir['images'] = images
        target_dir['annotations'] = annotations
        print('5 done')

        #json文件名称
        store_path=os.getcwd() + '/DET_' + SYMBOL + '.json'
        with open(store_path, 'w') as f:
            json.dump(target_dir, f)
        print('all done')


if __name__=='__main__':
    to_coco('test')