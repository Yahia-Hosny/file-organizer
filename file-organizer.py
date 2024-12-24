import os
import shutil

# Function to organize files
def organize_files(directory):
    # File type categories
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
        'Documents': ['.pdf', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
        'Videos': ['.mp4', '.mkv', '.avi', '.mov', '.flv'],
        'Audio': ['.mp3', '.wav', '.aac'],
        'Archives': ['.zip', '.rar', '.7z'],
        'Programs': ['.exe', '.apk', '.dmg'],
        'Scripts': ['.py', '.js', '.html', '.css'],
    }
    
    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return 
    
    # Create folders for each category if they don't exist
    for folder in file_types.keys():
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    
    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Check if it's a file
        if os.path.isfile(file_path):
            # Determine the file type based on extension
            moved = False
            for category, extensions in file_types.items():
                if any(filename.lower().endswith(ext) for ext in extensions):
                    # Move the file to the appropriate folder
                    dest_folder = os.path.join(directory, category)
                    shutil.move(file_path, os.path.join(dest_folder, filename))
                    moved = True
                    break
            
            # If the file type is not found, move it to the "Other" folder
            if not moved:
                other_folder = os.path.join(directory, 'Other')
                if not os.path.exists(other_folder):
                    os.makedirs(other_folder)
                shutil.move(file_path, os.path.join(other_folder, filename))

# Specify the directory you want to organize
directory = "Path_to_the_directory_to_organize"
organize_files(directory)
