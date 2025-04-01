try:
    file=open('example.txt', 'r')
    data=file.read()
    print(data)
except FileNotFoundError:
    print("File not found.")
finally:    
    file.close()
    print("File closed successfully.")
