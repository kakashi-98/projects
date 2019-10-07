from tkinter import*
import time;
import datetime
import pygame,sys,random
from tkinter import messagebox

pygame.init()
root = Tk()
root.title("Online Marketing System")
root.geometry('1410x667+0+0')
root.configure(background='white')

#====================Frame===============

ABC=Frame(root,bg="powder blue",bd=20, relief=RIDGE)
ABC.grid()

ABC1=Frame(ABC, bg="cadet blue",bd=10, relief=RIDGE)
ABC1.grid(row=0,column=0,columnspan=4, sticky=W)

ABC2=Frame(ABC, bg="powder blue",bd=10, relief=RIDGE)
ABC2.grid(row=1,column=0, sticky=W)
          
ABC3=Frame(ABC, bg="powder blue",bd=10, relief=RIDGE)
ABC3.grid(row=1,column=1, sticky=W)
          
ABC4=Frame(ABC, bg="powder blue",bd=10, relief=RIDGE)
ABC4.grid(row=1,column=2, sticky=W)
          
ABC5=Frame(ABC4, bg="powder blue",bd=10, relief=RIDGE)
ABC5.grid(row=0,column=0, sticky=W)

ABC6=Frame(ABC4, bg="powder blue",bd=10, relief=RIDGE)
ABC6.grid(row=1,column=0,columnspan=4, sticky=W)


#====================Variables===============
Date1=StringVar()
Time1=StringVar()
Reccepit_Ref=StringVar()
Tax=DoubleVar()
Subtotal=DoubleVar()
Total=DoubleVar()

Jeans_w=DoubleVar()
Jacket=DoubleVar()
Footwear=DoubleVar()
Dresses=DoubleVar()
Skirts=DoubleVar()
SchoolUniform=DoubleVar()
Swimwear=DoubleVar()
Pyjamas=DoubleVar()

Jeans_m=DoubleVar()
Trousers=DoubleVar()
Shirts=DoubleVar()
Boots=DoubleVar()
Bedsheet=DoubleVar()
Pillow=DoubleVar()
Mattress=DoubleVar()
Curtain=DoubleVar()


Jeans_w.set("0")
Jacket.set("0")
Footwear.set("0")
Dresses.set("0")
Skirts.set("0")
SchoolUniform.set("0")
Swimwear.set("0")
Pyjamas.set("0")

Jeans_m.set("0")
Trousers.set("0")
Shirts.set("0")
Boots.set("0")
Bedsheet.set("0")
Pillow.set("0")
Mattress.set("0")
Curtain.set("0")
#====================Date And Time===============

Date1.set(time.strftime("%d/%m/%Y"))
Time1.set(time.strftime("%H:%M:%S"))

#============Functions=========
def iExit():
    qExit = messagebox.askyesno("Quit System","Do you want to quit?")
    if qExit > 0 :  
        root.destroy()
        return
    
def Reset():
    txtReceipt.delete("1.0",END)
    Jeans_w.set("0")
    Jacket.set("0")
    Footwear.set("0")
    Dresses.set("0")
    Skirts.set("0")
    SchoolUniform.set("0")
    Swimwear.set("0")
    Pyjamas.set("0")

    Jeans_m.set("0")
    Trousers.set("0")
    Shirts.set("0")
    Boots.set("0")
    Bedsheet.set("0")
    Pillow.set("0")
    Mattress.set("0")
    Curtain.set("0")

