from tkinter import *
from PIL import Image,ImageTk

class CallManager:
    def __init__(self, master):
        self.master=master
        self.initialize(master)
        
    def initialize(self,master):  
        #Definições inicias
        master.title('Discador de Chamada V1.0')
        master.iconbitmap('image/phone.ico')
        master.resizable(FALSE,FALSE)
         
        #Variavel para indica que a tela top level não esta aberta
        self.topPesquisar=None
        self.topInserir=None
        self.topLogs=None
        # Variáveis da personalização dos botões
        self.atriLargura=10
        self.atriAltura=3
        self.atriBd=3
        self.atriRelief=GROOVE
        self.atriBg='#e0ebeb'
        self.atriFg='#002e4d'
        self.atriFont=('Verdana 25 bold')
        self.atriFont=('Verdana 25 bold')
        self.atriFont2=('Verdana 10 bold')
        self.atriFont3 = ('Verdana 12 bold')
        self.contador=0
        self.py=50
        #Frame
        self.frameA=Frame(master).place()
        self.frameB=Frame(master).place()
        #Imagem de fundo
        self.imagem=Label(self.frameA)
        self.amostra=ImageTk.PhotoImage(Image.open('image/imagemdebg.png'))
        self.imagem['image']=self.amostra
        self.imagem.place(x=0,y=0)
        ## Dimensões da janela 
        self.largura=800
        self.altura=500
        self.larguraScreen=master.winfo_screenwidth()
        self.alturaScreen=master.winfo_screenheight()
        self.posx=int(self.larguraScreen/2-self.largura/2)
        self.posy=int(self.alturaScreen/2-self.altura/2)
        # menu inicial
        self.meuMenu=Menu(root)

        self.fileMenu=Menu(self.meuMenu,tearoff=0)
        self.fileMenu.add_command(label="Novo")
        self.fileMenu.add_command(label="Importar")
        self.fileMenu.add_command(label="Exportar")

        self.helpMenu=Menu(self.meuMenu,tearoff=0)
        self.configMenu=Menu(self.meuMenu,tearoff=0)

        self.meuMenu.add_cascade(label='Arquivo', menu=self.fileMenu)
        self.meuMenu.add_cascade(label='Manual', menu=self.helpMenu)
        self.meuMenu.add_cascade(label='Configuração de rede',menu=self.configMenu)
        self.meuMenu.add_command(label='Exit',command=master.destroy)
        self.master.config(menu=self.meuMenu)
        # Botões primeiro frame

        self.btBuscar=Button(self.frameA,command=self.widgetPesquisar,text='Pesquisar',bd=self.atriBd,relief=self.atriRelief,fg=self.atriFg,
        width=self.atriLargura,height=self.atriAltura,bg=self.atriBg,font=self.atriFont)
        self.btBuscar.place(x=80,y=50)
        self.btBuscar.bind('<Return>') 

        self.btnInserir=Button(self.frameA,command=self.widgetInserir,text='Inserir',bd=self.atriBd,relief=self.atriRelief,fg=self.atriFg,
        width=self.atriLargura,height=self.atriAltura,bg=self.atriBg,font=self.atriFont)
        self.btnInserir.place(x=480,y=50)
        self.btnInserir.bind('<Return>')
        
        # Botões segundo frame

        self.btnLogs=Button(self.frameB,command=self.widgetLogs,text='Logs',bd=self.atriBd,relief=self.atriRelief,fg=self.atriFg,
        width=self.atriLargura,height=self.atriAltura,bg=self.atriBg,font=self.atriFont)
        self.btnLogs.place(x=80,y=250)
        self.btnLogs.bind('<Return>')

        self.btnExecutar=Button(self.frameB,text='Executar',bd=self.atriBd,relief=self.atriRelief,fg=self.atriFg,
        width=self.atriLargura,height=self.atriAltura,bg=self.atriBg,font=self.atriFont)
        self.btnExecutar.place(x=480,y=250)
        self.btnExecutar.bind('<Return>')
        #Tamanho da tela 
        self.master.geometry('{}x{}+{}+{}'.format(self.largura,self.altura,self.posx,self.posy))
        
    def widgetPesquisar(self):
        #Inicialização da top level
        if self.topPesquisar is None:
            self.topPesquisar=Toplevel()
            self.topPesquisar.title('Discador de Chamada V1.0')
            self.topPesquisar.iconbitmap('image/phone.ico')
            self.topPesquisar.resizable(FALSE,FALSE)
            self.topPesquisar.geometry('{}x{}+{}+{}'.format(self.largura,self.altura,self.posx,self.posy))
           
            #Comando para poder abrir a tela novamente
            self.topPesquisar.protocol("WM_DELETE_WINDOW", self.fechar_widgetPesquisar)

            #Imagem de fundo    
            self.imagem2=Label(self.topPesquisar)
            self.imagem2['image']=self.amostra
            self.imagem2.place(x=0,y=0)
          
        else:
        
            self.topPesquisar.lift()
            

    def widgetInserir(self):
        if self.topInserir is None:
            self.topInserir=Toplevel()
            self.topInserir.title('Discador de Chamada V1.0')
            self.topInserir.iconbitmap('image/phone.ico')
            self.topInserir.resizable(FALSE,FALSE)
            self.topInserir.geometry('{}x{}+{}+{}'.format(self.largura,self.altura,self.posx,self.posy))
            #Imagem de fundo    
            self.imagem3=Label(self.topInserir)
            self.imagem3['image']=self.amostra
            self.imagem3.place(x=0,y=0)
            
           
            #Comando para poder abrir a tela novamente
            self.topInserir.protocol("WM_DELETE_WINDOW", self.fechar_widgeInserir)

            # Parte de adicionar
            self.labelAdicionar = Label(self.topInserir, text='Adicionar', font=self.atriFont2, fg=self.atriFg)
            self.labelAdicionar.place(x=130, y=30)
            self.ent = Entry(self.topInserir, width=20)
            self.ent.place(x=100, y=80)
            self.btnAdicionar = Button(self.topInserir, command=self.botaoAdicionar,text='+', fg=self.atriFg, bd=self.atriBd, relief=self.atriRelief, font=self.atriFont2, bg=self.atriBg)
            self.btnAdicionar.place(x=225, y=76)
            # Parte do progesso
            self.labelProgresso = Label(self.topInserir, text='Progresso', font=self.atriFont2, fg=self.atriFg)
            self.labelProgresso.place(x=450, y=30)
            self.listaProgresso = Listbox(self.topInserir, width=70, height=18)
            self.listaProgresso.place(x=275, y=80)

            # Botoes rodape
            self.btnVoltar = Button(self.topInserir, text='Voltar', command=self.fechar_widgeInserir, fg=self.atriFg, bd=self.atriBd, relief=self.atriRelief,font=self.atriFont3, bg=self.atriBg, width=6)
            self.btnInserir = Button(self.topInserir, text='Inserir', fg=self.atriFg, bd=self.atriBd, relief=self.atriRelief, font=self.atriFont3, bg=self.atriBg, width=6)
            self.btnLimpar = Button(self.topInserir, text='Limpar', fg=self.atriFg, bd=self.atriBd, relief=self.atriRelief, font=self.atriFont3, bg=self.atriBg, width=6)
            self.btnVoltar.place(x=100, y=420)

            self.btnInserir.place(x=360, y=420)
        else:
            self.topInserir.lift()
        
       

    def widgetLogs(self):  
        if self.topLogs is None:
            self.topLogs=Toplevel()
            self.topLogs.title('Discador de Chamada V1.0')
            self.topLogs.iconbitmap('image/phone.ico')
            self.topLogs.resizable(FALSE,FALSE)
            self.topLogs.geometry('{}x{}+{}+{}'.format(self.largura,self.altura,self.posx,self.posy))
            #Imagem de fundo    
            self.imagem4=Label(self.topLogs)
            self.imagem4['image']=self.amostra
            self.imagem4.place(x=0,y=0)

            #ListaBox   
            self.labelLog=Label(self.topLogs,text='Registro',font=self.atriFont,fg=self.atriFg)
            self.labelLog.pack()
            self.listaLog=Listbox(self.topLogs,width=100,height=22)
            self.listaLog.pack()
            #Botões 
            self.btnlargura=6
            self.btnBuscar=Button(self.topLogs,text='Buscar',fg=self.atriFg,bd=self.atriBd,relief=self.atriRelief,
            font=self.atriFont,bg=self.atriBg,width=self.btnlargura)
            self.btnFiltro=Button(self.topLogs,text='Filtro',fg=self.atriFg,bd=self.atriBd,relief=self.atriRelief,
            font=self.atriFont,bg=self.atriBg,width=self.btnlargura)
            self.btnVoltar=Button(self.topLogs,text='Voltar',command=self.fechar_widgetLogs,fg=self.atriFg,bd=self.atriBd,relief=self.atriRelief,
            font=self.atriFont,bg=self.atriBg,width=self.btnlargura)
            self.btnBuscar.place(x=100,y=420)
            self.btnFiltro.place(x=330,y=420)
            self.btnVoltar.place(x=550,y=420)
            #Comando para poder abrir a tela novamente
            self.topLogs.protocol("WM_DELETE_WINDOW", self.fechar_widgetLogs)
        else:
            self.topLogs.lift()

    def botaoAdicionar(self):
        if (self.contador<4):
            self.ent = Entry(self.topInserir, width=20)
            self.ent.place(x=100, y=(80+self.py))
            self.btnAdicionar.place(x=225, y=(76+self.py))
            self.py+=50
            self.contador+=1

    def fechar_widgetPesquisar(self):
        # reseta de novo em None para recriar quando abrir
        self.topPesquisar.destroy()
        self.topPesquisar = None
    def fechar_widgeInserir(self):  
        
        # Reseta o Botão adicionar  
        self.contador=0
        self.py=50
        self.ent = Entry(self.topInserir, width=20)
        self.ent.place(x=100, y=80)
        self.btnAdicionar.place(x=225, y=76)

        # reseta de novo em None para recriar quando abrir
        self.topInserir.destroy()
        self.topInserir = None    
    def fechar_widgetLogs(self):   
        # reseta de novo em None para recriar quando abrir 
        self.topLogs.destroy()
        self.topLogs = None    
           
        

if __name__ == "__main__":  
    root=Tk()
    app=CallManager(root)
    root.mainloop()
             