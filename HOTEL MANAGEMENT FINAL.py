from tkinter import *
from tkinter.messagebox import *
from tkcalendar import *
import random
import mysql.connector
from datetime import datetime

try:
    mydb = mysql.connector.connect(host='localhost',database='ankitjain',user='root',password='Ankit')
except:
    print("Connection Failed")
mycursor = mydb.cursor()
mycursor.execute("create table if not exists hotel_data(Room_number int(11) primary key ,Name varchar(25) ,Phone_number bigint(11),Check_in varchar(15),Room_rent int,Total_bill float,Check_out varchar(15) )")
mycursor.execute("create table if not exists hotel_records(Room_number int(11) primary key, Restaurant_bill int , Game_bill int, Extra_bed int, Laundry_bill int,Room_rent int)")

tb=0
def Customer_Data():
    main1.iconify()
    Data=Tk()
    Data.title("Customer Data")
    Data.geometry('600x600')

    l1=Label(Data,text="Please Enter your information",font=('Oswald',18,'bold'),foreground='#0039CF')
    l1.place(x=1,y=1)
    
    n=Label(Data,text="Enter your name:")
    ne=Entry(Data,width=50)
    n.place(x=2,y=100)
    ne.place(x=150,y=100)

    p=Label(Data,text="Enter your Phone number:")
    pn=Entry(Data,width=50)
    p.place(x=2,y=130)
    pn.place(x=150,y=130)

    check_in_label = Label(Data, text="Check-in Date:")
    check_in_label.place(x=2,y=160)
    in_cal = DateEntry(Data, width=12, background='darkblue', foreground='white', borderwidth=2)
    in_cal.place(x=150,y=160)

    check_out_label = Label(Data, text="Check-out Date:")
    check_out_label.place(x=2,y=190)
    out_cal = DateEntry(Data, width=12, background='darkblue', foreground='white', borderwidth=2)
    out_cal.place(x=150,y=190)

    ROOM=Label(Data,text="SELECT HOTEL ROOM",font=('Oswald',11,'bold'),foreground='#0011DE')
    ROOM.place(x=150,y=230)
    room_type_var = StringVar(Data, "A")
    RoomA=Radiobutton(Data, text="Deluxe (Rs. 6000 PN)", variable=room_type_var, value="A")
    RoomB=Radiobutton(Data, text="Standard (Rs. 5000 PN)", variable=room_type_var, value="B")
    RoomA.place(x=150,y=260)
    RoomB.place(x=150,y=290)
    
    def sub():
        global tb
        if not ne.get().replace(" ", "").isalpha():
            showinfo("Invalid Input", "Please enter a valid name")
            return  

        try:
            y = str(pn.get())
        except:
            showinfo("Invalid Input", "Please Enter your correct Phone number")
            return  

        if len(y) != 10:
            showinfo("Invalid Input", "Please Enter your correct 10-digit Phone number")
            return  

        in_date = in_cal.get_date()
        out_date = out_cal.get_date()   
        delta = out_date - in_date
        stay = delta.days   
        stay=int(stay)
        

        room_number_assigned = None
        while True:
            room_number_assigned = random.randint(108, 122)
            mycursor.execute("SELECT count(*) FROM Hotel_data WHERE Room_number = {}".format(room_number_assigned))
            results = mycursor.fetchall()
            if results == [(1,)]:
                continue
            else:
                break
            
        roomtext = Label(Data, text="Your Room Number is")
        roomnumber = Label(Data, text=room_number_assigned)
        
        roomtext.place(x=10, y=370)
        roomnumber.place(x=120, y=370)     
        if room_type_var.get()=='A':
            X3=6000*stay
        if room_type_var.get()=='B':
            X3=5000*stay

        tb+=X3
        name=ne.get()
        mycursor.execute("insert into  hotel_data(Room_number,Name,Phone_number,Check_in,Room_rent,Total_bill,Check_out) values({},'{}',{},'{}',{},{},'{}')".format(room_number_assigned,name,y,in_date,X3,tb,out_date))
        mycursor.execute("insert into  hotel_records(Room_number,Restaurant_bill,Game_bill,Extra_Bed,Laundry_bill,Room_rent) values({},0,0,0,0,{})".format(room_number_assigned,X3))
        mydb.commit()

        def Back2mm():
            Data.destroy()
            main1.deiconify()

        Back=Button(Data,text="Back to Main Menu",command=Back2mm)
        Back.place(x=5,y=400)

    Submit=Button(Data,text="SUBMIT",font=('Oswald',10,'bold'),background='#5492FF',command=sub)
    Submit.place(x=5,y=340)
    Data.mainloop()



