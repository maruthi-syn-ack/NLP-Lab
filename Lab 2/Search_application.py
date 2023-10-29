# Author : MARUTHI R (github.com/maruthi-syn-ack)
# Required Libraries
import os
import re 
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

def highlight(match):
    return f'\033[91;1m{match.group()}\033[0m'

def search(Corpuse):
    regex = str(input("Enter a regular Expression to search "))
    regex = re.compile(regex)
    for file,contents in Corpuse.items():
        txt = str(contents)
        res = re.search(regex,contents)
        if res!= None:
            mod_str = re.sub(res.group(),highlight(res),res.string) # modifiy the string to highlight the pattren
            print("Found patren {}  as {}  in ' {} ' ".format(regex,mod_str,file))
        else:
            print("No pattren found in '{}' ".format(file))

def main():
    Corpuse = intial_setup()
    search(Corpuse)

if __name__ == "__main__":
    main()
