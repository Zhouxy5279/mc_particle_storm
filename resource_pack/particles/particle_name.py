# -*- coding: utf-8 -*-

# Author      - Zhou-xy
# Email       - zhouxy5279@qq.com
# Time        - 2023/7/20

import os


# 扫描所有particle文件,补全不含.particle的json文件
def particle_for_snow_storm(p='.'):
    file_list = os.listdir(p)
    for f in file_list:
        f_path = os.path.join(p, f)
        if f_path.endswith('.json'):
            if '.particle.json' not in f:
                new_path = f_path.replace('.json', '.particle.json')
                os.rename(f_path, new_path)
        
        if os.path.isdir(f_path):
            particle_for_snow_storm(f_path)


particle_for_snow_storm()