from tkinter import  *
import sqlite3

conn = sqlite3.connect(r'C:/Users/anderson.bispo/Downloads/ControlSchool-master/Database/Escola.db')
c = conn.cursor()

resultado = c.execute("SELECT MAX(id) from PROFESSOR")
for a in resultado:
    id = a[0]
    class Database:
        def __init__(self,  master, *args, **kwargs):

            #

            self.master = master
            self.heading = Label(master, text="Cadastro de Professores",  font=('Arial 30 bold'), fg='blue')
            self.heading.place(x=200, y=0)
            

            # Label com a indicação das informações (nome, cpf, entre outros dados

            self.nome_1 = Label(master, text="NOME :",  font=('Arial 12 bold'))
            self.nome_1.place(x=20, y=70)

            self.cpf_1 = Label(master, text="CPF :",  font=('Arial 12 bold'))
            self.cpf_1.place(x=570, y=70)

            self.fone_1 = Label(master, text="FONE :",  font=('Arial 12 bold'))
            self.fone_1.place(x=560, y=110)

            self.disciplina_1 = Label(master, text="DISCIPLINA",  font=('Arial 12 bold'))
            self.disciplina_1.place(x=20, y=150)

            self.turno_1 = Label(master, text="TURNO",  font=('Arial 12 bold'))
            self.turno_1.place(x=20, y=110)

            self.hora_1 = Label(master, text="DIA DA SEMANA",  font=('Arial 12 bold'))
            self.hora_1.place(x=20, y=280)

            # Entry para entrada de informações

            self.nome_e = Entry(master, width=50,  font=('Arial 12 bold'))
            self.nome_e.place(x=100, y=70)

            self.cpf_e = Entry(master, width=25,  font=('Arial 12 bold'))
            self.cpf_e.place(x=620, y=70)

            self.fone_e = Entry(master, width=25,  font=('Arial 12 bold'))
            self.fone_e.place(x=620, y=110)


            # Checkbutton do Turno

            self.c = Checkbutton(master, text="MATUTINO", font=('Arial 10 bold'))
            self.c.place(x=100,y=110)

            self.c = Checkbutton(master, text="VESPERTINO", font=('Arial 10 bold'))
            self.c.place(x=210,y=110)

            self.c = Checkbutton(master, text="NOTURNO", font=('Arial 10 bold'))
            self.c.place(x=340,y=110)

            # Checkbutton Dia da Semana

            self.c = Checkbutton(master, text="SEGUNDA-FEIRA", font=('Arial 10 bold'))
            self.c.place(x=20,y=310)

            self.c = Checkbutton(master, text="TERÇA-FEIRA", font=('Arial 10 bold'))
            self.c.place(x=20,y=340)

            self.c = Checkbutton(master, text="QUARTA-FEIRA", font=('Arial 10 bold'))
            self.c.place(x=20,y=370)

            self.c = Checkbutton(master, text="QUINTA-FEIRA", font=('Arial 10 bold'))
            self.c.place(x=150,y=310)

            self.c = Checkbutton(master, text="SEXTA-FEIRA", font=('Arial 10 bold'))
            self.c.place(x=150,y=340)

            # Checkbutton do Disciplina

            self.c = Checkbutton(master, text="PORTUGUÊS", font=('Arial 10 bold'))
            self.c.place(x=20,y=180)

            self.c = Checkbutton(master, text="MATEMATICA", font=('Arial 10 bold'))
            self.c.place(x=20,y=210)

            self.c = Checkbutton(master, text="GEOGRAFIA", font=('Arial 10 bold'))
            self.c.place(x=20,y=240)

            self.c = Checkbutton(master, text="HISTORIA", font=('Arial 10 bold'))
            self.c.place(x=135,y=180)

            self.c = Checkbutton(master, text="INGLÊS", font=('Arial 10 bold'))
            self.c.place(x=135,y=210)

            self.c = Checkbutton(master, text="QUIMICA", font=('Arial 10 bold'))
            self.c.place(x=135,y=240)

            self.c = Checkbutton(master, text="ESPANHOL", font=('Arial 10 bold'))
            self.c.place(x=230,y=180)

            self.c = Checkbutton(master, text="RELIGIÃO", font=('Arial 10 bold'))
            self.c.place(x=230,y=210)

            self.c = Checkbutton(master, text="FÍSICA", font=('Arial 10 bold'))
            self.c.place(x=230,y=240)

            self.c = Checkbutton(master, text="INFORMÁTICA", font=('Arial 10 bold'))
            self.c.place(x=325,y=180)

            self.c = Checkbutton(master, text="EMPREENDEDORISMO", font=('Arial 10 bold'))
            self.c.place(x=325,y=210)

            self.c = Checkbutton(master, text="ED. FÍSICA", font=('Arial 10 bold'))
            self.c.place(x=325,y=240)

            #

            self.btn_add = Button(master, text="SALVAR", width=10,  font=('Arial 10 bold'), bg='blue', fg='white')
            self.btn_add.place(x=125, y=550)

            self.btn_add = Button(master, text="CANCELAR", width=10,  font=('Arial 10 bold'), bg='red', fg='white')
            self.btn_add.place(x=225, y=550)


            #

            self.tBox = Text(master, width=50, height=18)
            self.tBox.place(x=890, y=70)
            self.tBox.insert(END, "ULTIMO REGISTRO :")

        def get_items(self, master, *args, **kwargs):
            self.name = self.name_e.get()
            self.name = self.name_e.get()
            self.name = self.name_e.get()
            self.name = self.name_e.get()
            

            

    root = Tk()
    root.iconbitmap("C:\\Users\\anderson.bispo\\Downloads\\ControlSchool-master\\icone\\calendarG.ico")
    b = Database(root)

    root.geometry("880x520+0+0")
    root.title("CADASTRO DE PROFESSORES")

    root.mainloop()
