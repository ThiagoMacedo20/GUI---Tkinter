from tkinter import *

root=Tk()
root.title('Call Manager')
root.iconbitmap('image/phone.ico')
root['bg']='#008ae6'
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
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label='Exit',command=root.destroy)

help_menu=Menu(meuMenu,tearoff=0)

config_menu=Menu(meuMenu,tearoff=0)


meuMenu.add_cascade(label='Arquivo', menu=file_menu)
meuMenu.add_cascade(label='Ajua', menu=help_menu)
meuMenu.add_cascade(label='Configuração', menu=config_menu)
root.config(menu=meuMenu)
# Imagem de fundo

# Variáveis da personalização dos botões
btn_largura=8
btn_altura=3
btn_bd=8
btn_relief=RAISED
btn_bg='#80ccff'
btn_fg='#002e4d'
btn_font=('Verdana 25 bold')

#Frame
frame_a=Frame(root).place()
frame_b=Frame(root).place()

# Botões primeiro frame

btn_buscar=Button(frame_a, text='Buscar', fg=btn_fg,bd=btn_bd,width=btn_largura,height=btn_altura,relief=btn_relief ,bg=btn_bg,font=btn_font)
btn_buscar.place(x=20,y=50)
btn_buscar.bind('<Return>') 


btn_ligar=Button(frame_a, text='Ligar', fg=btn_fg,bd=btn_bd,width=btn_largura,height=btn_altura, relief=btn_relief ,bg=btn_bg,font=btn_font)
btn_ligar.place(x=307,y=50)
btn_ligar.bind('<Return>')

btn_mensagem=Button(frame_a, text='SMS',fg=btn_fg,bd=btn_bd,width=btn_largura,height=btn_altura,relief=btn_relief ,bg=btn_bg,font=btn_font)
btn_mensagem.place(x=580,y=50)
btn_mensagem.bind('<Return>')


# Botões segundo frame

btn_importarArquivo=Button(frame_b, text='Importar\nArquivo',fg=btn_fg,bd=btn_bd,width=btn_largura,height=btn_altura,relief=btn_relief ,bg=btn_bg,font=btn_font)
btn_importarArquivo.place(x=20,y=250)
btn_importarArquivo.bind('<Return>')

btn_number=Button(frame_b, text='Inserir\nNúmero', fg=btn_fg,bd=btn_bd,width=btn_largura,height=btn_altura,relief=btn_relief ,bg=btn_bg,font=btn_font)
btn_number.place(x=307,y=250)
btn_number.bind('<Return>')


btn_executar=Button(frame_b, text='Executar', fg=btn_fg,bd=btn_bd,width=btn_largura,height=btn_altura, relief=btn_relief ,bg=btn_bg,font=btn_font)
btn_executar.place(x=580,y=250)
btn_executar.bind('<Return>')

root.geometry('{}x{}+{}+{}'.format(largura,altura,posx,posy))
root.mainloop()
