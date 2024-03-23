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
    __menuBar = Menu(__root)
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

        self.__root.geometry('%dx%d+%d+%d' % (self.__width, self.__height, left, top))
        
        # Configuração do Grid
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)
        
        # Controle da Área de texto
        self.__textArea.grid(sticky=N + E + S + W)
        
        #===================================================================
        
        # 
        
        
        
        
        

    def run(self):
        self.__root.mainloop()


pynote = PyNote()
pynote.run()
