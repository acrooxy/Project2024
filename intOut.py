myfile = open('myfile.txt')

print(myfile.read())
myfile.seek(0) #To read the file again you need to bring cursor back to the beggining of the file
print(myfile.read())

contents = myfile.read()
myfile.seek(0)
contents = myfile.readline() # use readline to grab a list
print(contents)

myfile.close() #Remember to close file
with open('myfile.txt', 'w') as f:
    f.write(contents)

# mode='r' Read only
# mode='w' Write only (can create new file)
# mode='a' Appending only (will add on to files
# mode='r+' reading and writing
# mode='w+' writing and reading (Overwrites existing files or creates a new file!)

with open('myTestFile.txt', 'w+') as f:
    f.write('This is a first line \n And a second line')
    print(f)
    f.close()


#Windows
# NewPathFile = open("C:\\Users\\UserName\\Folder\\test.txt")

#LINUX
# NewPathFile = ("/Users/YouUserName/Folder/myfile.txt

