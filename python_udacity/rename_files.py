import os

def rename_files():
        files_folder = os.listdir("/home/rr/Desktop/dev/python-studies/giraffe-course/first_python")
        saved_path = os.getcwd()
        os.chdir("/home/rr/Desktop/dev/python-studies/giraffe-course/first_python")
        
        for files in files_folder:
                print("old name ", files)
                os.rename(files, files.strip("E"))  
                print("new name ", files.strip("E"))
        os.chdir(saved_path)    
        
rename_files()