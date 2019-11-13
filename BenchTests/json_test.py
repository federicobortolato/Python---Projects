#json encoding test
import json
#defining some variables
a = 0
b = 1
c = 'ok'
d = True
e = False
f = [0 , 1]
g = (2 , 3)

name = 'GIGI'
surname = 'HADID'

h = {'name' : name , 'surname' : surname}
#listing them
abc = [a,b,c,d,e,f,g,h]

import inspect
#retrieve the variable's name depending on the variable level (i.e. the last time you redefine
#a variable (level=top) with grade==1)
def retrieve_name(var,grade):
    if grade == 1:
        callers_local_vars = inspect.currentframe().f_back.f_locals.items()
        return [var_name for var_name, var_val in callers_local_vars if var_val is var]
    elif grade == 2:
        callers_local_vars = inspect.currentframe().f_back.f_back.f_locals.items()
        return [var_name for var_name, var_val in callers_local_vars if var_val is var]
    elif grade == 3:
        callers_local_vars = inspect.currentframe().f_back.f_back.f_back.f_locals.items()
        return [var_name for var_name, var_val in callers_local_vars if var_val is var]
    else:
        raise(IndexError('Variables inspecting level out of range. If needed add one'))
        pass
#indexing all variables in a dictionary
def create_dic(iter_list):
    dic = {}
    for x in iter_list:
        dic[retrieve_name(x,2)[0]] = x
    return dic

old_dic = create_dic(abc)

#actual json module at work

#saving data to .json file
with open('json_test_encoded_files.json', 'w') as file:
    json.dump(old_dic , file , indent = 8 , separators = (', ' , ': ') , sort_keys = True)
#loading data from .json file
with open('json_test_encoded_files.json', 'r') as file:
    new_dic = json.load(file)

#printing some output to check how the conversion and reconversion works
print('\ndictionary before json conversion:\n')
print('\nold_dic:\n' , old_dic, '\n')

print('\ndictionary in the json file, converted:\n')
with open('json_test_encoded_files.json', 'r') as file:
    content = file.read()

print('\njson file:\n', content, '\n')

print('\ndictionary after json reconversion:\n')
print('\nnew_dic:\n' , new_dic, '\n')

print('testing complete')
