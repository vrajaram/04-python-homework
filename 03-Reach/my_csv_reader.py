import os.path

# 1. Check if the boston housing dataset file path is really a file.
# If it is print I have a file to process, otherwise print Boo, no file for me.


# 2 ways to check the file exists
# OS library
# try except
if os.path.isfile('housing.data'):
    print("I have a file to process")
else:
    print("Boo, no file for me")

# 2. Read the boston housing dataset file
# 3. Print the dataset line by line
try:
    f = open('housing.data','r')
    for line in f:
        print(line, end='')
    f.close()

# 4. Modify this script by printing each line as a list of values.
    f = open('housing.data','r')
    for line in f:
        li = list(line.split("  "))
        print(li)

except IOError:
    print("Boo, no file for me")
finally:
    f.close()
