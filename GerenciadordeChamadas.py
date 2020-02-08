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
meuMenu.add_cascade(label='Ajuda', menu=help_menu)
meuMenu.add_cascade(label='Configuração', menu=config_menu)
root.config(menu=meuMenu)

#Frame
frame_a=Frame(root).place()
frame_b=Frame(root).place()

# Botões primeira fila
btn_buscar=Button(frame_a, text='Buscar', fg='#002e4d',bd=8,width=8,height=3, relief=RAISED ,bg='#80ccff',font='Verdana 25 bold')
btn_buscar.place(x=20,y=50)

btn_ligar=Button(frame_a, text='Ligar', fg='#002e4d',bd=8,width=8,height=3, relief=RAISED,bg='#80ccff',font='Verdana 25 bold')
btn_ligar.place(x=307,y=50)

btn_mensagem=Button(frame_a, text='MSG', fg='#002e4d',bd=8,width=8,height=3, relief=RAISED,bg='#80ccff',font='Verdana 25 bold')
btn_mensagem.place(x=580,y=50)


# Botões Segunda fila

btn_importarArquivo=Button(frame_b, text='Importar\nArquivo', fg='#002e4d',bd=8,width=8,height=3, relief=RAISED ,bg='#80ccff',font='Verdana 25 bold')
btn_importarArquivo.place(x=20,y=250)

btn_number=Button(frame_b, text='Inserir\nNúmero', fg='#002e4d',bd=8,width=8,height=3, relief=RAISED,bg='#80ccff',font='Verdana 25 bold')
btn_number.place(x=307,y=250)

btn_executar=Button(frame_b, text='Executar', fg='#002e4d',bd=8,width=8,height=3, relief=RAISED,bg='#80ccff',font='Verdana 25 bold')
btn_executar.place(x=580,y=250)

root.geometry('{}x{}+{}+{}'.format(largura,altura,posx,posy))
root.mainloop()
