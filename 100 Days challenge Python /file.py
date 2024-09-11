# f = open('myfile.txt', 'r')
# text = f.read()
# print(text)
# f.close()


# f = open('myfile.txt', 'w')
# f.write("Dhrubo")
# f.close()
#
# with open('myfile.txt', 'a')as f:
#     f.write("LOL")




# with open('file.txt', 'r') as f:
#     print(type(f))
#
#     f.seek(10)  # Move to the 10th byte of the file
#     print(f.tell())
#     data = f.read(7) # Read the data next 5 bytes
#     print(data)

with open('sample.txt', 'w') as f:
    f.write("Hello, world!")
    f.truncate(5)

    with open('sample.txt', 'r') as f:
        print(f.read())