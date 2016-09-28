###########this program basically changes the name of file. In this program, files in prank folder are renamed. These files had a name with numbers , so after running this program it will rename those files and change the name without numbers
###example. file name is "123abcd7.jpg". after running this program, name will be "abcd.jpg"


import os

def rename_files():
    #get filename from the folder
    #this line will save all the file-name to the "file_name" variable as a list
    file_list = os.listdir(r"../images/")  #add path of your folder
    #to get and print current directory or file path in python-- cwd stands for current working directory
    saved_path = os.getcwd()
    print ("cwd "+saved_path)

    #to change current working directory
    os.chdir(r"../images/") #add path of your folder

    #rename each files in the folder
    for file_name in file_list:
        print("old name: "+file_name)
        print("new name: "+file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789")) #os.rename will rename the file

    os.chdir(saved_path)

rename_files()
