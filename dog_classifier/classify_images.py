#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: KAOSARA BAKARE
# DATE CREATED:  24/06/2023
# PURPOSE: Create a function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function 
#             and as in_arg.dir for function call within main. 
#            -The results dictionary as results_dic within classify_images 
#             function and results for the functin call within main.
#            -The CNN model architecture as model wihtin classify_images function
#             and in_arg.arch for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           classifier label as the item at index 1 of the list and the comparison 
#           of the pet and classifier labels as the item at index 2 of the list.
#
##
# Imports classifier function for using CNN to classify images 
from classifier import classifier 


# 
def classify_images(image_dir, results_dic, model):
      


#     function for classifying the image
    for key in results_dic:
#         for the path creation stating the image directory and the key to look for
        path = image_dir + key
        model_label = classifier(path, model)
        clean_model_label = model_label.strip().lower()
        truth = results_dic[key][0]
        if truth in clean_model_label:
            results_dic[key].extend([clean_model_label,1])
        else:
            results_dic[key].extend([clean_model_label,0])
#             basically to create the file directory in dictionary format 
    for key in results_dic:
        print("\nFile name", key, "\nPet image label=",results_dic[key][0],"\nclassifier label=", results_dic[key][1],"\nmatch=",results_dic[key][2])
    return None 
            
        
        
      