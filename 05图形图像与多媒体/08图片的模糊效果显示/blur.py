# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队   ：明日科技
# 开发人员   ：小科
# 开发时间   ：2019/4/8  15:31 
# 文件名称   ：blur.PY
# 开发工具   ：PyCharm
"""
  图片的模糊效果显示
"""
from PIL import Image,ImageFilter
img=Image.open('模糊效果原图.png') # 打开图片文件
newimg=img.filter(ImageFilter.BLUR) # 设置图片筛选器
newimg.save('模糊效果.png', 'png') # 保存模糊效果的图片