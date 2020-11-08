from watchdog.observers import Observer #pip install watchdog
from watchdog.events import FileSystemEventHandler
import time
import os
import json
import shutil
import sys
# Edit the following lines to change the folder to be sorted and the categories to sort the files into

# Make sure that the directories and the file extensions correspond to each other

# Add this script to your startup folder to automatically sort the files in the specified folder

# I AM NOT RESPONSIBLE IF THIS SCRIPT SOMEHOW MESSES YOU UP THAT IS NOT MY FAULT AND IF YOU BLAME ME 
# I WILL SIT AND LAUGH AT YOU
                                                                                   
#                                                                                            -Aten2005

sortedFolders = ['Videos', 'Images', 'Zip', 'Documents', 'Installers', 'Scripts', 'APKs', 'Moosic']

extensions= [['.webm', '.mp4', '.mkv', 'flv', '.ogg', '.ogv', 'avi', '.mov', '.wmv', '.m4p', '.m4v'],
            ['.tiff', '.jpeg', '.bmp', '.jpg', '.raw', '.png', '.jfif'],
            ['zip', '.rar'],
            ['.doc', '.docx', '.pdf', '.txt', '.xls', '.xlsx'],
            ['.msi', '.exe'],
            ['.py', '.jar'],
            ['.apk'],
            ['.m4a', 'mp3']]

folder_to_sort = f"{os.environ['USERPROFILE']}/Downloads/"

sortedFolders.append('Others')

class myHandler(FileSystemEventHandler):
    i = 1
    fileType = -1

    print("Successfully initialized")
    def on_modified(self, event):

        time.sleep(2)

        for filename in os.listdir(folder_to_sort):

            filename_parts = filename.split('.')
            file_extension = filename_parts[-1]
            file_extension = '.' + file_extension
            file_extension = file_extension.lower()
            fileType = -1
            src = folder_to_sort + "/" + filename

            for i in range(0, len(extensions)):
                for j in range(0, len(extensions[i])):
                    if extensions[i][j] in file_extension:
                        fileType = i
                        break
                if fileType != -1:
                        break
            
            dest = folder_to_sort + sortedFolders[fileType] + "/" + filename
            if not os.path.exists(dest) and not os.path.isdir(src) and file_extension not in ".tmp":
                shutil.move(src, dest)
                print(f"Moved {filename} to {dest} with extension {file_extension}")

for index in range(0, len(sortedFolders)):
    if not os.path.exists(folder_to_sort + sortedFolders[index]):
        os.makedirs(folder_to_sort + sortedFolders[index])

eventHandler = myHandler()
observer = Observer()
observer.schedule(eventHandler, folder_to_sort, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
                        


