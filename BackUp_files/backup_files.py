import os 
import shutil

curr_dir = os.path.dirname(os.path.abspath(__file__))
folder_name = 'test_folder'
folder_path = os.path.join(curr_dir, folder_name)

files_name = [
    "old_report_2023.txt",
    "old_summary.docx",
    "old_invoice.pdf",
    "some_other_file.txt"
]

if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    
    for fileName in files_name:
        file_path = os.path.join(folder_path, fileName)
        with open(file_path, 'w') as file:
            file.write("")
        print(f"file {fileName} created ")
        
    print(f"\nfolder {folder_name} and files created \n")
else:
    print("\nThe file already exist\n")
    
def backupFile(folder_path, backUppath):
    if not os.path.exists(backUppath):
        os.makedirs(backUpPath)
        
        
    for file in os.listdir(folder_path):
        currFile = os.path.join(folder_path, file)
        if os.path.isfile(currFile):
            destFile = os.path.join(backUpPath, file)
            shutil.copy(currFile, destFile)
            print(f'Backed up {file} in folder {backUppath}') 

        
    
    
backUpfolder = 'BackUpfolder'
backUpPath = os.path.join(curr_dir, backUpfolder)

backupFile(folder_path, backUpPath)  