def Services():
    global tb
    main1.iconify()
    Serv=Tk()
    Serv.title("Extra Services")
    Serv.geometry('600x600')

    l=Label(Serv,text="SERVICES",font=('Oswald',14,'bold'))
    l.pack()

    nl=Label(Serv,text="Enter your Room Number:")
    nl.place(x=2,y=30)
    rn=Entry(Serv,width=50)
    rn.place(x=160,y=30)
    
        
    l1=Label(Serv,text="Extra bed Cost is Rs.850:")
    l2=Spinbox(Serv,from_=0,to=1)
    l1.place(x=2,y=50)
    l2.place(x=160,y=50)
    
    r=Label(Serv,text="Restaurant",font=("Oswald",11,'underline'))
    r.place(x=2,y=80)

    r1=Label(Serv,text="Breakfast------Rs.150")
    r2=Spinbox(Serv,from_=0,to=5)
    r1.place(x=2,y=110)
    r2.place(x=130,y=110)
    
    
    r3=Label(Serv,text="Lunch----------Rs.250")
    r4=Spinbox(Serv,from_=0,to=5)
    r3.place(x=2,y=130)
    r4.place(x=130,y=130)
    
    r5=Label(Serv,text="Dinner---------Rs.350")
    r6=Spinbox(Serv,from_=0,to=5)
    r5.place(x=2,y=150)
    r6.place(x=130,y=150)
    
    g=Label(Serv,text="Gaming Centre",font=("Oswald",11,'underline'))
    g.place(x=2,y=180)

    g1=Label(Serv,text="Bowling--------Rs.100")
    g2=Spinbox(Serv,from_=0,to=5)
    g1.place(x=2,y=210)
    g2.place(x=130,y=210)
    
    g3=Label(Serv,text="Snooker--------Rs.250")
    g4=Spinbox(Serv,from_=0,to=5)
    g3.place(x=2,y=230)
    g4.place(x=130,y=230)
    
    g5=Label(Serv,text="Tennis---------Rs.400")
    g6=Spinbox(Serv,from_=0,to=5)
    g5.place(x=2,y=250)
    g6.place(x=130,y=250)
    
    L=Label(Serv,text="Laundry",font=("Oswald",11,'underline'))
    L.place(x=2,y=310)

    Lm=Label(Serv,text="Laundry Service Charge: Rs.50/cloth")
    Lm.place(x=2,y=330)
    Cloth=Label(Serv,text="Enter the number of cloths")
    Cloth_num=Spinbox(Serv,from_=0,to=10)
    Cloth.place(x=2,y=350)
    Cloth_num.place(x=150,y=350)
    
    def sub():
        global tb
        nonlocal rn
        room=int(rn.get())
        rbill=gbill=lbill=ebill=sbill=0
        if int(l2.get())==1:
            ebill=850
            tb+=ebill
            mycursor.execute("update hotel_records set Extra_bed=1 where Room_number=%s",(room,))

        rbill+=(int(r2.get())*150 + int(r4.get())*250 + int(r6.get())*350)
        tb+=rbill
        mycursor.execute("update hotel_data set Total_Bill=Total_bill+%s where Room_number=%s",(tb,room))
        mycursor.execute("update Hotel_records set Restaurant_bill=Restaurant_bill + %s where Room_number=%s",(rbill,room))
        
        gbill+=(int(g2.get())*100 + int(g4.get())*250 + int(g6.get())*400)
        tb+=gbill
        mycursor.execute("update hotel_data set Total_Bill=Total_bill+%s where Room_number=%s",(tb,room))
        mycursor.execute("update Hotel_records set Game_bill=Game_bill+%s where Room_number=%s",(gbill,room))
        
        lbill+=int(Cloth_num.get())*50
        tb+=lbill
        mycursor.execute("update Hotel_records set Laundry_Bill=Laundry_bill+%s where Room_number=%s",(lbill,room))
        mycursor.execute("update hotel_data set Total_Bill=Total_bill+%s where Room_number=%s",(tb,room))

        sbill=lbill+ebill+lbill+gbill
        F=Label(Serv,text="Your Services bill is",font=('Oswald',10,'bold'))
        F.place(x=5,y=440)
        B=Label(Serv,text=sbill,font=('Oswald',10,'bold')) 
        B.place(x=150,y=440)       
        mydb.commit()

        def Back2mm():
            Serv.destroy()
            main1.deiconify()

        Back=Button(Serv,text="Back to Main Menu",background='#5492FF',command=Back2mm)
        Back.place(x=5,y=480)

    Submit=Button(Serv,text="SUBMIT",font=('Oswald',10,'bold'),background='#5492FF',command=sub)
    Submit.place(x=5,y=400)
    Serv.mainloop()