def Total_Bill():
    Item1=float(Jeans_w.get())
    Item2=float(Jacket.get())
    Item3=float(Footwear.get())
    Item4=float(Dresses.get())
    Item5=float(Skirts.get())
    Item6=float(SchoolUniform.get())
    Item7=float(Swimwear.get())
    Item8=float(Pyjamas.get())

    Item9=float(Jeans_m.get())
    Item10=float(Trousers.get())
    Item11=float(Shirts.get())
    Item12=float(Boots.get())
    Item13=float(Bedsheet.get())
    Item14=float(Pillow.get())
    Item15=float(Mattress.get())
    Item16=float(Curtain.get())

    Priceofitem1 = ("Rs") + str ('%.2f'%(Item1 * 499.99))
    Priceofitem2 = ("Rs") + str ('%.2f'%(Item2 * 1799.99))
    Priceofitem3 = ("Rs") + str ('%.2f'%(Item3 * 1299.99))
    Priceofitem4 = ("Rs") + str ('%.2f'%(Item4 * 1599.99))
    Priceofitem5 = ("Rs") + str ('%.2f'%(Item5 * 1499.99))
    Priceofitem6 = ("Rs") + str ('%.2f'%(Item6 * 549.99))
    Priceofitem7 = ("Rs") + str ('%.2f'%(Item7 * 299.99))
    Priceofitem8 = ("Rs") + str ('%.2f'%(Item8 * 349.99))
    Priceofitem9 = ("Rs") + str ('%.2f'%(Item9 * 2099.99))
    Priceofitem10 = ("Rs") + str ('%.2f'%(Item10 * 999.99))
    Priceofitem11 = ("Rs") + str ('%.2f'%(Item11 * 449.99))
    Priceofitem12 = ("Rs") + str ('%.2f'%(Item12 * 2599.99))
    Priceofitem13 = ("Rs") + str ('%.2f'%(Item13 * 899.99))
    Priceofitem14 = ("Rs") + str ('%.2f'%(Item14 * 159.99))
    Priceofitem15 = ("Rs") + str ('%.2f'%(Item15 * 779.99))
    Priceofitem16 = ("Rs") + str ('%.2f'%(Item16 * 859.99))

    PriceofWomen = (Item1 * 499.99) + (Item2 * 1799.99) + (Item3 * 1299.99) + (Item4 * 1599.99)
    PriceofKids = (Item5 * 1499.99) + (Item6 * 549.99) + (Item7 * 299.99) + (Item8 * 349.99)
    PriceofMen = (Item9 * 2099.99) + (Item10 * 999.99) + (Item11 * 449.99) + (Item12 * 2599.99)
    PriceofHomeware = (Item13 * 899.99) + (Item14 * 159.99) + (Item15 * 779.99) + (Item16 * 859.99)

    SubTotalofITEMS = ("Rs") + str('%.2f'%(PriceofWomen + PriceofKids +PriceofMen + PriceofHomeware))
    iTax = ("Rs") + str('%.2f'%((PriceofWomen + PriceofKids +PriceofMen + PriceofHomeware)*0.12))

    TT = (PriceofWomen + PriceofKids +PriceofMen + PriceofHomeware)
    TC = ((PriceofWomen + PriceofKids +PriceofMen + PriceofHomeware)*0.12)
    TotalCost = ("Rs") + str('%.2f'%(TT + TC))

    txtReceipt.delete("1.0",END)
    x = random.randint(10747,500298)
    randomRef = str(x)
    Reccepit_Ref.set("BILL"+randomRef)

    txtReceipt.insert(END,'Receipt Ref:\t\t\t\t'+Reccepit_Ref.get()+'\n'+ Date1.get()+'\t\t\t\t'+ Time1.get() + "\n")
    txtReceipt.insert(END,'---------------------------------------------------------------------------------'+ "\n")
    txtReceipt.insert(END,'Item:\t\t\t\t'+"Cost of Items\n")
    txtReceipt.insert(END,'---------------------------------------------------------------------------------'+ "\n")
    txtReceipt.insert(END,'Top:\t\t\t\t'+Priceofitem1+ "\n")
    txtReceipt.insert(END,'Jackets:\t\t\t\t'+Priceofitem2+ "\n")
    txtReceipt.insert(END,'Footwear:\t\t\t\t'+Priceofitem3+ "\n")
    txtReceipt.insert(END,'Dresses:\t\t\t\t'+Priceofitem4+ "\n")
    txtReceipt.insert(END,'Skirts:\t\t\t\t'+Priceofitem5+ "\n")
    txtReceipt.insert(END,'School Uniform:\t\t\t\t'+Priceofitem6+ "\n")
    txtReceipt.insert(END,'Swimwear:\t\t\t\t'+Priceofitem7+ "\n")
    txtReceipt.insert(END,'Pyjamas:\t\t\t\t'+Priceofitem8+ "\n")
    txtReceipt.insert(END,'Jeans:\t\t\t\t'+Priceofitem9+ "\n")
    txtReceipt.insert(END,'Trousers:\t\t\t\t'+Priceofitem10+ "\n")
    txtReceipt.insert(END,'Shirts:\t\t\t\t'+Priceofitem11+ "\n")
    txtReceipt.insert(END,'Boots:\t\t\t\t'+Priceofitem12+ "\n")
    txtReceipt.insert(END,'Bed Sheet:\t\t\t\t'+Priceofitem13+ "\n")
    txtReceipt.insert(END,'Pillows:\t\t\t\t'+Priceofitem14+ "\n")
    txtReceipt.insert(END,'Patterned Bedding:\t\t\t\t'+Priceofitem15+ "\n")
    txtReceipt.insert(END,'Mattress:\t\t\t\t'+Priceofitem16+ "\n")
    txtReceipt.insert(END,'Tax Paid:\t\t\t\t'+iTax+ "\n")
    txtReceipt.insert(END,'Sub Total:\t\t\t\t'+SubTotalofITEMS+ "\n")
    txtReceipt.insert(END,'Total Cost:\t\t\t\t'+TotalCost+ "\n")
    
