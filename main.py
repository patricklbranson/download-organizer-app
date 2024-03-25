#  Copyright 2024 Patrick L. Branson
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import os
import shutil
import tkinter as tk
from tkinter import filedialog as fd


class DownloadOrganizerApp:
    """
    Download Folder Organizer Application
    """

    def __init__(self, master: tk.Tk):
        """
        Initializes the DownloadOrganizerApp class

        :param master: the master (root) GUI
        """
        self.__master: tk.Tk = master
        self.__master.title("Download Organizer App")

        self.__label = tk.Label(master=self.__master, text="Click Below to Select Your Download's Directory:")
        self.__label.pack(pady=10)

        self.__select_button = tk.Button(master=self.__master, text="Select Directory", command=self.__select_directory)
        self.__select_button.pack(pady=5)

        self.__status_label = tk.Label(master=self.__master, text="")
        self.__status_label.pack(pady=5)

    # noinspection PyMethodMayBeStatic
    def __organize_downloads(self, download_directory) -> None:
        """
        Organizes the download files

        :param download_directory: the download folder (directory)
        :return: None - "void" function
        """
        # Dictionary to map file extensions to directory names
        file_types = {
            'Documents': ['.pdf', '.doc', '.docx', '.txt'],
            'Images': ['.jpg', '.jpeg', '.png', '.gif'],
            'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
            'Music': ['.mp3', '.wav', '.flac'],
            'Archives': ['.zip', '.rar', '.tar', '.gz'],
            'Executables': ['.exe', '.msi', '.bat'],
            'Others': []  # Default directory for other file types
        }

        # Create directories if they don't exist
        for directory in file_types.keys():
            directory_path = os.path.join(download_directory, directory)
            if not os.path.exists(directory_path):
                os.makedirs(directory_path)

        # Move files to respective directories based on file type
        for filename in os.listdir(download_directory):
            # Exclude the script file itself - but must be renamed if moved to downloads folder
            if filename != 'organize-downloads-app.py':  # Exclude the script file itself
                src_path = os.path.join(download_directory, filename)
                if os.path.isfile(src_path):
                    file_ext = os.path.splitext(filename)[1]
                    moved = False
                    for directory, extensions in file_types.items():
                        if file_ext.lower() in extensions:
                            dst_path = os.path.join(download_directory, directory, filename)
                            shutil.move(src_path, dst_path)
                            moved = True
                            break
                    if not moved:
                        dst_path = os.path.join(download_directory, 'Others', filename)
                        shutil.move(src_path, dst_path)

    def __select_directory(self) -> None:
        """
        Selects the directory to be organized

        :return: None - "void" function
        """
        directory = fd.askdirectory()
        if directory:
            self.__organize_downloads(directory)
            self.__status_label.config(text="Downloads Organized Successfully!")


if __name__ == "__main__":
    root: tk.Tk = tk.Tk()

    app = DownloadOrganizerApp(root)
    root.mainloop()
