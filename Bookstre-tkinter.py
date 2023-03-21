from tkinter import *
from Bookstore import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Bookstore")
root.geometry("300x200")

def proizvodi():
    t1=Toplevel(root)
    t1.geometry("700x300")
    t1.title("Lista proizvoda")
    l_t1=Label(t1,text="U ponudi imamo sledeće:")
    l_t1.grid(row=0, column=0)

    def olovke():
        l1_o= Label(t1, text="")
        l1_o.grid(row=1,column=1)
        l11=Label(t1, text="Kolicina: ")
        l11.grid(row=1,column=2)
        e1=Entry(t1)
        e1.insert(1,"1")
        e1.grid(row=1, column=3)
        opis = P.lista[0].opis
        cena = P.lista[0].cena
        l1_o.configure(text= opis+" "+ "Cena: "+ " " + str(cena)+ "din")
        dodaj_u_korpu = Button(t1, text="Dodaj u korpu",
                               command=lambda: [K.dodaj_proizvod(P.lista[0], e1.get()),
                                                dodaj_u_korpu.config(state='disabled')])
        dodaj_u_korpu.grid(row=1, column=4)

    b1 = Button(t1, text=P.lista[0].naziv, command=lambda: olovke())
    b1.grid(row=1, column=0)
    

    def sveske():
        l2 = Label(t1, text="")
        l2.grid(row=2, column=1)
        l22=Label(t1, text="Kolicina: ")
        l22.grid(row=2,column=2)
        e2=Entry(t1)
        e2.insert(1,"1")
        e2.grid(row=2,column=3)
        opis = P.lista[1].opis
        cena = P.lista[1].cena
        l2.configure(text= opis+" "+ "Cena: "+ " " + str(cena)+ "din")
        dodaj_u_korpu = Button(t1, text="Dodaj u korpu",
                               command=lambda: [K.dodaj_proizvod(P.lista[1], e2.get()),
                                                dodaj_u_korpu.config(state='disabled')])
        dodaj_u_korpu.grid(row=2,column=4)

    b2 = Button(t1, text=P.lista[1].naziv, command=lambda: sveske())
    b2.grid(row=2, column=0)

    def flomasteri():
        l3 = Label(t1, text="")
        l3.grid(row=3, column=1)
        l33=Label(t1, text="Kolicina: ")
        l33.grid(row=3, column=2)
        e3=Entry(t1)
        e3.insert(1,"1")
        e3.grid(row=3, column=3)
        opis = P.lista[2].opis
        cena = P.lista[2].cena
        l3.configure(text= opis+" "+ "Cena: "+ " " + str(cena)+ "din")
        dodaj_u_korpu = Button(t1, text="Dodaj u korpu",
                               command=lambda: [K.dodaj_proizvod(P.lista[2], e3.get()),
                                                dodaj_u_korpu.config(state='disabled')])
        dodaj_u_korpu.grid(row=3, column=4)
        

    b3 = Button(t1, text=P.lista[2].naziv, command=lambda:flomasteri())
    b3.grid(row=3, column=0)


    def fascikla():
        l4 = Label(t1, text="")
        l4.grid(row=4, column=1)
        l44=Label(t1, text="Kolicina: ")
        l44.grid(row=4, column=2)
        e4=Entry(t1)
        e4.insert(1,"1")
        e4.grid(row=4, column=3)
        opis = P.lista[3].opis
        cena = P.lista[3].cena
        l4.configure(text= opis+" "+ "Cena: "+ " " + str(cena)+ "din")
        dodaj_u_korpu = Button(t1, text="Dodaj u korpu",
                                command=lambda:[K.dodaj_proizvod(P.lista[3], e4.get()),
                                                dodaj_u_korpu.config(state='disabled')])
        dodaj_u_korpu.grid(row=4, column=4)
        

    b4 = Button(t1, text = P.lista[3].naziv, command=lambda: fascikla())
    b4.grid(row = 4, column =0)
    
    def roler():
        l5 = Label(t1, text="")
        l5.grid(row=5, column=1)
        l55=Label(t1, text="Kolicina: ")
        l55.grid(row=5, column=2)
        e5=Entry(t1)
        e5.insert(1,"1")
        e5.grid(row=5, column=3)
        opis = P.lista[4].opis
        cena = P.lista[4].cena
        l5.configure(text= opis+" "+ "Cena: "+ " " + str(cena)+ "din")
        dodaj_u_korpu = Button(t1, text="Dodaj u korpu",
                                    command=lambda:[K.dodaj_proizvod(P.lista[4], e5.get()),
                                                    dodaj_u_korpu.config(state='disabled')])
        dodaj_u_korpu.grid(row=5, column=4)

    b5 = Button(t1, text = P.lista[4].naziv, command=lambda: roler())
    b5.grid(row = 5, column =0)
   


