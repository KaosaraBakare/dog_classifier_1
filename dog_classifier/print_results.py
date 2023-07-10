#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: KAOSARA BAKARE
# DATE CREATED:24/06/2023
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It 
#          should also allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results 
#          dictionary (results_dic).  
#         This function inputs:
#            -The results dictionary as results_dic within print_results 
#             function and results for the function call within main.
#            -The results statistics dictionary as results_stats_dic within 
#             print_results function and results_stats for the function call within main.
#            -The CNN model architecture as model wihtin print_results function
#             and in_arg.arch for the function call within main. 
#            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.
##

# 
def print_results(results_dic, results_stats_dict, model, 
                  print_incorrect_dogs = False, print_incorrect_breed = False):
    


                
    print('N Images: {}'.format(results_stats_dict['n_images']))
    print('N dog Images: {}'.format(results_stats_dict['n_dogs_img']))
    print('N not dog Images: {}'.format(results_stats_dict['n_notdogs_img']))
    print("\nsUMMARY STATISTICS ON MODEL:")
    for key in results_stats_dict:
        if key[0] == 'p':
            print(key,results_stats_dict[key])
    if (print_incorrect_dogs and ((results_stats_dict['n_correct_dogs'] + results_stats_dict['n_correct_notdogs'] ) != results_stats_dict['n_images'])):
        print("\nincorrect dog")
        for key in results_dic:
            if ((results_stats_dict[key][3] == 1) and  (results_stats_dict[key][4] == 0)):
                print("\npet label:{}, classifier label:{}".format(results_dic[key][0],results_dic[key][1]))
            elif ((results_dic[key][3] == 0) and (results_dic[key][4] == 1)):
                 print("\nlabel:{}","\nclassier label:{}",format(results_dic[key][0],results_dic[key][1]))
    if (print_incorrect_breed and (results_stats_dict['n_correct_dogs'] != results_stats_dict['n_correct_breed'])):
                print("\nincorrect dog breed")
                for key in results_dic:
                    if sum(results_dic[key][3:]) == 2 and results_dic[key][2] == 0:
#                         line 86 and 87 are just for debugging, not relevant
#                         print("Key:",key)
#                         print("results_dic[key][2]:",results_dic[key][2])
# print the incorrect dog breeds against the classifier 
                        print('Real:{} , Classifier:  {}'.format(results_dic[key][0], results_dic[key][1]) )
    return None
    