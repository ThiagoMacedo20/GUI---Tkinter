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
        self.top=Toplevel()
        self.top.title('Discador de Chamada V1.0')
        self.top.iconbitmap('image/phone.ico')
        self.top.resizable(FALSE,FALSE)
        self.top.geometry('{}x{}+{}+{}'.format(self.largura,self.altura,self.posx,self.posy))
        #Imagem de fundo    
        self.imagem2=Label(self.top)
        self.imagem2['image']=self.amostra
        self.imagem2.place(x=0,y=0)

    def widgetInserir(self):
        self.top=Toplevel()
        self.top.title('Discador de Chamada V1.0')
        self.top.iconbitmap('image/phone.ico')
        self.top.resizable(FALSE,FALSE)
        self.top.geometry('{}x{}+{}+{}'.format(self.largura,self.altura,self.posx,self.posy))
        #Imagem de fundo    
        self.imagem3=Label(self.top)
        self.imagem3['image']=self.amostra
        self.imagem3.place(x=0,y=0)

        # Parte de adicionar
        self.labelAdicionar = Label(self.top, text='Adicionar', font=self.atriFont2, fg=self.atriFg)
        self.labelAdicionar.place(x=130, y=30)
        self.ent = Entry(self.top, width=20)
        self.ent.place(x=100, y=80)
        self.btnAdicionar = Button(self.top, command=self.botaoAdicionar,text='+', fg=self.atriFg, bd=self.atriBd, relief=self.atriRelief, font=self.atriFont2, bg=self.atriBg)
        self.btnAdicionar.place(x=225, y=76)
        # Parte do progesso
        self.labelProgresso = Label(self.top, text='Progresso', font=self.atriFont2, fg=self.atriFg)
        self.labelProgresso.place(x=450, y=30)
        self.listaProgresso = Listbox(self.top, width=70, height=18)
        self.listaProgresso.place(x=275, y=80)

        # Botoes rodape
        self.btnVoltar = Button(self.top, text='Voltar', command=self.top.destroy, fg=self.atriFg, bd=self.atriBd, relief=self.atriRelief,font=self.atriFont3, bg=self.atriBg, width=6)
        self.btnInserir = Button(self.top, text='Inserir', fg=self.atriFg, command=self.insereDado, bd=self.atriBd, relief=self.atriRelief, font=self.atriFont3, bg=self.atriBg, width=6)
        self.btnLimpar = Button(self.top, text='Limpar', fg=self.atriFg, bd=self.atriBd, relief=self.atriRelief, font=self.atriFont3, bg=self.atriBg, width=6)
        self.btnVoltar.place(x=100, y=420)
        self.btnInserir.place(x=360, y=420)

    def widgetLogs(self):  
        self.top=Toplevel()
        self.top.title('Discador de Chamada V1.0')
        self.top.iconbitmap('image/phone.ico')
        self.top.resizable(FALSE,FALSE)
        self.top.geometry('{}x{}+{}+{}'.format(self.largura,self.altura,self.posx,self.posy))
        #Imagem de fundo    
        self.imagem4=Label(self.top)
        self.imagem4['image']=self.amostra
        self.imagem4.place(x=0,y=0)
        #ListaBox   
        self.labelLog=Label(self.top,text='Registro',font=self.atriFont,fg=self.atriFg)
        self.labelLog.pack()
        self.listaLog=Listbox(self.top,width=100,height=22)
        self.listaLog.pack()
        #Botões 
        self.btnlargura=6
        self.btnBuscar=Button(self.top,text='Buscar',fg=self.atriFg,bd=self.atriBd,relief=self.atriRelief,
        font=self.atriFont,bg=self.atriBg,width=self.btnlargura)
        self.btnFiltro=Button(self.top,text='Filtro',fg=self.atriFg,bd=self.atriBd,relief=self.atriRelief,
        font=self.atriFont,bg=self.atriBg,width=self.btnlargura)
        self.btnVoltar=Button(self.top,text='Voltar',command=self.top.destroy,fg=self.atriFg,bd=self.atriBd,relief=self.atriRelief,
        font=self.atriFont,bg=self.atriBg,width=self.btnlargura)
        self.btnBuscar.place(x=100,y=420)
        self.btnFiltro.place(x=330,y=420)
        self.btnVoltar.place(x=550,y=420)

    def botaoAdicionar(self):
        if (self.contador<4):
            self.ent = Entry(self.top, width=20)
            self.ent.place(x=100, y=(80+self.py))
            self.btnAdicionar = Button(self.top,command=self.botaoAdicionar, text='+', fg=self.atriFg, bd=self.atriBd, relief=self.atriRelief, font=self.atriFont2, bg=self.atriBg)
            self.btnAdicionar.place(x=225, y=(76+self.py))
            self.py+=50
            self.contador+=1
        
        

if __name__ == "__main__":  
    root=Tk()
    app=CallManager(root)
    root.mainloop()
             