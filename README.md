
# WLB Test Assignement

This project is a coding test assignement which consists in implementing for three differents problems three
parameterized python functions. Including a test set of minimum of 2 unit tests per function to verify that the
implementation works as expected. 

## Authors

- [@HamzaRakkabi]


## Running Tests

To run the unit tests, run the following command:

**Function1: contains 4 unit tests as follow**
```bash
  pytest Test_Assignement_WBX.py::test_UT1_function1
  pytest Test_Assignement_WBX.py::test_UT2_function1
  pytest Test_Assignement_WBX.py::test_UT3_function1
  pytest Test_Assignement_WBX.py::test_UT4_function1
```

**Function2: contains 3 unit tests as follow**               
***Note**: Please make sure you have also downloaded the attached directory "main_directory" in the same file directory as the project to run properly the test-set.*
```bash
  pytest Test_Assignement_WBX.py::test_UT1_function2
  pytest Test_Assignement_WBX.py::test_UT2_function2
```

**Function3: contains 5 unit tests as follow**
```bash
  pytest Test_Assignement_WBX.py::test_UT1_function3
  pytest Test_Assignement_WBX.py::test_UT2_function3
  pytest Test_Assignement_WBX.py::test_UT3_function3
  pytest Test_Assignement_WBX.py::test_UT4_function3
  pytest Test_Assignement_WBX.py::test_UT5_function3
```
## Installation

No installation is needed.
    
## Demo

Below is an PyTest execution demo of each written function:               
https://imagizer.imageshack.com/img923/2323/1UeL7e.png
https://imagizer.imageshack.com/img923/4299/k5pzrM.png
https://imagizer.imageshack.com/img922/1031/dxyeiZ.png
## Appendix

Note: many function sets and procedures have been tried for this implementation where only the ones with low Time & Space complexity have selected. 

## Usage
**Function1 implementation is a follow:**
```
================================================================
Function 1: return first file that meets the input requirements
================================================================

 #=------------------------------ Implementation -----------------------------#
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

 #=-------------------------------- Test Units --------------------------------#
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
        array2 =[17, 17.7, 17, 17, 17,11]
        assert first_repeated_num(array1, array2) == 17.7
```

**Function2 implementation is a follow:**
```
#================================================================
#Function 2: return first file that meets the input requirements.
#================================================================

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
```

**Function3 implementation is a follow:**
```
#===================================================================================================
#Function 3: finds the minimum quantity of permutations so that a binary sequence ends interspersed.
#===================================================================================================  

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