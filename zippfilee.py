# # import zipfile

# # # Open the ZIP file for reading
# # with zipfile.ZipFile('samplee.zip', 'r') as zip_file:
# #     # List the contents of the ZIP file
# #     file_list = zip_file.namelist()
# #     print("Contents of the ZIP file:", file_list)

 

# # Note: Don't forget to replace 'example.zip' and 'path_to_extract_to' with your actual file and path.
# import zipfile

# # Create a new ZIP file
# with zipfile.ZipFile('samplee.zip', 'w') as zip_file:
#     # Add files to the ZIP file
#     file_to_add1 = 'file5.txt'
#     file_to_add2 = 'fh.txt'
    
#     zip_file.write(file_to_add1, arcname='file5.txt')  # You can specify a different name inside the ZIP file
#     zip_file.write(file_to_add2, arcname='fh.txt')
# with zipfile.ZipFile('samplee.zip', 'r') as zip_file:
#     # Add files to the ZIP file
#     file_to_add1 = 'file5.txt'
#     file_to_add2 = 'fh.txt'
    
#     zip_file.read(file_to_add1)  # You can specify a different name inside the ZIP file
#     zip_file.read(file_to_add2)

# Note: Replace 'new_example.zip', 'file_to_add1.txt', and 'file_to_add2.txt' with your actual filenames.
# import zipfile

# # Create a new ZIP file and add files to it
# with zipfile.ZipFile('samplee.zip', 'w') as zipf:
#     zipf.write("file5.txt")

 

    # Add files to the ZIP file without extracting them
      # You can specify a different name inside the ZIP file
  

# Note: Replace 'new_example.zip', 'file_to_add1.txt', and 'file_to_add2.txt' with your actual filenames.
# import zipfile

# # Create a new ZIP file and add files to it
# with zipfile.ZipFile('sample.zip', 'w') as zipf:
#     zipf.write('hello', 'file5.txt')  # Provide the complete path to 'file5.txt'

# print("Success")
# import zipfile

# # Create a new ZIP file and add files to it
# with zipfile.ZipFile('sample.zip', 'w') as zipf:
#     zipf.write('file5.txt', 'file5.txt')  # Provide the complete path to 'file5.txt'

# print("Success")
# import zipfile

# # Open the ZIP file for reading
# with zipfile.ZipFile('sample.zip', 'r') as zipf:
#     # Check if 'file5.txt' exists in the ZIP archive
#     if 'file5.txt' in zipf.namelist():
#         # Read the contents of 'file5.txt' from the ZIP archive
#         with zipf.open('file5.txt') as file_in_zip:
#             contents = file_in_zip.read().decode('utf-8')
#         print(contents)
#     else:
#         print("'file5.txt' does not exist in the ZIP archive.")

import zipfile

with zipfile.ZipFile('testt.zip', 'r') as zipf:
    with zipf.open('fh.txt') as file_in_zip:
        contents = file_in_zip.read().decode('utf-8')
    print(contents)