#====================Frame===============

lblDate = Label (ABC1 , textvariable=Date1, font=('arial',30,'bold'), padx=9 , pady=9,bd=5,bg = "cadet Blue" , fg="Cornsilk" ,justify=CENTER).grid(row=0,column=0)

lblTitle = Label (ABC1 , text="\tOnline Marketing System\t", font=('arial',30,'bold'), padx=9 ,width=37, pady=9,bd=14,bg = "cadet Blue" , fg="Cornsilk" ,justify=CENTER).grid(row=0,column=1)

lblTime = Label (ABC1 , textvariable=Time1, font=('arial',30,'bold'), padx=9 , pady=9,bd=5,bg = "cadet Blue" , fg="Cornsilk" ,justify=CENTER).grid(row=0,column=2)

#====================label===============
lblWomen=Label(ABC2, text="Women" , font=('arial',20,'bold'),pady=1,bd=8, bg="Cadet Blue",fg="Cornsilk",width=25, justify=CENTER).grid(row=0,column=0,columnspan=4)

lblJeans=Label(ABC2, text="Top",bg="powder blue",font=('arial',18,'bold'), justify=LEFT).grid(row=1,column=0,sticky=W)

lblJacket=Label(ABC2, text="Jacket",bg="powder blue",font=('arial',18,'bold'), justify=LEFT).grid(row=2,column=0,sticky=W)

lblFootwear=Label(ABC2, text="Footwear",bg="powder blue",font=('arial',18,'bold'), justify=LEFT).grid(row=3,column=0,sticky=W)

lblDresses=Label(ABC2, text="Dresses",bg="powder blue",font=('arial',18,'bold'), justify=LEFT).grid(row=4,column=0,sticky=W)

lblSkirts=Label(ABC2, text="Skirts",bg="powder blue",font=('arial',18,'bold'), justify=LEFT).grid(row=6,column=0,sticky=W)

lblSchoolUniform=Label(ABC2, text="School Uniform",bg="powder blue",font=('arial',18,'bold'), justify=LEFT).grid(row=7,column=0,sticky=W)

lblSwimwear=Label(ABC2, text="Swimwear",bg="powder blue",font=('arial',18,'bold'), justify=LEFT).grid(row=8,column=0,sticky=W)

lblPyjamas=Label(ABC2, text="Pyjamas",bg="powder blue",font=('arial',18,'bold'), justify=LEFT).grid(row=9,column=0,sticky=W)



#====================txt===============


txtJeans=Entry(ABC2,textvariable=Jeans_w,font=('arial',18,'bold'),bd=8,bg="cyan",fg="black",width=12, justify=CENTER).grid(row=1,column=1,pady=1)

txtJacket=Entry(ABC2,textvariable=Jacket,font=('arial',18,'bold'),bd=8,bg="cyan",fg="black",width=12, justify=CENTER).grid(row=2,column=1,pady=1)

txtFootwear=Entry(ABC2,textvariable=Footwear,font=('arial',18,'bold'),bd=8,bg="cyan",fg="black",width=12, justify=CENTER).grid(row=3,column=1,pady=1)

txtDresses=Entry(ABC2,textvariable=Dresses,font=('arial',18,'bold'),bd=8,bg="cyan",fg="black",width=12, justify=CENTER).grid(row=4,column=1,pady=1)

lblKids=Label(ABC2,text="Kids",font=('arial',20,'bold'),bd=8,bg="Cadet blue",fg="Cornsilk",width=25, justify=CENTER).grid(row=5,column=0,columnspan=4)

txtSkirts=Entry(ABC2,textvariable=Skirts,font=('arial',18,'bold'),bd=8,bg="cyan",fg="black",width=12, justify=CENTER).grid(row=6,column=1,pady=1)

txtSchoolUniform=Entry(ABC2,textvariable=SchoolUniform,font=('arial',18,'bold'),bd=8,bg="cyan",fg="black",width=12, justify=CENTER).grid(row=7,column=1,pady=1)

txtSwimwears=Entry(ABC2,textvariable=Swimwear,font=('arial',18,'bold'),bd=8,bg="cyan",fg="black",width=12, justify=CENTER).grid(row=8,column=1,pady=1)

