# Accept text file as input corpuses 
import os
import re 
os.getcwd()
#os.mkdir("Lab1")
#os.chdir("Lab1")
def intial_setup():
    folder_name=input("Enter a folder name")
    os.mkdir(folder_name)
    os.chdir(folder_name)
    os.getcwd()
    Corpuse = dict()
    
    for i in range(1,6):
        file_name=input("Enter File name "+str(i))
        f=open(file_name,"w+")
        Contents= input("Enter File Contents")
        Corpuse[file_name]= Contents
        f.write(Contents)
        f.close
    return Corpuse
  def search(Corpuse):
    regex = str(input("Enter a regular Expression to search "))
    # regex = re.compile(regex)
    # inargass 'str'> <class 'str'>
    for file,contents in Corpuse.items():
        txt = str(contents)
        res = re.search(regex,contents)
        if res!= None:
            # print("Found patren {}  as {}  in ' {} ' ".format(regex,highlight_one(contents,res.group()),file
            print("Found patren {}  as {}  in ' {} ' ".format(regex,res.group(),file))
        else:
            print("No pattren found in '{}' ".format(file))
