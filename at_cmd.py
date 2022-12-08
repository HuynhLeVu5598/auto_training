
import os

import shutil

import datetime 

import subprocess


def time_to_name():
    current_time = datetime.datetime.now() 
    name_folder = str(current_time)
    name_folder = list(name_folder)
    for i in range(len(name_folder)):
        if name_folder[i] == ':':
            name_folder[i] = '-'
        if name_folder[i] == ' ':
            name_folder[i] ='_'
        if name_folder[i] == '.':
            name_folder[i] ='-'
    name_folder = ''.join(name_folder)
    return name_folder


import time
img_size = 416
epoch = 300


# điền 5 thông số
while True:
    # vd: '08'
    # số giờ
    hour = time.strftime("%H")
    if hour ==  '08':
        # đường dẫn chứa file train và valid
        # vd: 'C:/abc'
        path_input_move = r"C:\Users\AICCSX\Desktop\Hieu\C1"


        # tên classes
        # vd: ['loi1','loi2']
        myclasses5 = ['di_vat','me','kim_nam_cham','nut','nam_cham_cao','kim_cao','di_vat_duoi','tray_bac_truc','kim_bien_dang','kim_ri_set']



        # đường dẫn lưu kết quả
        # vd: 'C:/save'
        path_save = r"C:\Users\AICCSX\Desktop\Hieu\model_c1"


        # tên file
        # vd: 'abc'
        name_save = "A47_A19_C1_01102022_Finallun"



        if os.path.isdir(os.getcwd() + '/train'):
            shutil.rmtree(os.getcwd() + '/train')
        if os.path.isdir(os.getcwd() + '/valid'):
            shutil.rmtree(os.getcwd() + '/valid')
        shutil.copytree(path_input_move + '/train',os.getcwd() + '/train')
        shutil.copytree(path_input_move + '/valid',os.getcwd() + '/valid')


        #myclasses5 = []
        # texts5 = values['input_classes7'].split('\n')
        # for text in texts5:
        #     myclasses5.append(text)

        with open(os.getcwd() + '/levu/data.yaml', "w") as f:
            f.write('train: ' + os.getcwd() + '/train/images')
            f.write('\n')
            f.write('val: ' + os.getcwd() + '/valid/images')
            f.write('\n')
            f.write('nc: '  + str(len(myclasses5)))     
            f.write('\n')
            f.write('names: '  + str(myclasses5))     

        with open(os.getcwd() + '/levu/models/levu.yaml', "w") as f:
            f.write('nc: ' +  str(len(myclasses5)) + '\n' + 
                    'depth_multiple: 0.33  # model depth multiple' + '\n' + 
                    'width_multiple: 0.50  # layer channel multiple' + '\n' + 
                    'anchors:' + '\n' + 
                    '  - [10,13, 16,30, 33,23]  # P3/8' + '\n' + 
                    '  - [30,61, 62,45, 59,119]  # P4/16' + '\n' + 
                    '  - [116,90, 156,198, 373,326]  # P5/32' + '\n' + 

                    'backbone:' + '\n' + 

                    '  [[-1, 1, Conv, [64, 6, 2, 2]],  # 0-P1/2' + '\n' + 
                    '   [-1, 1, Conv, [128, 3, 2]],  # 1-P2/4' + '\n' + 
                    '   [-1, 3, C3, [128]],' + '\n' + 
                    '   [-1, 1, Conv, [256, 3, 2]],  # 3-P3/8' + '\n' + 
                    '   [-1, 6, C3, [256]],' + '\n' + 
                    '   [-1, 1, Conv, [512, 3, 2]],  # 5-P4/16' + '\n' + 
                    '   [-1, 9, C3, [512]],' + '\n' + 
                    '   [-1, 1, Conv, [1024, 3, 2]],  # 7-P5/32' + '\n' + 
                    '   [-1, 3, C3, [1024]],' + '\n' + 
                    '   [-1, 1, SPPF, [1024, 5]],  # 9' + '\n' + 
                    '  ]' + '\n' + 

                    'head:' + '\n' + 
                    '  [[-1, 1, Conv, [512, 1, 1]],' + '\n' + 
                    "   [-1, 1, nn.Upsample, [None, 2, 'nearest']]," + '\n' + 
                    '   [[-1, 6], 1, Concat, [1]],  # cat backbone P4' + '\n' + 
                    '   [-1, 3, C3, [512, False]],  # 13' + '\n' + 

                    '   [-1, 1, Conv, [256, 1, 1]],' + '\n' + 
                    "   [-1, 1, nn.Upsample, [None, 2, 'nearest']]," + '\n' + 
                    '   [[-1, 4], 1, Concat, [1]],  # cat backbone P3' + '\n' + 
                    '   [-1, 3, C3, [256, False]],  # 17 (P3/8-small)' + '\n' + 

                    '   [-1, 1, Conv, [256, 3, 2]],' + '\n' + 
                    '   [[-1, 14], 1, Concat, [1]],  # cat head P4' + '\n' + 
                    '   [-1, 3, C3, [512, False]],  # 20 (P4/16-medium)' + '\n' + 

                    '   [-1, 1, Conv, [512, 3, 2]],' + '\n' + 
                    '   [[-1, 10], 1, Concat, [1]],  # cat head P7' + '\n' + 
                    '   [-1, 3, C3, [1024, False]],  # 23 (P5/32-large)' + '\n' + 

                    '   [[17, 20, 23], 1, Detect, [nc, anchors]],  # Detect(P3, P4, P5)' + '\n' + 
                    '  ]'
                    )




        dir_py5 = os.path.join(os.getcwd()  + '/levu/' , 'hlvtrain.py')
        dir_data5 = os.path.join(os.getcwd()  + '/levu/' , 'data.yaml')
        dir_model5 = os.path.join(os.getcwd()  + '/levu/models/' , 'levu.yaml')
        name_folder = time_to_name()
        program_dir5 = [ dir_py5, ' --img ', str(img_size), ' --batch ', '6' ,' --epochs ', '{}'.format(int(epoch)) , ' --data ', dir_data5 , ' --cfg ', dir_model5, ' --weights ', '""', ' --name ', 'my_results' + '{}'.format(name_folder),  ' --cache']

        subprocess.call(['python', program_dir5])
        shutil.copyfile(os.getcwd() + '/levu/runs/train/my_results'+ name_folder +'/weights/best.pt',path_save + '/' + name_save + '.pt')

        shutil.copyfile(os.getcwd() + '/levu/result.txt',path_save + '/' + 'result.txt')
        break
