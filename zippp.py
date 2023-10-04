# import zipfile

# with zipfile.ZipFile('testt.zip', 'w') as zipf:
#     zipf.write('file6.txt', 'file6.txt')

# import zipfile

# with zipfile.ZipFile('testt.zip', 'r') as zipf:
#     with zipf.open('file6.txt') as zip:
#         contents = zip.read().decode('utf-8')
# print(contents)

import zipfile

# Specify the name of the file you want to extract
file_to_extract = 'file6.txt'
extraction_path = "C:/Users/legal/OneDrive/Desktop/python programs/samplee.zip"
with zipfile.ZipFile('testt.zip', 'r') as zipf:
    if file_to_extract in zipf.namelist():
        # Extract the specified file to the current working directory
        zipf.extract(file_to_extract)
        print(f"'{file_to_extract}' has been extracted.")
    else:
        print(f"'{file_to_extract}' does not exist in the ZIP archive.")



