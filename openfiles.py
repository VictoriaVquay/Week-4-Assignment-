#open a file in read mode
#with open('example.txt', 'r') as file:
    #read the content of the file
   # content = file.read()
    #print the content of the file
    #print(content)

#open a file in write mode
with open('output.txt', 'w') as file:
    #write to the file
    file.write('Hello, Python World! This is wonderful! The Updates keep up')
    #print a message
    #print('File written successfully!')