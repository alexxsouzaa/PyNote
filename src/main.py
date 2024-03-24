import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter import ttk


class PyNote:
    # Inicializando a janela
    __root = Tk()

    # Configurações iniciais do bloco de notas
    __width = 600
    __height = 450
    __textArea = Text(__root, padx=10, pady=10,
                      wrap='word', font=('Consolas 12'))
    __menuBar = Menu(__root, relief='flat')
    __fileMenu = Menu(__menuBar, tearoff=0)
    __editMenu = Menu(__menuBar, tearoff=0)
    __viewMenu = Menu(__menuBar, tearoff=0)
    __helpMenu = Menu(__menuBar, tearoff=0)

    __scrollBar = Scrollbar(__textArea)
    __file = None

    def __init__(self, **kwargs):
        # Set icon
        try:
            self.__root.wm_iconbitmap('icons/icon.ico')
        except:
            pass

        # Configurações da janela (300x300)
        try:
            self.__width = kwargs['width']
        except KeyError:
            pass
        try:
            self.__height = kwargs['height']
        except KeyError:
            pass

        self.__root.title('Sem título - PyNote')

        screenWidth = self.__root.winfo_screenwidth()
        screeHeight = self.__root.winfo_screenheight()

        left = (screenWidth / 2) - (self.__width / 2)
        top = (screeHeight / 2) - (self.__height / 2)

        self.__root.geometry('%dx%d+%d+%d' %
                             (self.__width, self.__height, left, top))
        
        self.__root.minsize(width=300, height=300)

        # Configuração do Grid
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)

        # Controle da Área de texto
        self.__textArea.grid(sticky=N + E + S + W)

        # Exibi o MenuBar e o ScrollBar
        self.__root.config(menu=self.__menuBar)
        self.__scrollBar.config(command=self.__textArea.yview)
        self.__textArea.config(yscrollcommand=self.__scrollBar.set)
        self.__scrollBar.pack(side='right', fill='y')

    # =================== Menus ===================
    # Menu de Arquivo
        self.__fileMenu.add_command(label='Novo', command=self.__newFile)

        self.__fileMenu.add_command(label='Abrir', command=self.__openFile)

        self.__fileMenu.add_command(label='Salvar', command=self.__saveFile)

        self.__fileMenu.add_separator()

        self.__fileMenu.add_command(
            label='Sair', command=self.__quitApplication)

        self.__menuBar.add_cascade(label='Arquivo', menu=self.__fileMenu)

    # Menu Editar
        self.__editMenu.add_command(label='Cortar', command=self.__cut)

        self.__editMenu.add_command(label='Copiar', command=self.__copy)

        self.__editMenu.add_command(label='Colar', command=self.__paste)

        self.__menuBar.add_cascade(label='Editar', menu=self.__editMenu)

    # Menu Editar
        self.__viewMenu.add_command(label='Temas', command=self.__theme)

        self.__menuBar.add_cascade(label='View', menu=self.__viewMenu)

    # Menu Ajuda
        self.__helpMenu.add_command(
            label='Sobre o aplicativo', command=self.__showAbout)

        self.__menuBar.add_cascade(label='Ajuda', menu=self.__helpMenu)

    # =================== Funções dos Menus ===================
    # Funções do menu de Arquivo
    def __newFile(self):
        self.__root.title('Sem título - PyNote')
        self.__file = None
        self.__textArea.delete(1.0, END)

    def __openFile(self):
        self.__file = askopenfilename(defaultextension='.txt',
                                      filetypes=[('ALL Files', '*.*'),
                                                 ('Text Documents', '.txt')])
        
        if self.__file == '':
            self.__file = None
        else:
            self.__root.title(os.path.basename(self.__file) + ' - PyNote')
            self.__textArea.delete(1.0, END)
            
            file = open(self.__file, 'r', encoding='utf-8')
            self.__textArea.insert(1.0, file.read())
            file.close()

    def __saveFile(self):
        if self.__file == None:
            self.__file = asksaveasfilename(initialfile='Sem titulo', defaultextension='.txt', filetypes=[('ALL Files', '*.*'), ('Text Documents', '*.txt')])
            
            if self.__file == '':
                self.__file = None
            else:
                file = open(self.__file, 'w', encoding='utf-8')
                file.write(self.__textArea.get(1.0, END))
                file.close()
                
                self.__root.title(os.path.basename(self.__file) + ' - PyNote')
        
        else:
            file = open(self.__file, 'w')
            file.write(self.__textArea.get(1.0, END))
            file.close()
            
    def __quitApplication(self):
        self.__root.quit()

    # Funções do menu de Editar
    def __cut(self):
        self.__textArea.event_generate('<<Cut>>')

    def __copy(self):
        self.__textArea.event_generate('<<Copy>>')

    def __paste(self):
        self.__textArea.event_generate('<<Paste>>')

    # Funções do menu de View
    def __theme(self):
        ...

    # Funções do menu de Ajuda
    def __showAbout(self):
        showinfo('Sobre o Software - PyNote',
                 'Versão: 1.0.0\nLicença Grátis\nDesenvolvedor: Bruno Álex\nGitHub: alexxsouzaa')

    def run(self):
        self.__root.mainloop()


pynote = PyNote()
pynote.run()
