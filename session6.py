# -*- coding: utf-8 -*-
"""Session6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mqr_MAR6ywYBs6buwD8RDz1MHbHocwZ4
"""

#Accessing the value
my_dict={'name':'bhanu','class':'b.c.a','age':20}
print(my_dict['age'])

print(my_dict.get('couse','nhi ha'))

#modifying or adding elements
my_dict['age']='23'

del my_dict['name']

my_dict

my_dict.pop('age')
my_dict

#keys()-------Will print all the keys in the dictionary
#values()------will print all the values in the dictionary
#items()-------this will print all the keys value pairs in the dictionary
#update()-----can add multiple key pair or we can say another dictionary in the existing dict
#clear()------will delete all the keys value pairs in the dict

#Booltype/Booleantype (True/False) is_passed=True
#is_placed=False
#in_class=False
#Nonetype
#classses=None