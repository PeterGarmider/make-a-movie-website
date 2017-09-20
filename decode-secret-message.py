import os

def rename_files():

    file_list = os.listdir(r"C:\Users\peter\PycharmProjects\Module 4 - Make a Movie Website\SecretMessage\prank")
    print (file_list)
    saved_path = os.getcwd()
    print("Current path is: "+saved_path)
    os.chdir(r"C:\Users\peter\PycharmProjects\Module 4 - Make a Movie Website\SecretMessage\prank")
    for file_name in file_list:
        print("Old name - "+ file_name)
        mapping_table = str.maketrans(dict.fromkeys('0123456789'))
        print("New name - "+ str(os.rename(file_name, file_name.translate(mapping_table))))
    os.chdir(saved_path)
rename_files()