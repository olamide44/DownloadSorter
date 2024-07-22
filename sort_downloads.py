import os
import shutil
from glob import glob

# Define source and destination directories
downloads_folder = 'C:/Users/olami/Downloads'  # Update this path
destination_folders = {
    'images': 'C:/Users/olami/Images',  # Update these paths
    'documents': 'C:/Users/olami/Documents',
    'videos': 'C:/Users/olami/Videos',
    'audio': 'C:/Users/olami/Music',
    'archives': 'C:/Users/olami/Desktop/Archives',
    'others': 'C:/Users/olami/Desktop/Others'
}

# Define file extensions for each category
file_types = {
    'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg'],
    'documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
    'videos': ['.mp4', '.mkv', '.flv', '.avi', '.mov', '.wmv'],
    'audio': ['.mp3', '.wav', '.aac', '.flac', '.ogg'],
    'archives': ['.zip', '.rar', '.tar', '.gz', '.7z']
}

# Create destination folders if they don't exist
for folder in destination_folders.values():
    os.makedirs(folder, exist_ok=True)

# Function to move files
def move_file(file, destination_folder):
    try:
        shutil.move(file, destination_folder)
        print(f'Moved: {file} to {destination_folder}')
    except Exception as e:
        print(f'Error moving file {file}: {e}')

# Scan the downloads folder and move files
for file in glob(os.path.join(downloads_folder, '*')):
    if os.path.isfile(file):
        file_extension = os.path.splitext(file)[1].lower()
        moved = False
        
        for category, extensions in file_types.items():
            if file_extension in extensions:
                move_file(file, destination_folders[category])
                moved = True
                break
        
        if not moved:
            move_file(file, destination_folders['others'])