def korpa():
    t2=Toplevel(root)
    t2.geometry("200x400")
    t2.title("Korpa")

    l = Label(t2, text="Proizvodi u korpi:")
    l.pack()
    l2_t2=Label(t2,text="")
    l2_t2.pack()

    lb = Listbox(t2)
    lb.pack()

    for proizvod in K.pregled_korpe():
        lb.insert(END, proizvod)

    ukloni=Button(t2, text="Ukloni", command=lambda: ukloni_iz_korpe())
    ukloni.pack()

    racun = Button(t2, text ="Racun", command=lambda: l2_t2.configure(text=K.racun()))
    racun.pack()

    stampaj_racun = Button(t2, text="Štampaj račun", command=lambda: K.stampaj_racun())
    stampaj_racun.pack()

    def ukloni_iz_korpe():
        if lb.curselection():
            proizvod = K.lista_proizvoda[lb.curselection()[0]]
            K.ukloni_proizvod(proizvod)
            lb.delete(ANCHOR)
            l2_t2.config(text="")

    def prikazi_cenu(event):
        if lb.curselection():
            proizvod = K.lista_proizvoda[lb.curselection()[0]]
            l2_t2.configure(text=f"{proizvod.naziv}: {proizvod.cena} din,\nKoličina: {proizvod.kolicina} kom")


    lb.bind("<<ListboxSelect>>", prikazi_cenu)

frame = Frame(root)
frame.grid(row=0, column=0)

b1 = Button(frame, text="Proizvodi", command=lambda: proizvodi())
b1.grid(row=0, column=0)

b2 = Button(frame, text="Korpa", command=lambda:korpa())
b2.grid(row=0, column=1)

b3 = Button(frame, text="Pretraga", command=lambda:l1.configure(text= P.pretraga_proizvoda_po_imenu(e1_root.get())))
b3.grid(row=0, column=2)

e1_root = Entry(frame)
e1_root.grid(row=1, columnspan=3)
l1=Label(frame)
l1.grid(row=2, columnspan=3)

def pregled_proizvoda():
    t3=Toplevel(root)
    t3.title("Pregled ponude")
    t3.geometry("300x600")
    l_t3=Label(t3, text="")
    l_t3.pack()
    a=""
    for i in P.lista:
        a=a + str(i) +"\n"
    l_t3.configure(text=a)
    b_t3=Button(t3, text="Nazad", command=lambda: t3.destroy())   
    b_t3.pack()

def kontakt():
    t4 = Toplevel(root)
    t4.title("Kontakt")
    t4.geometry("200x150")
    l_t4=Label(t4,
               text="Kontakt informacije 'Bookstore'\nAdresa:\
                Vojvode Stepe\n 11010 Beograd\nTel\mob:\
                    064/4547584\nemail: bookstore@bookstore.com")
    l_t4.pack()
    b_t4=Button(t4, text="Nazad", command=lambda: t4.destroy())   
    b_t4.pack()

def about():
    t5 = Toplevel(root)
    t5.title("O nama")
    t5.geometry("630x200")
    l_t5=Label(t5, text="Bookstore je osnovana 2023. godine kao mala knjižara sa fokusom na proizvode školskog asortimana.\n \
               Danas u našoj knjižari možete pronaći širok izbor olovaka, rolera, fascikli, svezaka i drugih proizvoda za pisanje.\n \
               Naša knjižara nalazi se u ulici Vojvode Stepe.\nPozivamo vas da nas posetite i pronađete sve što vam je\n potrebno za uspešan početak nove školske ili poslovne godine.")
    l_t5.pack()
    b_t5=Button(t5, text="Nazad", command=lambda: t5.destroy())   
    b_t5.pack()

    
    
    


meni=Menu(root)
root.config(menu=meni)

file_menu=Menu(meni)
meni.add_cascade(label="Meni", menu=file_menu)
file_menu.add_command(label="Proizvodi u ponudi", command=pregled_proizvoda)
file_menu.add_command(label="Kontakt", command=kontakt)
file_menu.add_command(label="O nama", command = about)
file_menu.add_separator()
file_menu.add_command(label="Izađi", command=root.destroy)


img = ImageTk.PhotoImage(Image.open("download.jpg"))
image_label = Label(root, image=img)
image_label.grid(row=3, column=0)

root.mainloop()