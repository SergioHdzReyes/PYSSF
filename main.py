#! /usr/bin/env python
import Tkinter as tk
from git import Repo
import os

class Application(tk.Frame):
    """Esta es una clase de ejemplo"""

    repo_dir = ''
    repo = Repo()

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.set_repository_information()
        self.createWidgets()

        dir_path = os.path.abspath(os.path.dirname(__file__))
        self.repo_dir = dir_path
        self.repo = Repo(self.repo_dir)
        print self.repo.active_branch

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

app = Application()
app.master.title('Sincronizar archivos')
app.mainloop()