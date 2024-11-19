#########################################################################################
# file: print_folder_contents.py
# type: Python
# date: 13_OCTOBER_2024
# author: karbytes
# license: PUBLIC_DOMAIN 
#########################################################################################

import os

# Define the only function in this program.
def list_files_in_folder(folder_path, output_file):
    total_size = 0
    file_count = 0
    i = 0

    # Define the output file handler.
    with open(output_file, 'w') as f:

        # Print a horizontal divider line to the command line terminal and to the output file.
        print("\n\n--------------------------------")
        f.write("--------------------------------")

        # Print "This Python program prints the names and file sizes (in megabytes) of each file inside of a particular folder." to the command line terminal and to the output file.
        print("\n\nThis Python program prints the names and file sizes (in megabytes) of each file inside of a particular folder.")
        f.write("\n\nThis Python program prints the names and file sizes (in megabytes) of each file inside of a particular folder.")

        # Print a horizontal divider line to the command line terminal and to the output file.
        print("\n\n--------------------------------")
        f.write("\n\n--------------------------------")

        # Walk through the folder and its subfolders
        for root, dirs, files in os.walk(folder_path):
            f.write(f"\n\nDirectory: {root}")
            print(f"\n\nDirectory: {root}")
            for file in files:
                file_path = os.path.join(root, file)
                if os.path.isfile(file_path):  # Only process files, not subdirectories.
                    file_size = os.path.getsize(file_path) / (1024 * 1024)  # Convert from bytes to megabytes.
                    total_size += file_size
                    file_count += 1
                    f.write(f"\n\nfile_{i}: {file} // {file_size:.2f} megabytes")
                    print(f"\n\nfile_{i}: {file} // {file_size:.2f} megabytes")
                    i += 1
        
        # Print totals to the output file.
        f.write("\n\n--------------------------------")
        f.write(f"\n\nTotal number of files: {file_count}")
        f.write(f"\n\nTotal folder size: {total_size:.2f} megabytes")
        f.write("\n\n--------------------------------")

        # Print totals to the command line terminal.
        print("\n\n--------------------------------")
        print(f"\n\nTotal number of files: {file_count}")
        print(f"\n\nTotal folder size: {total_size:.2f} megabytes")
        print("\n\n--------------------------------")

    # Print a final message to the command line terminal.
    print(f"\n\nResults have been written to '{output_file}'.")

    # Print a horizontal divider line to the command line terminal.
    print("\n\n--------------------------------\n\n")

# Set the folder path to the folder you would like to analyze.
folder_path = 'test_folder'  # Replace the value of folder_path with your actual folder path.
output_file = 'test_folder_contents.txt'  # Replace the value of output_file with your preferred output text file path (which will overwrite that file if it exists or else generate it).

# Execute the function which is defined in this program file.
list_files_in_folder(folder_path, output_file)
