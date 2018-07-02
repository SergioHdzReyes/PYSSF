#! /usr/bin/env python
import re, os

class Directories:
    root_dir = ''
    files_with_changes = []
    files_with_changes2 = []
    directories = []

    def __init__(self, files_with_changes, root_dir = ''):
        self.files_with_changes = files_with_changes
        self.root_dir = root_dir

        self.set_only_files()

    # En caso que haya directorios en files_with_changes,
    # extrae los archivos y remueve esos elementos (directorios)
    def set_only_files(self):
        for key in self.files_with_changes:
            self.process_directory(key)
        print self.files_with_changes2

    # Retorna una ruta completa del archivo dado
    def full_path(self, path=''):
        return self.root_dir + os.sep + path

    # Procesa directorio y subdirectorios en busca de archivos
    # Se incluyen los archivos a la lista files_with_changes
    def process_directory(self, file=''):
        print '--' + file
        if os.path.isfile(file):
            print 'is_file'
        if os.path.isdir(file):
            print 'is_dir'
            for item in os.listdir(self.full_path(file)):
                if os.path.isfile(self.full_path(item)):
                    print 'is_file2: ' + item
                if os.path.isdir(file):
                    print 'is_dir'
        #for item in os.listdir(self.full_path(file)):
        #    print '__2: ' + item
        return



        if not file:
            return
        #print '--' + file
        print '--: ' + file

        # Nuevas validaciones
        if os.path.isfile(self.full_path(file)):
            self.files_with_changes2.append(file)
            print 'is_file'
            return

        if os.path.isdir(self.full_path(file)):
            print 'is_dir: ' + self.full_path(file)
            for item in os.listdir(self.full_path(file)):
                if os.path.isfile(self.full_path(item)):
                    self.files_with_changes2.append(item)
                    print 'is_file2: ' + item
                else:
                    print 'is_dir2: ' + item
                    self.process_directory(item)
            return

        #self.files_with_changes2.append(file)
        #print 'is_file'
        return