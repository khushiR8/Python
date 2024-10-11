import shutil
source = input("Enter the name of the source file: ")
source = source + '.txt'
destination = input("Enter the name of he destination file: ")
destination = destination + '.txt'
shutil.copy(source,destination)