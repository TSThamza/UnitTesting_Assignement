# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 14:40:19 2022
@author: hamza rakkabi
"""

"""
===================================================================
Function2: return the first file that meets the input requirements.
===================================================================
"""

import os
import win32security

#For this exercie I found the fastest solution can be using Python's walk    
def get_file_owner(file):
    sd = win32security.GetFileSecurity (file, win32security.OWNER_SECURITY_INFORMATION)
    owner_sid = sd.GetSecurityDescriptorOwner ()
    file_owner, domain, type = win32security.LookupAccountSid (None, owner_sid)
    return(file_owner)

def get_file_size(file):
    return os.stat(file).st_size

def search_through_path(input_path):
    result="no file match"   
    #health check for the input path 
    if os.path.isdir(input_path):            
        #Necessary to check all folders and sub-folders too                                                                                         
        for root, subdirectories, files in os.walk(input_path):
            for file in files:
             file_pth=os.path.join(root, file)                                                                                  
             if (get_file_size(file_pth)<14*2**20) and (file_pth.split(".")[-1]=="exe") and (get_file_owner(file_pth)=="admin"):
              return file                                                               
    return result

def test_UT1_function2():  
     input_path="./main_directory/"
     assert search_through_path(input_path) == "HelloWorld.exe"
     
def test_UT2_function2():
     input_path="./main_directory/test_directory/dist/"
     assert search_through_path(input_path) == "HelloWorld.exe"