txtPyjamas=Entry(ABC2,textvariable=Pyjamas,font=('arial',18,'bold'),bd=8,bg="cyan",fg="black",width=12, justify=CENTER).grid(row=9,column=1,pady=1)


#====================label===============
lblmen=Label(ABC3, text="Men" , font=('arial',20,'bold'),pady=1,bd=8, bg="Cadet Blue",fg="Cornsilk",width=25, justify=CENTER).grid(row=0,column=0,columnspan=4)

lblJeans=Label(ABC3, text="Jeans",bg="powder blue",font=('arial',18,'bold'), justify=LEFT).grid(row=1,column=0,sticky=W)

lblTrousers=Label(ABC3, text="Trousers",bg="powder blue",font=('arial',18,'bold'), justify=LEFT).grid(row=2,column=0,sticky=W)

lblShirts=Label(ABC3, text="Shirts",bg="powder blue",font=('arial',18,'bold'), justify=LEFT).grid(row=3,column=0,sticky=W)

lblBoots=Label(ABC3, text="Boots",bg="powder blue",font=('arial',18,'bold'), justify=LEFT).grid(row=4,column=0,sticky=W)

lblBedsheet=Label(ABC3, text="BedSheets",bg="powder blue",font=('arial',18,'bold'), justify=LEFT).grid(row=6,column=0,sticky=W)

lblpillow=Label(ABC3, text="Pillow",bg="powder blue",font=('arial',18,'bold'), justify=LEFT).grid(row=7,column=0,sticky=W)

lblmattress=Label(ABC3, text="Mattress",bg="powder blue",font=('arial',18,'bold'), justify=LEFT).grid(row=8,column=0,sticky=W)

lblcurtain=Label(ABC3, text="Curtain",bg="powder blue",font=('arial',18,'bold'), justify=LEFT).grid(row=9,column=0,sticky=W)



#====================txt===============


txtJeans=Entry(ABC3, textvariable=Jeans_m,font=('arial',18,'bold'),bd=8,bg="cyan",fg="black",width=12, justify=CENTER).grid(row=1,column=1,pady=1)

txtTrousers=Entry(ABC3, textvariable=Trousers,font=('arial',18,'bold'),bd=8,bg="cyan",fg="black",width=12, justify=CENTER).grid(row=2,column=1,pady=1)

txtShirts=Entry(ABC3, textvariable=Shirts,font=('arial',18,'bold'),bd=8,bg="cyan",fg="black",width=12, justify=CENTER).grid(row=3,column=1,pady=1)

txtBoots=Entry(ABC3, textvariable=Boots,font=('arial',18,'bold'),bd=8,bg="cyan",fg="black",width=12, justify=CENTER).grid(row=4,column=1,pady=1)

lblHomeware=Label(ABC3,text="Homeware",font=('arial',20,'bold'),bd=8,bg="Cadet blue",fg="Cornsilk",width=25, justify=CENTER).grid(row=5,column=0,columnspan=4)

txtBedsheet=Entry(ABC3, textvariable=Bedsheet,font=('arial',18,'bold'),bd=8,bg="cyan",fg="black",width=12, justify=CENTER).grid(row=6,column=1,pady=1)

txtpillow=Entry(ABC3, textvariable=Pillow,font=('arial',18,'bold'),bd=8,bg="cyan",fg="black",width=12, justify=CENTER).grid(row=7,column=1,pady=1)

txtmattress=Entry(ABC3, textvariable=Mattress,font=('arial',18,'bold'),bd=8,bg="cyan",fg="black",width=12, justify=CENTER).grid(row=8,column=1,pady=1)

txtcurtain=Entry(ABC3, textvariable=Curtain,font=('arial',18,'bold'),bd=8,bg="cyan",fg="black",width=12, justify=CENTER).grid(row=9,column=1,pady=1)



#===============text===================

txtReceipt = Text(ABC5 , height = 24 , width = 50, bd = 20,font=('arial',9,'bold'))
txtReceipt.grid(row=0,column=0)

#===============button===================
btnTotal = Button(ABC6 , padx =15,pady = 1, bd=4 , fg="black" , font = ('arial',16,'bold'),width=7,bg="sky blue",text="Total",command=Total_Bill).grid(row=0,column=0)

btnRest = Button(ABC6 , padx =15,pady = 1, bd=4 , fg="black" , font = ('arial',16,'bold'),width=7,bg="sky blue",text="Reset",command=Reset).grid(row=0,column=1)

btnExit = Button(ABC6 , padx =15,pady = 1, bd=4 , fg="black" , font = ('arial',16,'bold'),width=7,bg="sky blue",text="Exit",command=iExit).grid(row=0,column=2)

root.mainloop()
