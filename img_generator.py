# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 15:10:49 2022

@author: Maximilian
"""

# import section ------------------------------------------------------------ #
from PIL import Image
from random import randint as rint

a = (rint(0,255), rint(0,255), rint(0,255))
b = (rint(0,255), rint(0,255), rint(0,255))

cross_lst = [
    
    0, 0, 1, 1, 1, 0, 0,
    0, 0, 1, 1, 1, 0, 0,
    1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1,
    0, 0, 1, 1, 1, 0, 0,
    0, 0, 1, 1, 1, 0, 0
           
           ]

square_lst = [
    
    0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 0,
    0, 1, 1, 1, 1, 1, 0,
    0, 1, 1, 1, 1, 1, 0,
    0, 1, 1, 1, 1, 1, 0,
    0, 1, 1, 1, 1, 1, 0,
    0, 0, 0, 0, 0, 0, 0
           
           ]

input_lst = [cross_lst, square_lst]


def generate_images(lst_lst, w, h, num, name, mode):
    
    counter = 1
    
    for i in range(num):
        
        a = (rint(0,255), rint(0,255), rint(0,255))
        b = (rint(0,255), rint(0,255), rint(0,255))
        c = rint(0, len(lst_lst)-1)
        path = "{name}_".format(name=name) + "{counter}.png".format(counter=counter).zfill(10)
        
        img = Image.new(mode, (w, h))
        input_lst = [a if x==0 else b for x in (lst_lst[c])]
        
        img.putdata(input_lst)
        img.save(path)
        counter += 1

generate_images(input_lst, 7, 7, 10000, "generated_images_square_cross/test_image", "RGB")



