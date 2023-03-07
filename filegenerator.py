import os
from sys import argv

def fileGenerator(FolderName,filename,No,extension):
    FolderName = os.path.abspath(FolderName)
    for i in range(0,10,1):
        fname = filename+(str(No))+"."+(extension.lower())
        No+=1
        fpath = os.path.join(FolderName,fname)
        f = open(fpath,'w')


def main() :
    print("----------Generate 10 files at a time------------")

    print("Application name : "+argv[0])

    if(len(argv)!=5) :
        print("Error : Invalid number of arguments")
        exit()

    if(argv[1] == "-h") or (argv[1] == "-H") :
        print("This Script is used to generate multiple files with given extension")
        exit()

    if(argv[1] == '-u') or (argv[1] == '-U') :
        print("usage : ApplicationName AbsolutPath_of_Directory Filename Start_No Extension")
        exit()

    try :
        fileGenerator(argv[1],argv[2],int(argv[3]),argv[4])
        print("Files Created Succesfully")

    except ValueError :
        print("Error : Invalid datatype of input")


if __name__ == "__main__" :
    main()
