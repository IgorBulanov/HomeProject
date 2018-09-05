'''
Created on 1 мая 2018 г.

@author: Igor
'''

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

class MainMenu(object):
    '''
    classdocs
    '''

    def __init__(self, root):
        self.root = root
        #icons_path="/home/igor/eclipse-workspace/radar/src/radar/icons/"
        #new_file_icon = tk.PhotoImage(file=icons_path+'new_file.gif')
        #open_file_icon = tk.PhotoImage(file=icons_path+'open_file.gif')
        #save_file_icon = tk.PhotoImage(file=icons_path+'save.gif')
        #        cut_icon = tk.PhotoImage(file=icons_path+'cut.gif')
        #        copy_icon = tk.PhotoImage(file=icons_path+'copy.gif')
        #        paste_icon = tk.PhotoImage(file=icons_path+'paste.gif')
        #        undo_icon = tk.PhotoImage(file=icons_path+'undo.gif')
        #        redo_icon = tk.PhotoImage(file=icons_path+'redo.gif')
        #image=new_file_icon,
        #image=open_file_icon,
        #image=save_file_icon,
        #
        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="New",
                                  accelerator='Ctrl+N',
                                  compound='left', underline=0,
                                  command=lambda: self.projectNew())
        self.filemenu.add_command(label="Open",
                                  accelerator='Ctrl+O',
                                  compound='left', underline=0,
                                  command=lambda: self.projectOpen())
        self.filemenu.add_command(label="Save",
                                  accelerator='Ctrl+S',
                                  compound='left', underline=0,
                                  command=lambda: self.projectSave())
        self.filemenu.add_command(label="Save as...",
                                  accelerator='Shift+Ctrl+S',
                                  command=lambda: self.projectSaveAs())
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit",
                                  accelerator='Alt+X',
                                  command=self.root.quit)
        self.menubar.add_cascade(label="Files", menu=self.filemenu)

        self.patterns = tk.Menu(self.menubar, tearoff=0)
        self.patterns.add_command(label="Build",
                                  accelerator='Ctrl+B', underline=0,
                                  command=lambda: self.patternsCreate)
        self.patterns.add_command(label="Find",
                                  accelerator='Ctrl+F', underline=0,
                                  command=lambda: self.patternsFind)
        self.patterns.add_command(label="Edit",
                                  accelerator='Ctrl+E', underline=0,
                                  command=lambda: self.patternsEdit)
        self.menubar.add_cascade(label="Patterns", menu=self.patterns)

        view_menu = tk.Menu(self.menubar, tearoff=0)
        themes_menu = tk.Menu(self.menubar, tearoff=0)
        view_menu.add_cascade(label='Themes', menu=themes_menu)

        color_schemes = {
            'Default': '#000000.#FFFFFF',
            'Greygarious': '#83406A.#D1D4D1',
            'Aquamarine': '#5B8340.#D1E7E0',
            'Bold Beige': '#4B4620.#FFF0E1',
            'Cobalt Blue': '#ffffBB.#3333aa',
            'Olive Green': '#D1E7E0.#5B8340',
            'Night Mode': '#FFFFFF.#000000',
        }
        theme_choice = tk.StringVar()
        theme_choice.set('Default')
        for k in sorted(color_schemes):
            themes_menu.add_radiobutton(label=k, variable=theme_choice)
        self.menubar.add_cascade(label='View', menu=view_menu)

        self.about = tk.Menu(self.menubar, tearoff=0)
        self.about.add_command(label="About project", command=lambda: self.aboutProject)
        self.about.add_command(label="Developers", command=lambda: self.aboutDeveloper)
        self.menubar.add_cascade(label="About", menu=self.about)

    def projectNew(self):
        pass

    def projectOpen(self):
        self.projectNameFile = tk.filedialog.askopenfilename(initialdir = ".",title = "Select file",filetypes = (("project files","*.prj"),("all files","*.*")))
        print(self.projectNameFile)

    def projectSave(self):
        self.projectNameFile = tk.filedialog.asksaveasfilename(initialdir = ".",title = "Select file",filetypes = (("project files","*.prj"),("all files","*.*")))

    def projectSaveAs(self):
        pass

    def projectClose(self):
        pass

    def patternsCreate(self):
        pass

    def patternsFind(self):
        pass

    def patternsEdit(self):
        pass

    def aboutProject(self):
        pass

    def aboutDeveloper(self):
        tk.messagebox.showinfo("Developers",
                               "created by:\nHB hb2hb@yandex.ru\nBIG bulanov.ig@phystech.edu")



