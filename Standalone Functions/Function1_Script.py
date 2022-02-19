# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 14:30:51 2022
@author: hamza rakkabi
"""

"""
=============================================================================
Function1: return the first repeated number from 2 differents integer array.
=============================================================================
"""

#For this exercie I found the fastest solution can be using Python's sets   
def unique_items(array):
    #Remove duplicates from each array and Keep the Order
	return (sorted(set(array), key=array.index))
    
def first_repeated_num(array1, array2):
   ref_set = set()
   no_duplicate = -1
   #concating only unique items from each array in one single array
   array=unique_items(array1)+unique_items(array2)
   
   #making sure all items are integers as been requiered, if not return -1
   if(all(isinstance(i, int) for i in array)):
    #checking item by item once a there's match break the function and return it back. 
    for i in range(len(array)):
        if array[i] in ref_set:
            return array[i]
        else:
            ref_set.add(array[i])
   return no_duplicate

def test_UT1_function1():
    #friendly error message in case of exception
        array1 =[2,4,0,5,17,233,0,0,2,5]
        array2 =[107,121,4,7,5,411,41,1,1000,10,127,17]
        assert first_repeated_num(array1, array2) == 17
    
def test_UT2_function1():
    #friendly error message in case of exception
        array1 =[1,4,0,5,177,233,0,33,2,5]
        array2 =[17, 17, 17, 17, 17,11]
        assert first_repeated_num(array1, array2) == -1
    
def test_UT3_function1():
    #friendly error message in case of exception
        array1 =[]
        array2 =[0,0, 0, 0, 0,1]
        assert first_repeated_num(array1, array2) == 0

def test_UT4_function1():
    #friendly error message in case of exception
        array1 =[1,4,0,5,17.7,233,0,33,2,5]
        array2 =[17, 17.7, 17, 17, 17,1]
        assert first_repeated_num(array1, array2) == 1
    
    
 