def Cost():
    main1.iconify()
    Costwin=Tk()
    Costwin.title("Total Cost")
    Costwin.geometry('600x600')

    l=Label(Costwin,text="TOTAL BILL",font=('Oswald',14,'bold'))
    l.pack()

    nr=Label(Costwin,text="Enter your Room Number:")
    nr.place(x=2,y=30)
    nl=Entry(Costwin,width=50)
    nl.place(x=160,y=30)
    
    def sub():
        room=int(nl.get())

        mycursor.execute("select Total_Bill from hotel_data where Room_number=%s",(room,))
        xt=mycursor.fetchall()
        mycursor.execute("select Room_rent from hotel_data where Room_number=%s",(room,))
        xr=mycursor.fetchall()
        mycursor.execute("select Restaurant_Bill from hotel_records where Room_number=%s",(room,))
        xe=mycursor.fetchall()
        mycursor.execute("select Game_bill from hotel_records where Room_number=%s",(room,))
        xg=mycursor.fetchall()
        mycursor.execute("select Extra_Bed from hotel_records where Room_number=%s",(room,))
        xb=mycursor.fetchall()
        mycursor.execute("select Laundry_Bill from hotel_records where Room_number=%s",(room,))
        xl=mycursor.fetchall()

        try:
            total=xt[0][0]
            r=xr[0][0]
            e=xe[0][0]
            g=xg[0][0]
            bed=xb[0][0]
            l=xl[0][0]
        except:
            showinfo("Error","Technical Error")

        if bed==1:
            b=850
        
        gst=total*0.18

        L=Label(Costwin,text="HOTEL COUNTRY INN",font=('Oswald',15,'bold'))
        L.place(x=200,y=100)

        L=Label(Costwin,text="ROOM RENT",font=('Oswald',9,''))
        L.place(x=200,y=150)
        L=Label(Costwin,text=r,font=('Oswald',9,''))
        L.place(x=350,y=150)

        L=Label(Costwin,text="RESTAURANT BILL",font=('Oswald',9,''))
        L.place(x=200,y=170)
        L=Label(Costwin,text=e,font=('Oswald',9,''))
        L.place(x=350,y=170)

        L=Label(Costwin,text="GAME BILL",font=('Oswald',9,''))
        L.place(x=200,y=190)
        L=Label(Costwin,text=g,font=('Oswald',9,''))
        L.place(x=350,y=190)

        L=Label(Costwin,text="EXTRA BED",font=('Oswald',9,''))
        L.place(x=200,y=210)
        L=Label(Costwin,text=b,font=('Oswald',9,''))
        L.place(x=350,y=210)

        L=Label(Costwin,text="LAUNDRY BILL",font=('Oswald',9,''))
        L.place(x=200,y=230)
        L=Label(Costwin,text=l,font=('Oswald',9,''))
        L.place(x=350,y=230)

        L=Label(Costwin,text="BILLED AMOUNT",font=('Oswald',9,''))
        L.place(x=200,y=290)
        L=Label(Costwin,text=total,font=('Oswald',9,''))
        L.place(x=350,y=290)

        L=Label(Costwin,text="TAX @ 18% GST",font=('Oswald',9,''))
        L.place(x=200,y=310)
        L=Label(Costwin,text=gst,font=('Oswald',9,''))
        L.place(x=350,y=310)

        L=Label(Costwin,text="TOTAL AMOUNT",font=('Oswald',9,''))
        L.place(x=200,y=330)
        L=Label(Costwin,text=total+gst,font=('Oswald',9,''))
        L.place(x=350,y=330)

        def Back2mm():
                Costwin.destroy()
                main1.deiconify()

        Back=Button(Costwin,text="Back to Main Menu",background='#5492FF',command=Back2mm)
        Back.place(x=5,y=400)

    Submit=Button(Costwin,text="SUBMIT",font=('Oswald',10,'bold'),background='#5492FF',command=sub)
    Submit.place(x=5,y=60)
    Costwin.mainloop()



main1=Tk()
main1.title("HOTEL COUNTRY INN")
main1.geometry('600x600')
Hotel_name=Label(main1,text='WELCOME TO HOTEL COUNTRY INN',font=('Oswald', 20, 'bold'),foreground='#1D4AC1')
Hotel_name.pack(padx=10,pady=10)

X4=X5=X6=0
laundry_bill=0
bed=0
tb=0  

Ch=Label(main1,text="Please Select", font=('Oswald',12))
Ch.place(x=5,y=100)

Cus_data=Button(main1,text='ENTER CUSTOMER DATA',borderwidth=5,background='Sky Blue',command=Customer_Data)
Cus_data.place(x=20,y=130)

Extra=Button(main1,text='ANY EXTRA SERVICES REQUIRED',borderwidth=5,background='Sky Blue',command=Services)
Extra.place(x=20,y=180)

T_cost=Button(main1,text='SHOW TOTAL COST,WITH GST(18%)',borderwidth=5,background='Sky Blue',command=Cost)
T_cost.place(x=20,y=230)

Close=Button(main1,text='EXIT',borderwidth=5,background='#F88167',command=exit)
Close.place(x=20,y=280)

main1.mainloop()





