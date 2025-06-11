import sys
import os
import filecmp

def CompareFiles(Fname, keyword):
    if(os.path.isabs(Fname) == False):
        Fname = os.path.abspath(Fname)

    if(os.path.exists(Fname) == False):
        print("path does not exists : ", Fname)
        exit()
    
    if(os.path.isfile(Fname) == False):
        print("Path is valid but it is not a file : ", Fname)       
        exit()
    
    fobj = open(Fname, 'r')
    data = fobj.read()

    


def main():
    if(len(sys.argv) == 2):
        if((sys.argv[1]) == "--h" or (sys.argv[1]) == "--H"):
            print("--u : Usage")
            print("ScriptName.py Argument1 Argument2")
            
        elif((sys.argv[1]) == "--u" or (sys.argv[1]) == "--U"):
            print("Usage for copying the contents of the file using Command Line Arguments")
            print("ScriptName.py Argument1 Argument2")
        else:
            print("No such command. Use the commands below for instructions:")
            print('--h : Help')
            print('--u : Usage')
    elif(len(sys.argv) == 3):
        ret = CompareFiles(sys.argv[1], sys.argv[2]) 
        print("The frequency of ", sys.argv[2], " in ", sys.argv[1], " is ", ret)     
    else:
        print("Invalid number of Command Line Arguements")
        print("use --h for help")
        print("use --u for usage")


if __name__ == "__main__":
    main()