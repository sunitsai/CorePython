'''
Created on Jul 26, 2019

@author: SUNIT
'''
# s = str("Hello this is my file management program")
# file = open("test","w")
# file.write(s)
# file.close()
# print("File Created")
# 
# 
# file = open("test","r")
# print(file.tell())
# 
# filecontent = file.read()
# print(filecontent)


file = open("Listfile","w")
list1 = ["Hello Python","Hello Ram","Hello Mohan","Hello MI"]
file.writelines(list1)
 
file.close()
print("File Created")

file = open("Listfile","r")
list1 = file.readlines()
print(list1)
