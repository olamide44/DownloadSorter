# DownloadSorter
**Overview**

This Python script automatically organizes files in your Downloads folder by categorizing and moving them into designated directories based on their file types. The script helps maintain an organized file system by sorting images, documents, videos, audio files, archives, and other miscellaneous files into specific folders.

**Features**

Automatic File Organization: The script scans the Downloads folder and categorizes files into predefined directories based on their extensions.

Customizable Directories: You can easily update the source (Downloads) and destination directories to match your file organization preferences.

Supports Multiple File Types: The script handles common file types for images, documents, videos, audio files, and archives.

Error Handling: Includes basic error handling to notify the user if a file cannot be moved.



**Tech Stack**


Python 3.x

os: For interacting with the operating system and managing directories.

shutil: For moving files.

glob: For pattern matching to find files.


**Prerequisites**

Python 3.x installed on your system.
Basic understanding of Python scripting.


**Installation**

Clone the Repository:

git clone https://github.com/olamide44/DownloadSorter.git

cd file-organizer-script


**Update the Script**:


Modify the downloads_folder path to point to your Downloads directory.
Update the destination_folders paths to your preferred directories.


**Run the Script:**

python file_organizer.py


**Customization**

Adding/Removing File Types: Edit the file_types dictionary in the script to add or remove file extensions for each category.
Changing Destination Folders: Modify the paths in the destination_folders dictionary to direct files to different directories.


**Usage**

The script scans the specified Downloads folder and moves files to the appropriate directory based on their extensions. Files that do not match any of the specified types are moved to the "Others" folder.


**Example**

For example, all .jpg and .png files will be moved to the Images folder, while .pdf and .docx files will be moved to the Documents folder.

