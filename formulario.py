from tkinter import*
from tkinter import ttk
#### Falta instalar paquete cv2

def send_data():
    usuario_info = usuario.get()
    contraseña_info = contraseña.get()
    numero_info=numero.get()
    cajas_info=numero.get()
    pist_info=barras.get()
    print(usuario_info ,"\t", contraseña_info,"\t",numero_info,"\t",cajas_info,"\t",pist_info,"\t")
    

    file = open("Registro.xls","a")
    file.write(usuario_info)
    file.write("\t")
    file.write(contraseña_info)
    file.write("\t")
    file.write(numero_info)
    file.write("\t")
    file.write(pist_info)
    file.write("\t")
    file.close()
    print("Usuario registrado. Usuario:{} ".format(usuario_info))

    usuario_entry.delete(0, END)
    contraseña_entry.delete(0, END)
    numero_entry.delete(0,END)
    barras_entry.delete(0,END)










### Creacion de la ventana
miventana=Tk()
miventana.geometry("720x680")
miventana.title("Formulario")
miventana.resizable(False,False)
miventana.config(background="#FFFFF0")### Color Ivory
main_title = Label(text = "Registro", font=("Cambria",14), bg = "#FFFFF0", fg="black",width="500",height="2")
main_title.pack()



usuario_label = Label(text ="Usuario", bg ="#FFEEDD")
usuario_label.place(x=22,y=70)
contraseña_label=Label(text="Contraseña", bg="#FFEEDD")
contraseña_label.place(x=22, y=130)

cajas_combo = ttk.Combobox(text="Color de caja",state="readonly",
    values=["Rojo","Azul"]
)
cajas_label=Label(text ="Color de camisas ", bg ="#FFEEDD")
cajas_label.place(x=350,y=60)
cajas_combo.place(x=350,y=90)

numero_label = Label(text ="Cantidad de camisas", bg ="#FFEEDD")
numero_label.place(x=350,y=140)

barras_label=Label(text="Barras", bg="#FFEEDD")
barras_label.place(x=350, y= 200)

usuario=StringVar()
contraseña = StringVar()
numero=StringVar()
barras=StringVar()


usuario_entry=Entry(textvariable =  usuario,width = "40")
contraseña_entry=Entry(textvariable = contraseña,width = "40", show ="*")
numero_entry=Entry(textvariable =  numero,width = "10")
barras_entry=Entry(textvariable = barras,width="40")





usuario_entry.place(x=22, y=100)
contraseña_entry.place(x=22, y=160)
numero_entry.place(x=350, y=160)
barras_entry.place(x=350, y= 220)






submit_btn=Button(miventana,text="Ingresar", width="30",height="2", command=send_data, bg="#00CD63")
submit_btn.place(x=170,y=290)



miventana.mainloop()