# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 14:30:51 2022

@author: hamza rakkabi
"""

"""
===================================================================================================
Function 3: finds the minimum quantity of permutations so that a binary sequence ends interspersed.
===================================================================================================
"""

#health check to valid the input sequence (with only haids & tails) 
def binarity_health_check(coin):
    sides = {'0', '1'}
    return True if (coin==sides or coin == {'0'} or coin == {'1'}) else False

def flips_min_permutation(sequence):
    flip_Count = 0
    seq_len=len(sequence)
    #if it's a valid binary sequence and with more than 1 char in length proceed, if not return -1
    if binarity_health_check(set(sequence)) or seq_len<=1:
    #based on the index position parity (odd & even) + the current coin side => counter will be couting
        for x in range(0, seq_len):
            if x % 2 == 0 and sequence[x] == '1':
                flip_Count += 1
            if x % 2 == 1 and sequence[x] == '0':
                flip_Count += 1
        return min(flip_Count,seq_len - flip_Count)
    else:
        return -1

def test_UT1_function3():  
     input_seq="0001010111"
     assert flips_min_permutation(input_seq) == 2
     
def test_UT2_function3():
     input_seq="0110"
     assert flips_min_permutation(input_seq) == 2
     
def test_UT3_function3():
    input_seq="3110101010110"
    assert flips_min_permutation(input_seq) == -1
    
def test_UT4_function3():
    input_seq="1"
    assert flips_min_permutation(input_seq) == -1
    
def test_UT5_function3():
    input_seq="010101010101010101"
    assert flips_min_permutation(input_seq) == 0 
        
    
    
 