#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py
#                                                                             
# PROGRAMMER: KAOSARA BAKARE
# DATE CREATED: 23/06/2023
# PURPOSE: Create a function that retrieves the following 3 command line inputs 
#          from the user using the Argparse Python module. If the user fails to 
#          provide some or all of the 3 inputs, then the default values are
#          used for the missing inputs. Command Line Arguments:
#     1. Image Folder as --dir with default value 'pet_images'
#     2. CNN Model Architecture as --arch with default value 'vgg'
#     3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
#
##
# Imports python modules
import argparse

# 
def get_input_args():

    # Create Parse using ArgumentParser
#     the argument that are going to be used 
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir',default='pet_images/')
    parser.add_argument('--arch',default='vgg')
    parser.add_argument('--dogfile',default='dognames.txt')
    # Create 3 command line arguments as mentioned above using add_argument() from ArguementParser method
    
    
    # Replace None with parser.parse_args() parsed argument collection that 
    # you created with this function 
    return parser.parse_args()
