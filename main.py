#! /usr/bin/env python
import Tkinter as tk
from Tkinter import Tk
from git import Repo
import os

class Application(tk.Frame):
    """Clase principal para correr la interfaz de la sincronizacion de archivos"""

    repo_dir = ''
    repo = Repo()
    files_with_changes = []

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.set_repository_information()
        self.createWidgets()

        dir_path = os.path.abspath(os.path.dirname(__file__))
        self.repo_dir = dir_path
        self.repo = Repo(self.repo_dir)

        self.set_files_with_changes()

    def set_repository_information(self):
        self.repo_info = tk.LabelFrame(self, text="Informacion del repositorio")
        self.repo_info.grid()

        branches = [h.name for h in self.repo.heads]

        text = "\nRama actual: " + str(self.repo.active_branch) + \
               "\nRamas: " + str(branches)

        self.left = tk.Label(self.repo_info, text=text)
        self.left.grid()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text="Cerrar", command=self.quit)
        self.quitButton.grid()

    def set_files_with_changes(self):
        files = os.popen('git status -s | cut -c4-', 'r')
        self.files_with_changes = files.read().strip().split('\n')
        print self.files_with_changes
        self.draw_checkbox_files()

    def draw_checkbox_files(self):
        for file in self.files_with_changes:
            print file
            self.check = tk.Checkbutton(self, text=str(file))
            self.check.grid()

root = Tk()
app = Application(master=root)
app.master.title('Sincronizar archivos')
app.mainloop()
app.destroy()