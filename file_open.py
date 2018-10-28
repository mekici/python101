# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 10:01:10 2018

@author: Murat Ekici
"""
import os #bu sınıfın importuna sadece dosya ismi düzenleme ve silme işlemlerinde gerek var

#dosyadan okuma
fh = open("list_comprehension.txt", "r")
result = [satir for satir in fh if "satir" in satir]
print (result)
fh.close()

fileObject = open("list_comprehension.txt", "r+")
print(fileObject.name)
print(fileObject.mode)
print(fileObject.readline())
fileObject.write("\n dosyaya yazıyorum")
print(fileObject.read())
fileObject.close()

fileCreateObject = open("file_operations.txt","w+")

fileCreateObject.write(str(result))
fileCreateObject.read()
fileCreateObject.close()

os.rename("file_operations.txt", "file_declarations.txt") #dosya adını değiştirir

os.remove("file_declarations.txt") #dosyayı siler

"""
"R" Opens file for read only
"r+" Opens file for reading and writing
"Rb" Only Read file in binary
"rb+" Opens file to read and write in binary
"W" Opens file to write only. Overwrites existing files with same name, If file does not exist, it creates a new file
"Wb" Opens file to write only in binary. Overwrites existing files with same name
"w+" Opens file for reading and writing
"Wb" Opens file to read and write in binary. Overwrites existing files with same name
"A" Opens a file for appending content at the end of the file, If file does not exist, it creates a new file.
"a+" Opens file for appending as well as reading content
"Ab" Opens a file for appending content in binary
"ab+" Opens a file for reading and appending content in binary
"X" Creates a new file. If file already exists, the operation fails.

"""

