import os

# Creating test folder and test files in it 
currDir = os.path.dirname(os.path.abspath(__file__))
folder_name = 'test_folder'
folder_path = os.path.join(currDir, folder_name)

print(folder_path)

files_name = [
    "old_report_2023.txt",
    "old_summary.docx",
    "old_invoice.pdf",
    "some_other_file.txt"
]

# Creting the folder 
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    
    for file_name in files_name:
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'w') as file:
            file.write("")
        print(f'file created : {file_name}')

    print(f'Folder {folder_name} created and files created ')
    
else :
    print("folder existed")

def bulk_rename(folder_path, old_name_part, new_name_part):
    '''
    Renames all files in a folder by replacing occurrences of old_name_part in filenames with new_name_part
    
    Args:
        folder_path (str): Path to the folder containing files to rename
        old_name_part (str): part of the file name to replace
        new_name_part (str) : the replacement string 
    '''
    
    for fileName in os.listdir(folder_path):
        if old_name_part in fileName:
            new_fileName = fileName.replace(old_name_part, new_name_part)
            os.rename(
                os.path.join(folder_path, fileName),
                os.path.join(folder_path, new_fileName)
            )
            
            print(f"rename {fileName} to {new_fileName}")
                
bulk_rename(folder_path, 'old', 'new')