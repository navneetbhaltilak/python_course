with open('myfile2.txt','w') as f:
    f.write('Hello World, My name is Navneet')
    #to define the size of a file or delete the extra things use truncate(size)
    f.truncate(15)
with open('myfile2.txt','r') as f:
    print(type(f))
    #to move to the 10th byte of the file you need to use the following keyword
    f.seek(10)
    #to know where we are in the file we have to use tell
    current_position=f.tell()
    print(current_position)
    #to read specific numbers of bytes you have to use read(length)
    data=f.read(5)
    print(data)
