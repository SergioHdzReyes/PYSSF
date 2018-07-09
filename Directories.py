#! /usr/bin/env python
import re, os

class Directories:
    root_dir = ''
    files_with_changes = []
    directories = []

    def __init__(self, files_with_changes, root_dir=''):
        self.root_dir = root_dir

        self.set_only_files(files_with_changes)

    # En caso que haya directorios en files_with_changes,
    # extrae los archivos y remueve esos elementos (directorios)
    def set_only_files(self, files_with_changes = []):
        for key in files_with_changes:
            self.process_directory(re.sub(r"" + os.sep + '$', '', key))

    # Retorna una ruta completa del archivo dado
    def full_path(self, path=''):
        return self.root_dir + os.sep + path

    # Procesa directorio y subdirectorios en busca de archivos
    # Se incluyen los archivos a la lista files_with_changes
    def process_directory(self, file=''):
        #print '--' + file
        is_dir = 0

        for root, dirs, files in os.walk(file):
            is_dir = 1
            for dir in dirs:
                self.process_directory(file + os.sep + dir)

            for archivo in files:
                if os.path.exists(file + os.sep + archivo):
                    self.files_with_changes.append(file + os.sep + archivo)

        root, ext = os.path.splitext(file)
        if is_dir == 0 and ext and os.path.exists(file):
            self.files_with_changes.append(file)

        return