from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.title('Discador de Chamada V1.0')
root.iconbitmap('image/phone.ico')
root.resizable(FALSE,FALSE)

# Dimensões da janela Inicial
largura=800
altura=500
largura_screen=root.winfo_screenwidth()
altura_screen=root.winfo_screenheight()
posx=int((largura_screen/2)-largura/2)
posy=int(altura_screen/2-altura/2)
# Menu de Opções
meuMenu=Menu(root)

file_menu=Menu(meuMenu,tearoff=0)
file_menu.add_command(label="Novo")
file_menu.add_command(label="Importar")
file_menu.add_command(label="Exportar")
file_menu.add_separator()
file_menu.add_command(label='Sair',command=root.destroy)

help_menu=Menu(meuMenu,tearoff=0)

config_menu=Menu(meuMenu,tearoff=0)


meuMenu.add_cascade(label='Arquivo', menu=file_menu)
meuMenu.add_cascade(label='Ajuda', menu=help_menu)
meuMenu.add_cascade(label='Configuração', menu=config_menu)
root.config(menu=meuMenu)
# Imagem de fundo

photo=ImageTk.PhotoImage(Image.open('image/imagemdebg.png'))
label = Label(root,image=photo)# keep a reference!
label.place(x=0,y=0)


# Variáveis da personalização dos botões
btn_largura=10
btn_altura=3
btn_bd=8
btn_relief=RAISED
btn_bg='#e0ebeb'
btn_fg='#002e4d'
btn_font=('Verdana 25 bold')


#Frame
frame_a=Frame(root).place()
frame_b=Frame(root).place()

# Botões primeiro frame

btn_buscar=Button(frame_a, text='Pesquisar',fg=btn_fg,bd=btn_bd,width=btn_largura,height=btn_altura,relief=btn_relief ,bg=btn_bg,font=btn_font)
btn_buscar.place(x=80,y=50)
btn_buscar.bind('<Return>') 


btn_ligar=Button(frame_a, text='Inserir', fg=btn_fg,bd=btn_bd,width=btn_largura,height=btn_altura, relief=btn_relief ,bg=btn_bg,font=btn_font)
btn_ligar.place(x=480,y=50)
btn_ligar.bind('<Return>')

# Botões segundo frame

btn_logs=Button(frame_b, text='Logs',fg=btn_fg,bd=btn_bd,width=btn_largura,height=btn_altura,relief=btn_relief ,bg=btn_bg,font=btn_font)
btn_logs.place(x=80,y=250)
btn_logs.bind('<Return>')


btn_executar=Button(frame_b, text='Executar', fg=btn_fg,bd=btn_bd,width=btn_largura,height=btn_altura, relief=btn_relief ,bg=btn_bg,font=btn_font)
btn_executar.place(x=480,y=250)
btn_executar.bind('<Return>')


root.geometry('{}x{}+{}+{}'.format(largura,altura,posx,posy))
root.mainloop()
