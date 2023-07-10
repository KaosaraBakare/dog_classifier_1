#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: KAOSARA BAKARE
# DATE CREATED:  24/06/2023
# PURPOSE: Create a function adjust_results4_isadog that adjusts the results 
#          dictionary to indicate whether or not the pet image label is of-a-dog, 
#          and to indicate whether or not the classifier image label is of-a-dog.
#          All dog labels from both the pet images and the classifier function
#          will be found in the dognames.txt file. We recommend reading all the
#          dog names in dognames.txt into a dictionary where the 'key' is the 
#          dog name (from dognames.txt) and the 'value' is one. If a label is 
#          found to exist within this dictionary of dog names then the label 
#          is of-a-dog, otherwise the label isn't of a dog. Alternatively one 
#          could also read all the dog names into a list and then if the label
#          is found to exist within this list - the label is of-a-dog, otherwise
#          the label isn't of a dog. 
#         This function inputs:
#            -The results dictionary as results_dic within adjust_results4_isadog 
#             function and results for the function call within main.
#            -The text file with dog names as dogfile within adjust_results4_isadog
#             function and in_arg.dogfile for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           whether or not the pet image label is of-a-dog as the item at index
#           3 of the list and whether or not the classifier label is of-a-dog as
#           the item at index 4 of the list. Note we recommend setting the values
#           at indices 3 & 4 to 1 when the label is of-a-dog and to 0 when the 
#           label isn't a dog.
#
##
def adjust_results4_isadog(results_dic, dogfile):



    #creating dogname dictionary
    dogname_dict = dict()
    with open(dogfile,'r') as dog_file:
#         opening and reading the file and also reading it line by line
        dog_line = dog_file.readline()
        while dog_line != "":
            dog_line = dog_line.lower().strip()
#             truncating the line read with th strip method
            if dog_line not in dogname_dict:
                dogname_dict[dog_line] = 1
            else:
                print("It already exist")
            dog_line = dog_file.readline()
    for key in results_dic:
#         for checking the keys and seeing if it's in the dict then extends a tuple depends on the condition given
        if results_dic[key][0] in dogname_dict:
            if results_dic[key][1] in dogname_dict:
                results_dic[key].extend((1,1))
            else:
                results_dic[key].extend((1, 0))
        else:
            if results_dic[key][1] in dogname_dict:
                      results_dic[key].extend((0,1))
            else:
                results_dic[key].extend((0, 0))                      
    return None               
                      
                
            
        
    