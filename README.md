# File Organizer Script

This Python script organizes files in a given directory into different folders based on their file type. The script categorizes files into several types such as images, documents, videos, audio, archives, programs, and scripts.

## Features
- Automatically creates folders for each file type category (e.g., Images, Documents, Videos, etc.).
- Moves files to the appropriate folder based on their extensions.
- If a file's extension doesn't match any of the predefined categories, it is moved to a folder named "Other."
- Designed to work with various file formats like `.jpg`, `.pdf`, `.mp3`, `.exe`, `.py`, and many more.

## File Types Supported
The script categorizes files into the following types:

- **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`
- **Documents**: `.pdf`, `.docx`, `.txt`, `.xls`, `.xlsx`, `.ppt`, `.pptx`
- **Videos**: `.mp4`, `.mkv`, `.avi`, `.mov`, `.flv`
- **Audio**: `.mp3`, `.wav`, `.aac`
- **Archives**: `.zip`, `.rar`, `.7z`
- **Programs**: `.exe`, `.apk`, `.dmg`
- **Scripts**: `.py`, `.js`, `.html`, `.css`

Any file that does not match the above extensions will be moved to an "**Other**" folder.

## Requirements
- Python 3.x
- `os` and `shutil` libraries (both are built-in libraries, so no additional installation is required).

## How to Use
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/Yahia-Hosny/file-organizer.git
2. Open the script file_organizer.py in your preferred editor 
3. Specify the path of the directory you want to organize in the script
``` python
directory = "Path_to_the_directory_to_organize"
```
4. Run the script 
``` shell 
python file_organizer.py
```
## Example 
``` python 
directory = "C:/Users/Username/Downloads"
organize_files(directory)
``` 
This will organize all the files in the `C:/Users/Username/Downloads` directory into respective folders based on their file types.

## Error Handling
* If the specified directory does not exist, the script will print an error message and stop execution.
* The script automatically creates the necessary folders (if they don't exist) for each file type.
* It handles cases where a file doesn't match any predefined type and moves it to the "Other" folder.


## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/Yahia-Hosny/file-organizer?tab=MIT-1-ov-file#readme) file for details. 




