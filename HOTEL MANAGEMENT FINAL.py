import random
import mysql.connector
from datetime import datetime

try:
    mydb = mysql.connector.connect(host='localhost',database='ankitjain',user='root',password='Ankit')
except:
    print("Connection Failed")


mycursor = mydb.cursor()
mycursor.execute("create table if not exists hotel_data(Room_number int(11) primary key ,Name char(25) ,Phone_number bigint(11),Check_in varchar(15),Room_rent float,Total_bill float,Check_out varchar(15) )")
mycursor.execute("create table if not exists hotel_records(Room_number int(11) primary key, Restaurant_bill float , Game_bill float, Extra_bed float, Laundry_bill float,Room_rent float)")

print("---------------------------------------")
print("*****WELCOME TO HOTEL COUNTRY INN*****")
print("---------------------------------------")
print()
print()
X4=X5=X6=0
laundry_bill=0
bed=0
tb=0    
while 1 == 1:
    print("PLEASE ENTER YOUR CHOICE")
    print("1.ENTER CUSTOMER DATA")
    print("2.ANY EXTRA SERVICES REQUIRED")
    print("3.SHOW TOTAL COST,WITH GST(18%)")
    print("4.EXIT")
    mainchoice = int(input("ENTER YOUR CHOICE:"))

    if mainchoice == 1:

        while True:
            X1 = input("ENTER YOUR NAME:")
            if all(i.isspace() or i.isalpha() for i in X1):
                break
            else:
                print("INVALID INPUT")
        while True:
            y = input("ENTER YOUR PHONE NUMBER:")
            if len(y) > 10 or len(y) < 10:
                print("INVALID INPUT")
            elif any(i.isspace() or i.isalpha() for i in y):
                print("INVALID INPUT")
            else:
                break

        while True:
            z=datetime.strptime((input("ENTER YOUR CHECKIN DATE(DD/MM/YY):")),"%d/%m/%y")
            v=datetime.strptime((input("ENTER YOUR CHECKOUT DATE(DD/MM/YY):")),"%d/%m/%y")
            if v<z :
                print("INVALID INPUT")
                continue
            else:
                break
        c_in=str(z)
        c_out=str(v)
        chc_in=c_in[0:10]
        chc_out=c_out[0:10]            

        print()
        print("HOTEL ROOMS")
        print("Type A---->rs 6000 PN\-")
        print("Type B---->rs 5000 PN\-")
        q=input("ENTER YOUR CHOICE:")
        T=v - z
        T=v-z
        r=""
        t=str(T)
        D=0

        for i in range (len(t)):
            if t[i].isspace():
                break
            else:
                r+=t[i]
        
        r=int(r)
        
        while True:
            room_number_assigned=random.randint(108,122)
            mycursor.execute("Select count(*) from Hotel_data where Room_number={}".format(room_number_assigned))
            results=mycursor.fetchall() 
            if results==[(1,)] :
                continue
            else:
                break
            
        if q=="A":
            
            
            X3=6000*r
            print("you have opted room type A")
            print("---------------------------------------")
            print("your room rent is =",X3)
            print("---------------------------------------")
            
        else:
            
            X3=5000*r
            print("you have opted room type B")
            print("---------------------------------------")
            print("your room rent is =",X3)
            print("---------------------------------------")
        print()
        print()
        print("--------------------------------")
        print("Your Room Number is",room_number_assigned)
        print("--------------------------------")
        tb=tb+X3
        print(tb)
        mycursor.execute("insert into  Hotel_data(Name,Phone_number,Room_number,Total_Bill) values('{}',{},{},{})".format(X1,y,room_number_assigned,tb))
        mycursor.execute("insert into  Hotel_records(Room_number,Restaurant_bill,Game_bill,Extra_Bed,Laundry_bill,Room_rent) values('{}',0,0,0,0,0)".format(room_number_assigned))
        mycursor.execute("update Hotel_records set Room_rent={} where Room_number={}".format(X3,room_number_assigned))
        mycursor.execute("update Hotel_data set check_in='{}' where Room_number={}".format(chc_in,room_number_assigned))    
        mycursor.execute("update Hotel_data set check_out='{}' where Room_number={}".format(chc_out,room_number_assigned))


        mydb.commit()       
        print()
        print()
    if mainchoice == 2:
        while True:
            rn=int(input("ENTER YOUR ROOM NUMBER:"))
            if rn>130:
                print("INVALID INPUT")
                continue
            if rn<100:
                print("INVALID INPUT")
                continue
            else:
                break
        while True:
            print()
            print()
            print("-------SERVICES AVAILABLE-------")
            print("1.RESTAURANT**")
            print("2.GAME_BILL**")
            print("3.BEDDING")
            print("4.LAUNDRY")
            print("5.UPDATE MY RECORDS")
            print("6.BACK TO MAIN MENU")
            print()
            print("NOTE:**-EXTRA CHARGE TAKEN")
            print()

            service=int(input("ENTER THE SERVICE YOU WANT TO AVAIL:"))
            print()
            if service == 1:
                print()
                print("*****RESTAURANT MENU*****")
                print("1.water----->Rs20")
                print("2.tea----->Rs10")
                print("3.breakfast combo--->Rs90")
                print("4.lunch---->Rs110")
                print("5.dinner--->Rs150")

                items = int(input("HOW MANY ITEMS DID YOU BUY:"))

                for i in range(items):
                    r = int(input("ENTER YOUR CHOICE:"))
                    t = int(input("ENTER THE QUANTITY:"))

                    if r == 1:
                        X4 = X4 + (t * 20)

                    elif r == 2:
                        X4 = X4 + (t * 10)

                    elif r == 3:
                        X4 = X4 + (t * 90)

                    elif r == 4:
                        X4 = X4 + (t * 110)

                    else:
                        X4 = X4 + (t * 150)
             
                print("---------------------------------------")
                print("YOUR RESTAURANT BILL=", X4)
                print("---------------------------------------")
                print()
                print()
                tb=tb+X4
                mycursor.execute("update hotel_data set Total_Bill='{}' where Room_number={}".format(tb,rn))
                mycursor.execute("update Hotel_records set Restaurant_bill=Restaurant_bill + {} where Room_number={}".format(X4,rn))
                mydb.commit()

            if service == 2:

                print("******GAME MENU*******")
                print("1.Table tennis----->Rs60")
                print("2.Bowling----->Rs80")
                print("3.Snooker--->Rs70")
                print("4.Video games---->Rs90")
                print("5.Pool--->Rs50==6")
                u = int(input("HOW MANY ACTIVITIES DID YOU BUY:"))

                for i in range(u):
                    choice = int(input("ENTER YOUR CHOICE:"))
                    quantity = int(input("ENTER THE QUANTITY:"))
                    if choice == 1:
                        X5 = X5 + (quantity * 60)

                    elif choice == 2:
                        X5 = X5 + (quantity * 80)

                    elif choice == 3:
                        X5 = X5 + (quantity * 70)

                    elif choice == 4:
                        X5 = X5 + (quantity * 90)

                    else:
                        X5 = X5 + (quantity* 50)

                print("---------------------------------------")
                print("YOUR GAME BILL=", X5)
                print("---------------------------------------")
                print()
                print()
                tb=tb+X5
                mycursor.execute("update hotel_data set Total_Bill='{}' where Room_number={}".format(tb,rn))
                mycursor.execute("update Hotel_records set Game_bill=Game_bill + {} where Room_number={}".format(X5,rn))
                mydb.commit()

            if service==3:
                print("EXTRA BED COST IS Rs.850")
                sure=input("ARE YOU SURE FOR AN EXTRA BED AT RS.850--Y/N")
                if sure=="Y":
                    y=850
                    mycursor.execute("update Hotel_records set Extra_Bed=Extra_Bed + {} where Room_number={}".format(y,room_number_assigned))
                    mydb.commit()
                    bed=850
                    tb=tb+bed
                    mycursor.execute("update hotel_data set Total_Bill='{}' where Room_number={}".format(tb,rn))
                if sure=="N":
                    y=0
                    mycursor.execute("update hotel_records set Extra_bed={} where Room_number={}".format(y,rn))
                    mydb.commit()
                    bed=0
                    tb=tb+bed
                    mycursor.execute("update hotel_data set Total_Bill='{}' where Room_number={}".format(tb,rn))
            if service==4:
                print("LAUNDRY SERVICE CHARGE = Rs.50 per cloth")
                cloth=int(input("NUMBER OF CLOTHES"))
                laundry_bill=int(50*cloth)
                mycursor.execute("update Hotel_records set Laundry_bill=Laundry_bill + {} where Room_number={}".format(laundry_bill,room_number_assigned))
                mydb.commit()
                tb=tb+laundry_bill
                mycursor.execute("update hotel_data set Total_Bill='{}' where Room_number={}".format(tb,rn))

            if service==5:
                while True:
                    X1 = input("ENTER YOUR NAME:")
                    if all(i.isspace() or i.isalpha() for i in X1):
                        break
                    else:
                        print("INVALID INPUT")
                while True:
                    y = input("ENTER YOUR PHONE NUMBER:")
                    if len(y) > 10 or len(y) < 10:
                        print("INVALID INPUT")
                    elif any(i.isspace() or i.isalpha() for i in y):
                        print("INVALID INPUT")
                    else:
                        break
                mycursor.execute("update hotel_data set Name='{}' where Room_number={}".format(X1,rn))
                mycursor.execute("update hotel_data set Phone_number={} where Room_number={}".format(y,rn))
                mycursor.execute("update hotel_data set Total_Bill='{}' where Room_number={}".format(tb,rn))
                mydb.commit()
                mycursor.execute("update hotel_data set Total_Bill='{}' where Room_number={}".format(tb,rn))
    
            if service==6:
                break
            d=(18*tb)/100
            tb=tb+d
            mycursor.execute("update hotel_data set Total_Bill='{}' where Room_number={}".format(tb,rn))

    if mainchoice == 3:

        while True:
            R=int(input("ENTER YOUR ROOM NUMBER:"))
            if R>130:
                print("INVALID INPUT")
                continue
            if R<100:
                print("INVALID INPUT")
                continue
            else:
                break

        mycursor.execute("select Total_Bill from hotel_data where Room_number={}".format(R))
        x=mycursor.fetchall()
        for i in x:
            l=i
        for j in l:
            a=j
        print("-------------------------------")
        print(a)
        print("-------------------------------")
    if mainchoice == 4:
        exit()

             
